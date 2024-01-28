"""Python wrapper for getting data from the Ntuity API."""

from __future__ import annotations

import logging
from http import HTTPStatus
from typing import TYPE_CHECKING, Any

import orjson
from aiohttp import ClientSession

from .const import (
    ACCESSIBLE_SITES,
    DETAILS,
    LATEST_ENERGY_FLOW,
    HTTP_HEADERS,
)

from .exceptions import (
    ApiError,
    InvalidApiTokenError,
)

from .utils import (
    construct_url,
    valid_api_token,
)

_LOGGER = logging.getLogger(__name__)

class Ntuity:
    """Ntuity API wrapper."""

    def __init__(
        self,
        api_token: str,
        session: ClientSession,
        site_id: list[str] | None = None,
    ) -> None:
        """Initialize."""
        if not valid_api_token(api_token):
            raise InvalidApiTokenError(
                "Your API token is invalid. Please check your API token."
            )
        self._api_token = api_token
        self._session = session
        self._site_id = site_id if site_id is not None else []
        
    async def _async_get_data(self, url: str) -> dict[str, Any]:
        """Retrieve data from the ntuity API."""
        headers = HTTP_HEADERS.copy()
        headers["authorization"] = f"Bearer {self._api_token}"
        async with self._session.get(url, headers = headers) as resp:
            if resp.status == HTTPStatus.UNAUTHORIZED.value:
                raise InvalidApiTokenError(
                    "Your API token is invalid. Please check your API token."
                )
            if resp.status != HTTPStatus.OK.value:
                try:
                    error_text = orjson.loads(await resp.text())
                except orjson.JSONDecodeError as exc:
                    raise ApiError(
                        f"Can't decode API response: {exc}"
                    ) from exc
                raise ApiError(
                    f"Invalid response from ntuity API: {resp.status}"
                )
            
            _LOGGER.debug("Data retrieved from %s, status: %s", url, resp.status)
            data = await resp.json()

        return data if isinstance(data, dict) else data[0]
    
    async def async_get_accessible_sites(self) -> dict[str, Any]:
        """Get accessible sites."""
        url = construct_url(
            ACCESSIBLE_SITES,
            )
        data = await self._async_get_data(url)
        
        self._site_id = [site["id"] for site in data["sites"]]
        return self._site_id
    
    async def async_get_site_details(self) -> dict[str, Any]:
        """Get details for all site IDs."""
        site_details = {}
        for site_id in self._site_id:
            url = construct_url(
                DETAILS,
                site_id = site_id,
            )
            data = await self._async_get_data(url)
            site_details[site_id] = data
        
        return site_details
            
    async def async_get_latest_energy_flow(self) -> dict[str, Any]:
        """Get latest energy flow for all site IDs."""
        latest_energy_flows = {}
        for site_id in self._site_id:
            url = construct_url(
                LATEST_ENERGY_FLOW,
                site_id = site_id,
            )
            data = await self._async_get_data(url)
            latest_energy_flows[site_id] = data
        
        return latest_energy_flows
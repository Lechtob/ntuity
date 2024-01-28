"""Constants for Ntuity library."""
from __future__ import annotations

ACCESSIBLE_SITES: str = "accessible_sites"
DETAILS: str = "details"
LATEST_ENERGY_FLOW: str = "latest_energy_flow"

MAX_API_KEY_LENGTH = 32

ENDPOINT: str = "https://api.ntuity.io/v1"
HTTP_HEADERS: dict[str, str] = {
    "accept": "application/json",
    "authorization": "Bearer {api_token}",
}
REQUESTS_EXCEEDED: str = "The allowed number of requests has been exceeded."

URLS: dict[str, str] = {
    ACCESSIBLE_SITES: (
        "/sites"
    ),
    DETAILS: (
        "/sites/{site_id}"
    ),
    LATEST_ENERGY_FLOW: (
        "/sites/{site_id}/energy-flow/latest"
    )
}
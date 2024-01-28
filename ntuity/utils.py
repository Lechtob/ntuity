"""Utils for ntuity."""
from __future__ import annotations

from typing import Any

from .const import (
    ENDPOINT,
    #MAX_API_KEY_LENGTH,
    URLS,
)
MAX_API_KEY_LENGTH = 64
def valid_api_token(api_token: str) -> bool:
    """Return True if the API token is valid."""
    if isinstance(api_token, str) and 0 < len(api_token) <= MAX_API_KEY_LENGTH:
        return True
    
    return False

def construct_url(arg: str, **kwargs: str) -> str:
    """Construct the ntuity API URL."""
    return ENDPOINT + URLS[arg].format(**kwargs)

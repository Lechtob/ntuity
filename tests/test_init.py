"""Tests for the ntuity package."""
from http import HTTPStatus

import aiohttp
import orjson
import pytest
from aiohttp import ClientSession
from aioresponses import aioresponses

from ntuity import (
    Ntuity,
    ApiError,
    InvalidApiTokenError,
)


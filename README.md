[![GitHub Release][releases-shield]][releases]


# Ntuity API

Python wrapper for getting energy data from Ntuity API.

## API Token

To generate a API token go to https://neoom.ntuity.io/ and log into your account. After logging in open a site and generate a API token under API key.

## How to use the package
```python
"""Example of usage of the ntuity API."""
import asyncio
import logging
import json

from aiohttp import ClientError, ClientSession
from ntuity import (
    Ntuity,
    ApiError,
    InvalidApiTokenError,
)

API_TOKEN = "YOUR_API_TOKEN_HERE"

logging.basicConfig(level=logging.DEBUG)

async def main():
    """Run main function."""
    async with ClientSession() as session:
        try:
            ntuity = Ntuity(API_TOKEN, session)
            site_ids = await ntuity.async_get_accessible_sites()
            print("Found site IDs:", site_ids)
            site_details = await ntuity.async_get_site_details()
            energy_flow_data = await ntuity.async_get_latest_energy_flow()
            for site_id in site_ids:
                site_details_json = json.dumps(site_details[site_id], indent=4)
                energy_flow_data_json = json.dumps(energy_flow_data[site_id], indent=4)
                print(f"Site details for site {site_id}: \n{site_details_json}\n")
                print(f"Energy flow data for site {site_id}: \n{energy_flow_data_json}\n")
        except (
            ApiError,
            ClientError,
            InvalidApiTokenError,
        ) as err:
            print(err)
        else:
            print("Success! \n")
            
loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()
```

[releases]: https://github.com/Lechtob/ntuity/releases
[releases-shield]: https://img.shields.io/github/v/release/Lechtob/ntuity

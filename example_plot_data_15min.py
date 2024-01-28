"""Example of usage of the ntuity API."""
import asyncio
import logging
import json
import matplotlib.pyplot as plt

from aiohttp import ClientError, ClientSession
from ntuity import (
    Ntuity,
    ApiError,
    InvalidApiTokenError,
)

API_TOKEN = "xamSFi6MBYjP7VRUSYdiKbydazeyWndR"

logging.basicConfig(level=logging.INFO)

def create_power_consumption_plot(site_id, time_points, power_consumption_data):
    plt.plot(time_points, power_consumption_data)
    plt.title(f"Power consumption for site {site_id}")
    plt.xlabel("Time (min)")
    plt.ylabel("Power consumption (W)")
    plt.savefig(f"power_consumption_site_{site_id}.png")
    plt.show()
    

async def main():
    """Run main function."""
    async with ClientSession() as session:
        try:
            ntuity = Ntuity(API_TOKEN, session)
            site_ids = await ntuity.async_get_accessible_sites()
            print("Found site IDs:", site_ids)
            for site_id in site_ids:
                time_points = []
                power_consumption_data = []
                for _ in range(60):
                    energy_flow_data = await ntuity.async_get_latest_energy_flow()
                    site_data = energy_flow_data[site_id]
                    power_consumption_calc = site_data.get("power_consumption_calc")
                    value = power_consumption_calc.get("value")
                    if power_consumption_calc:
                        time_points.append((_*5)/60)
                        power_consumption_data.append(value)
                    await asyncio.sleep(5)
                create_power_consumption_plot(site_id, time_points, power_consumption_data)
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
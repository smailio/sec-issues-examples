import aiohttp
import asyncio
import os 
import logging

GEOCODE_API_KEY = os.getenv("GEOCODE_API_KEY")

async def make_api_call(address):
    url = f"https://api-adresse.data.gouv.fr/search/?q={address}&key={GEOCODE_API_KEY}"
    logging.info(f"get {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
            print(res)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_api_call("paris"))

if __name__ == '__main__':
    main()
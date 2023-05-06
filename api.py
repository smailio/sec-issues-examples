import aiohttp
import asyncio

async def make_api_call():
    url = "https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port&postcode=44380"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={
            "api-key" : "okjNNizdbIIjkzdfn21"
        }) as response:
            res = await response.json()
            print(res)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_api_call())

if __name__ == '__main__':
    main()
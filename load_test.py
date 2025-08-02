# load_test.py

import asyncio
import httpx
import time

URL = "http://127.0.0.1:8000"

async def call_sync():
    async with httpx.AsyncClient(timeout=120.0) as client:
        r = await client.get(f"{URL}/sync")
        return r.json()

async def call_async():
    async with httpx.AsyncClient(timeout=60.0) as client:
        r = await client.get(f"{URL}/async")
        return r.json()

async def run_many_requests(endpoint_func, name, n=5):
    print(f"\n🚀 Testing {name} with {n} concurrent requests...")
    start = time.time()
    results = await asyncio.gather(*[endpoint_func() for _ in range(n)])
    total_time = time.time() - start
    print(f"✅ {name} finished in {total_time:.2f} seconds\n")
    for i, res in enumerate(results):
        print(f"  • Response {i+1}: {res}")

async def main():
    await run_many_requests(call_sync, "SYNC", n=5)
    await run_many_requests(call_async, "ASYNC", n=5)

if __name__ == "__main__":
    asyncio.run(main())

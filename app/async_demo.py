# app/async_demo.py

from fastapi import FastAPI
import time
import asyncio

app = FastAPI(title="Async vs Sync Demo")

@app.get("/sync")
def sync_operation():
    """
    Simulates a CPU-bound blocking task by doing heavy computation.
    This will block the event loop when called concurrently.
    """
    count = 0
    for _ in range(10**8):  # Heavy computation
        count += 1
    return {"message": "Finished sync CPU-bound work"}

@app.get("/async")
async def async_operation():
    """
    Simulates an I/O-bound non-blocking task using asyncio.sleep.
    Multiple calls can run concurrently.
    """
    await asyncio.sleep(5)
    return {"message": "Finished async I/O-bound work"}

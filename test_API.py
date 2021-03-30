#!/usr/bin/env python3

import time
import requests

start = time.time()
sql = "SELECT * FROM zones LIMIT 10000"
for i in range(10):
    r = requests.get("http://api-proxy.auckland-cer.cloud.edu.au/QONQR/?query=" + sql)
print(f"AJAX took {time.time() - start}")


import asyncio
import websockets

async def hello():
    uri = "wss://api-proxy.auckland-cer.cloud.edu.au/QONQR/websocket"
    start = time.time()
    async with websockets.connect(uri, max_size=1e9) as websocket:
        for i in range(10):
            await websocket.send(sql)
            resp = await websocket.recv()
        print(f"WS took {time.time() - start}")

asyncio.get_event_loop().run_until_complete(hello())
import asyncio
import websockets
import json
from random import seed, randint
from datetime import datetime


async def connect(websocket, path):
    print("Received request")

    id = randint(1, 10000)
    desc = f'Description generated at {datetime.now().strftime("%Y/%m/%d %H:%M:%S")}'

    payload = { 
        "id": id,
        "desc": desc
    }

    await websocket.send(json.dumps(payload))
    print("Payload sent")

server = websockets.serve(connect, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
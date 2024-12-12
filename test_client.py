import asyncio
import websockets

async def test_client():
    print("Test Client: Connecting to the WebSocket server...")
    async with websockets.connect("ws://localhost:6789") as websocket:
        print("Test Client: Connected to WebSocket server")
        while True:
            data = await websocket.recv()
            print(f"Test Client: Data received: {data}")

asyncio.run(test_client())

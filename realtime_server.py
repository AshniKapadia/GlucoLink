import asyncio
import websockets
import json
import random

async def send_data(websocket):
    while True:
        # Simulate real-time data
        caution_data = [
            {"name": "🟡 John Smith", "glucose_level": f"{random.randint(60, 80)} mg/dL", "condition": "BG < 70 mg/dL (≥54 mg/dL)"},
            {"name": "🟡 Alice Green", "glucose_level": f"{random.randint(180, 200)} mg/dL", "condition": "BG > 180 mg/dL (≤250 mg/dL)"},
        ]
        warning_data = [
            {"name": "🔴 Emma Johnson", "glucose_level": f"{random.randint(40, 50)} mg/dL", "condition": "BG < 54 mg/dL", "address": "123 Maple St", "emergency_services": "Not On Route"},
        ]

        # Combine data into a single payload
        data = {"caution_data": caution_data, "warning_data": warning_data}

        # Send data as JSON
        await websocket.send(json.dumps(data))

        # Wait before sending the next update
        await asyncio.sleep(5)

async def main():
    async with websockets.serve(send_data, "localhost", 6789):
        print("WebSocket server running on ws://localhost:6789")
        await asyncio.Future()  # Run forever

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(main())

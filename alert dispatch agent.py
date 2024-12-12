import asyncio
import aiohttp
from uagents import Agent, Context, Model

class AlertMessage(Model):
    pt_id: str
    glucose_value: float
    alert_type: str  # "critical_high" or "critical_low"

# Initialize the dispatch agent (replace with your own seed keys if needed)
dispatch_agent = Agent(
    name="dispatch_agent",
    seed="my_private_key_seed"
)

# Placeholder EMS endpoint
EMS_ENDPOINT = "https://httpbin.org/post"

async def send_alert_to_ems(alert_data: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(EMS_ENDPOINT, json=alert_data) as response:
            if response.status == 200:
                print("Alert successfully sent to EMS.")
            else:
                print(f"Failed to send alert to EMS, status: {response.status}")

@dispatch_agent.on_message(model=AlertMessage)
async def handle_alert(ctx: Context, sender: str, msg: AlertMessage):
    print(f"Received alert: PtID={msg.pt_id}, Value={msg.glucose_value}, Type={msg.alert_type}")
    alert_payload = {
        "patient_id": msg.pt_id,
        "glucose_value": msg.glucose_value,
        "alert_type": msg.alert_type,
        "origin": sender
    }
    await send_alert_to_ems(alert_payload)

async def main():
    # Run the agent within the existing event loop
    await dispatch_agent.run_async()

if __name__ == "__main__":
    asyncio.run(main())

from slack_bolt.async_app import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient

from sharktank.shark_actions.user.jump import jump


async def message_handler(client: AsyncWebClient, say: AsyncSay, body: dict):
    event = body["event"]
    user = event["user"]
    text = event["text"]
    await client.reactions_add(
        channel=event["channel"],
        timestamp=event["ts"],
        name="loading2",
    )
    
    match text.lower():
        case "jump":
            await jump()
        case "help":
            await client.chat_postMessage(
                channel=event["channel"],
                text="hiiii!!!!!!! you can say to me `jump` and i will jump :D"
            )
        case _:
            await client.reactions_remove(
                channel=event["channel"],
                timestamp=event["ts"],
                name="loading2"
            )
            return
    await client.reactions_remove(
        channel=event["channel"],
        timestamp=event["ts"],
        name="loading2"
    )
    await client.reactions_add(
        channel=event["channel"],
        timestamp=event["ts"],
        name="blahaj_approved",
    )
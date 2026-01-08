from sharktank.config import config
from sharktank.tables import Shark

async def jump():
    from sharktank.env import env
    await env.slack_client.chat_postMessage(
        channel=config.slack.shark_channel,
        text=":rocket: The shark has jumped! :rocket:",
    )
    
    shark = await Shark.objects().first()
    if shark:
        shark.happiness += 1
        await shark.save()

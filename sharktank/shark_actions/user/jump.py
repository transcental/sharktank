from sharktank.config import config
from sharktank.tables import Shark

async def jump():
    from sharktank.env import env
    await env.slack_client.chat_postMessage(
        channel=config.slack.shark_channel,
        blocks=[
            {
                "type": "image",
                "image_url": "https://cassiopeia3000.transcental.dev/public/sharks/boing.gif",
                "alt_text": "A shark jumping out of the water"
            }
        ]
    )
    
    shark = await Shark.objects().first()
    if shark:
        shark.happiness += 1
        await shark.save()

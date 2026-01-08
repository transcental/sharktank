from sharktank.config import config
from sharktank.tables import Shark

async def jump():
    from sharktank.env import env
    shark = await Shark.objects().first()
    if shark:
        shark.happiness += 10
        await shark.save()
    
    await env.slack_client.chat_postMessage(
        channel=config.slack.shark_channel,
        blocks=[
            {
                "type": "image",
                "image_url": "https://cassiopeia3000.transcental.dev/static/sharks/boing.gif",
                "alt_text": "A shark jumping on a trampoline"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Boing Boing!* 🦈 The shark loves jumping and jumps happily on its trampoline :D\n+10 happiness!"
                }
            }
        ]
    )
    
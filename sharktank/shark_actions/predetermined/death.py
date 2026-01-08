from sharktank.tables import Shark
from sharktank.config import config

async def kill_shark():
    await Shark.delete(force=True)
    from sharktank.env import env
    await env.slack_client.chat_postMessage(
        channel=config.slack.shark_channel,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Press F to pay respects chat*\n Haj is dead!"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://cassiopeia3000.transcental.dev/static/sharks/sad.png",
                    "alt_text": "dead haj"
                }
            }
        ]
    )

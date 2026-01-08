import random
from sharktank.config import config
from sharktank.tables import Shark


async def heal():
    from sharktank.env import env
    shark = await Shark.objects().first()

    outcomes = [
        {
            "health": 15,
            "happiness": 5,
            "image": "https://sharktank.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark with bandages",
            "message": "*First aid applied!* 🩹 The shark got patched up with some bandages!\n+15 health, +5 happiness"
        },
        {
            "health": 20,
            "happiness": 8,
            "image": "https://sharktank.transcental.dev/public/sharks/happy.png",
            "alt_text": "A shark taking medicine",
            "message": "*Medicine time!* 💊 The shark took its medicine like a good shark!\n+20 health, +8 happiness"
        },
        {
            "health": 25,
            "happiness": 10,
            "image": "https://sharktank.transcental.dev/public/sharks/happy.png",
            "alt_text": "A shark visiting the doctor",
            "message": "*Doctor visit!* 🏥 The shark saw a doctor and got proper treatment!\n+25 health, +10 happiness"
        },
        {
            "health": 10,
            "happiness": 3,
            "image": "https://sharktank.transcental.dev/public/sharks/boing.gif",
            "alt_text": "A shark resting to heal",
            "message": "*Rest and recovery!* 😌 The shark took some time to rest and recuperate.\n+10 health, +3 happiness"
        }
    ]

    outcome = random.choice(outcomes)

    if shark:
        shark.health += outcome["health"]
        shark.happiness += outcome["happiness"]
        await shark.save()

    await env.slack_client.chat_postMessage(
        channel=config.slack.shark_channel,
        blocks=[
            {
                "type": "image",
                "image_url": outcome["image"],
                "alt_text": outcome["alt_text"]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": outcome["message"]
                }
            }
        ]
    )

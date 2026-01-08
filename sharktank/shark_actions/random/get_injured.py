import random
from sharktank.config import config
from sharktank.tables import Shark


async def get_injured():
    from sharktank.env import env
    shark = await Shark.objects().first()

    outcomes = [
        {
            "hunger": 2,
            "happiness": -5,
            "health": -8,
            "image": "https://sharktank.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark with scratches",
            "message": "The shark scraped against some sharp coral! Ouch! 🩹\n-8 health, -5 happiness, +2 hunger"
        },
        {
            "hunger": 0,
            "happiness": -7,
            "health": -10,
            "image": "https://sharktank.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark that got bitten",
            "message": "The shark got into a fight with another shark and got bitten! 🦷\n-10 health, -7 happiness"
        },
        {
            "hunger": 3,
            "happiness": -4,
            "health": -6,
            "image": "https://sharktank.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark stung by a jellyfish",
            "message": "The shark swam into a jellyfish and got stung! 🎐\n-6 health, -4 happiness, +3 hunger"
        },
        {
            "hunger": 0,
            "happiness": -8,
            "health": -12,
            "image": "https://sharktank.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark caught on a fishing hook",
            "message": "The shark got caught on a fishing hook! That really hurt! 🪝\n-12 health, -8 happiness"
        },
        {
            "hunger": 1,
            "happiness": -3,
            "health": -5,
            "image": "https://sharktank.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark that bumped into something",
            "message": "The shark bumped its nose on a rock... bonk! 🪨\n-5 health, -3 happiness, +1 hunger"
        },
        {
            "hunger": 0,
            "happiness": -6,
            "health": -9,
            "image": "https://sharktank.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark tangled in a fishing net",
            "message": "The shark got tangled in a fishing net and struggled to escape! 🥅\n-9 health, -6 happiness"
        }
    ]

    outcome = random.choice(outcomes)

    if shark:
        shark.hunger += outcome["hunger"]
        shark.happiness += outcome["happiness"]
        shark.health += outcome["health"]
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

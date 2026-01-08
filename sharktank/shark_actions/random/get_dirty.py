import random
from sharktank.config import config
from sharktank.tables import Shark


async def get_dirty():
    from sharktank.env import env
    shark = await Shark.objects().first()

    outcomes = [
        {
            "hunger": 0,
            "happiness": -3,
            "health": -5,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/sad.png",
            "alt_text": "A dirty shark covered in algae",
            "message": "The shark swam through some murky water and got covered in algae! 🦠\n-5 health, -3 happiness"
        },
        {
            "hunger": 0,
            "happiness": -2,
            "health": -3,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/sad.png",
            "alt_text": "A muddy shark",
            "message": "The shark rolled around in the sandy bottom and got all muddy! 💩\n-3 health, -2 happiness"
        },
        {
            "hunger": 0,
            "happiness": -4,
            "health": -7,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark covered in oil",
            "message": "The shark swam through an oil slick... this is bad! 🛢️\n-7 health, -4 happiness"
        },
        {
            "hunger": 2,
            "happiness": -1,
            "health": -4,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark tangled in seaweed",
            "message": "The shark got tangled in some rotting seaweed 🌿\n-4 health, -1 happiness, +2 hunger"
        },
        {
            "hunger": 0,
            "happiness": -5,
            "health": -6,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/sad.png",
            "alt_text": "A shark in polluted water",
            "message": "The shark wandered into polluted waters and feels gross 🤢\n-6 health, -5 happiness"
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

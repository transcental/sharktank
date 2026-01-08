import random
from sharktank.config import config
from sharktank.tables import Shark


async def clean():
    from sharktank.env import env
    shark = await Shark.objects().first()

    outcomes = [
        {
            "hunger": 1,
            "happiness": 5,
            "health": 8,
            "image": "https://sharktank.transcental.dev/public/sharks/scrub.png",
            "alt_text": "A shark getting scrubbed clean",
            "message": "*Scrub scrub!* 🧽 You give the shark a good scrub and it sparkles!\n+8 health, +5 happiness, +1 hunger"
        },
        {
            "hunger": 0,
            "happiness": 7,
            "health": 6,
            "image": "https://sharktank.transcental.dev/public/sharks/bubble_bath.png",
            "alt_text": "A shark enjoying a bubble bath",
            "message": "*Splish splash!* 🛁 The shark enjoys a relaxing bubble bath!\n+6 health, +7 happiness"
        },
        {
            "hunger": 0,
            "happiness": 3,
            "health": 10,
            "image": "https://sharktank.transcental.dev/public/sharks/power_wash.png",
            "alt_text": "A shark being power washed",
            "message": "*WHOOOOSH!* 💦 Power wash mode activated! The shark is squeaky clean!\n+10 health, +3 happiness"
        },
        {
            "hunger": 2,
            "happiness": 4,
            "health": 5,
            "image": "https://sharktank.transcental.dev/public/sharks/cleaner_fish.png",
            "alt_text": "Cleaner fish helping the shark",
            "message": "*Nibble nibble!* 🐟 Some cleaner fish friends help remove the gunk!\n+5 health, +4 happiness, +2 hunger"
        },
        {
            "hunger": 0,
            "happiness": 6,
            "health": 7,
            "image": "https://sharktank.transcental.dev/public/sharks/fresh_water.png",
            "alt_text": "A shark in crystal clear water",
            "message": "*So fresh!* ✨ You move the shark to crystal clear waters!\n+7 health, +6 happiness"
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
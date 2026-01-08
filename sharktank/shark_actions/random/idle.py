import random
from sharktank.config import config
from sharktank.tables import Shark

async def idle():
    from sharktank.env import env
    shark = await Shark.objects().first()
    
    outcomes = [
        {
            "hunger": 5,
            "happiness": -2,
            "health": 0,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/idle.png",
            "alt_text": "A shark doing nothing",
            "message": "The shark is idly swimming around... 🦈\n+5 hunger, -2 happiness"
        },
        {
            "hunger": 3,
            "happiness": 3,
            "health": 0,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/nap.png",
            "alt_text": "A shark taking a nap",
            "message": "The shark takes a nap and feels refreshed 😴\n+3 hunger, +3 happiness"
        },
        {
            "hunger": 2,
            "happiness": -5,
            "health": -1,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/bored.png",
            "alt_text": "A bored shark",
            "message": "The shark looks bored and a bit grumpy 😒\n+2 hunger, -5 happiness, -1 health"
        },
        {
            "hunger": 1,
            "happiness": 4,
            "health": 0,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/bubble.png",
            "alt_text": "A shark playing with bubbles",
            "message": "The shark plays with bubbles and smiles 🫧\n+1 hunger, +4 happiness"
        },
        {
            "hunger": 6,
            "happiness": 1,
            "health": 0,
            "image": "https://cassiopeia3000.transcental.dev/public/sharks/lookingfourfood.png",
            "alt_text": "A hungry shark looking for food",
            "message": "The shark looks around hungrily... 👀\n+6 hunger, +1 happiness"
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

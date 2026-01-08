import logging
import random

from sharktank.shark_actions.random.idle import idle
from sharktank.shark_actions.random.get_dirty import get_dirty
from sharktank.shark_actions.random.get_injured import get_injured


async def task():
    logging.info("Hi, i'm a task :3")

    if random.randint(0, 1) == 1: # Add some randomness to the timing ig idk
        # Randomly choose between idle, get_dirty, and get_injured actions
        action = random.choice([idle, get_dirty, get_injured])
        await action()

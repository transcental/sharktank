import logging
import random


async def task():
    logging.info("Hi, i'm a task :3")

    if random.randint(0, 1) == 1: # Add some randomness to the timing ig idk
        ...

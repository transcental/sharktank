from sharktank.shark_actions.predetermined.death import kill_shark
from sharktank.tables import Shark


async def setup_shark(reset: bool = False):
    shark = await Shark.objects().first()
    if not shark or reset:
        shark = Shark()
        
        await shark.save()

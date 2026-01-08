# An example of how to create a table. Read the docs for more info: https://piccolo-orm.readthedocs.io/

from piccolo.table import Table
from piccolo.columns import Integer, Varchar, Timestamptz

class Shark(Table):
    name = Varchar(length=20, index=True)
    age = Integer()
    mood = Integer()
    health = Integer()
    hunger = Integer()
    happiness = Integer()
    created_at = Timestamptz()

from pony.orm import *
import os
from pony.orm.examples.estore import Category

db = Database()


class Request(db.Entity):
    id = PrimaryKey(int, auto=True)
    name: Required(str)
    parent_id: Required(int)
    slug: Required(str)

    @property
    def get_access(self):
        return select(c for c in Category if c.path.startswith(cat.path + '/' + cat.name))

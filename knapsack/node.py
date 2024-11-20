from dataclasses import dataclass, field


# instantiate with Item(value = , weight = )
# update level with itemInstance.level = index
@dataclass
class Item:
    value: int
    weight: int
    level: int = field(default=-1)


class Node():
    def __init__(self, item):
        self.item = item
        

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
        self.max_included = -1
        self.max_excluded = -1
        self.yes = None
        self.no = None
        self.capacity = 0
        self.cur_value = 0

    def visit(self, items):
        if self.item.level == len(items) - 1:
            # leaf node
            print("reached leaf", self.item)
            return
        # create 2 new child nodes of next item type
        self.yes = Node(items[self.item.level + 1])
        self.no = Node(items[self.item.level + 1])
        print("created children", self.yes, self.no)
        return



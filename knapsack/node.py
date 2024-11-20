from dataclasses import dataclass, field


# instantiate with Item(value = , weight = )
# update level with itemInstance.level = index
@dataclass
class Item:
    value: int
    weight: int
    level: int = field(default=-1)


class Node():
    def __init__(self, item, capacity, parent = None):
        self.parent = parent
        self.item = item
        self.max_included = -1
        self.max_excluded = -1
        self.yes = None
        self.no = None
        self.capacity = 0
        self.cur_value = 0

    def visit(self, stack, items):
        if self.item.level == len(items) - 1:
            # leaf node
            return
        if self.item.weight > self.capacity:
            #todo don't add the yes side
            pass
        # create 2 new child nodes of next item type
        self.yes = Node(items[self.item.level + 1], self.capacity - self.item.weight, self)
        self.no = Node(items[self.item.level + 1], self.capacity, self)
        stack.append(self.yes)
        stack.append(self.no)
        return



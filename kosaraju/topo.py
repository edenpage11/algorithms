
def TopoSort(digraph):
    unexplored = set(digraph.keys())
    topoOrder = {}
    for key in digraph.keys():
        topoOrder[key] = None
    curLabel = len(unexplored)
    for vertex in digraph.keys():
        if vertex in unexplored:
            curLabel = DfsTopo(digraph, vertex, unexplored, curLabel, topoOrder)
    return topoOrder


def DfsTopo(digraph, vertex, unexplored, curLabel, topoOrder):
    unexplored.remove(vertex)
    for edge in digraph[vertex]:
        if edge in unexplored:
            curLabel = DfsTopo(digraph, edge, unexplored, curLabel, topoOrder)
    topoOrder[vertex] = curLabel
    return curLabel - 1


def main():
    digraph = {
        "1": ["4"],
        "2": ["8"],
        "3": ["6"],
        "4": ["7"],
        "5": ["2"],
        "6": ["9"],
        "7": ["1"],
        "8": ["5", "6"],
        "9": ["7", "3"]
    }
    TopoSort(digraph)


if __name__ == '__main__':
    main()

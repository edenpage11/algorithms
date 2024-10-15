numSCC = 0

## read in files and store edges as dictionary
def get_edges(file):
    G = {}
    G_rev = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                num1, num2 = line.split(' ')
                if num1 in G.keys():
                    G[(num1)] += [(num2)]
                else: 
                    G[(num1)] = [(num2)]
                if num2 in G_rev.keys():
                    G_rev[(num2)] += [(num1)]
                else: 
                    G_rev[(num2)] = [(num1)]

    return G, G_rev

def TopoSort(digraph):
    unexplored = set(digraph.keys())
    topoOrder = {}
    for key in digraph.keys():
        topoOrder[key] = None
    curLabel = len(unexplored)
    for vertex in digraph.keys():
        if vertex in unexplored:
            curLabel = DfsTopo(digraph, vertex, unexplored, curLabel, topoOrder)
    reverse_topo = {v: k for k, v in topoOrder.items()}
    sorted_keys = sorted(reverse_topo.keys())
    sorted_dict = {key: reverse_topo[key] for key in sorted_keys}
    return sorted_dict


def DfsTopo(digraph, vertex, unexplored, curLabel, topoOrder):
    unexplored.remove(vertex)
    if digraph[vertex] != None:
        for edge in digraph[vertex]:
            if edge in unexplored:
                curLabel = DfsTopo(digraph, edge, unexplored, curLabel, topoOrder)
    topoOrder[vertex] = curLabel
    return curLabel - 1

def Dfs(G, vertex, unexplored, SCCSize = 0):
    unexplored.remove(vertex)
    global numSCC
    SCCSize += 1
    if G[vertex] != None:
        for edge in G[vertex]:
            if edge in unexplored:
                SCCSize = Dfs(G, edge, unexplored, SCCSize)
    return SCCSize

def Kosaraju(G, G_rev):
    topo_order = TopoSort(G_rev)
    unexplored = set(G.keys())
    global numSCC
    numSCC = 0
    SCCsize = []
    for vertex in topo_order.values():
        if vertex in unexplored:
            numSCC += 1
            SCCsize.append(Dfs(G, vertex, unexplored))
    SCCsize = sorted(SCCsize, reverse = True)
    fiveSCC = [0] * 5
    for i in range(min(5, len(SCCsize))):
        fiveSCC[i] = SCCsize[i]
    return numSCC, fiveSCC

def main():
    G, G_rev = get_edges("problem8.10.txt")
    noOutgoing = []
    for values in G.values():
        for value in values:
            if value not in G.keys() and value not in noOutgoing:
                noOutgoing.append(value)
    for value in noOutgoing:
        G[value] = None
    noOutgoing = []
    for values in G_rev.values():
        for value in values:
            if value not in G_rev.keys() and value not in noOutgoing:
                noOutgoing.append(value)
    for value in noOutgoing:
        G_rev[value] = None
    print(Kosaraju(G, G_rev))

if __name__ == "__main__":
    main()
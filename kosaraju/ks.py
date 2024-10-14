## read in files and store edges as dictionary
def get_edges(file):
    G = {}
    G_rev = {}
    with open(file, "r") as f:
        for line in f:
            if line[0] in G.keys():
                G[int(line[0])] += [int(line[2])]
            else: 
                G[int(line[0])] = [int(line[2])]
            if line[2] in G_rev.keys():
                G_rev[int(line[2])] += [int(line[0])]
            else: 
                G_rev[int(line[2])] = [int(line[0])]

    return G, G_rev

print(get_edges("kosaraju\ex8.txt"))
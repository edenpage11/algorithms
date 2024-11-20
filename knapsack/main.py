from node import Item, Node


def read_file(filename):
    with open(filename, 'r') as f:
        firstline = f.readline()
        capacity, depth = firstline.strip().split(" ")
        itemList = []
        for line in f:
            value, weight = line.strip().split(" ")
            itemList.append(Item(int(value), int(weight)))
        itemList = sorted(
            itemList, key=lambda item: item.value / item.weight, reverse=True)
        for i in range(len(itemList)):
            itemList[i].level = i
    return capacity, depth, itemList

def main():
    filename = "problem16.7test.txt"
    capacity, depth, itemList = read_file(filename)


if __name__ == '__main__':
    main()

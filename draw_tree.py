import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


def get_left(arr, i):
    index = 2 * i + 1
    return (index, arr[index]) if index < len(arr) else None


def get_right(arr, i):
    index = 2 * i + 2
    return (index, arr[index]) if index < len(arr) else None


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def add_children(self, arr, i):
        left = get_left(arr, i)
        if left:
            self.left = Node(left[1])
            self.left.add_children(arr, left[0])
        right = get_right(arr, i)
        if right:
            self.right = Node(right[1])
            self.right.add_children(arr, right[0])


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == "__main__":
    nums = [0, 4, 5, 10, 1, 3]
    heapq.heapify(nums)
    root = Node(nums[0])
    root.add_children(nums, 0)
    draw_tree(root)

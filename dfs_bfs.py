import time

from networkx import DiGraph

from draw_tree import *
import heapq


def draw_tree_color(tree_root: Node):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(0.5)
    return tree


def dfs(node: Node, root: Node):
    if node.color != "skyblue":
        return
    node.color = "gray"
    draw_tree_color(root)
    if node.right:
        dfs(node.right, root)
    if node.left:
        dfs(node.left, root)
    node.color = "black"
    draw_tree_color(root)


def bfs(node: Node, root: Node, list: list):
    if node.color == "black":
        return
    node.color = "black"
    draw_tree_color(root)
    if node.right:
        node.right.color = "gray"
        draw_tree_color(root)
        list.append(node.right)
    if node.left:
        node.left.color = "gray"
        draw_tree_color(root)
        list.append(node.left)
    if list:
        bfs(list.pop(0), root, list)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
heapq.heapify(nums)
root = Node(nums[0])
root.add_children(nums, 0)
draw_tree_color(root)
dfs(root, root)

root = Node(nums[0])
root.add_children(nums, 0)
draw_tree_color(root)
bfs(root, root, list())

import node_unit

# Завдання 1
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

# Завдання 2
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Завдання 3
def sum_all_nodes(node):
    sums = node.val
    if node.right:
        sums += sum_all_nodes(node.right)
    if node.left:
        sums += sum_all_nodes(node.left)
    return sums


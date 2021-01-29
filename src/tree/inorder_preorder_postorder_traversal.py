from src.tree.TreeNode import Node

def in_order_traversal_recursive(node):
    if node == None:
        return
    in_order_traversal_recursive(node.leftNode)
    print(node.data, end=' ')
    in_order_traversal_recursive(node.rightNode)

def pre_order_traversal_recursive(node):
    if node == None:
        return
    print(node.data, end=' ')
    pre_order_traversal_recursive(node.leftNode)
    pre_order_traversal_recursive(node.rightNode)

def post_order_traversal_recursive(node):
    if node == None:
        return
    post_order_traversal_recursive(node.leftNode)
    post_order_traversal_recursive(node.rightNode)
    print(node.data, end=' ')

def pre_order_traversal_iterative(node):
    stack = []
    stack.append(node)
    while (len(stack) > 0):
        current = stack.pop()
        print(current.data, end=" ")
        if current.rightNode != None:
            stack.append(current.rightNode)
        if current.leftNode != None:
            stack.append(current.leftNode)

def in_order_traversal_iterative(node):
    stack = []
    current = node
    while (current != None or len(stack) > 0):
        if current != None:
            stack.append(current)
            current = current.leftNode
        else:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.rightNode

def post_order_traversal_iterative(node):
    stack = []
    current = node
    while (current != None or len(stack) > 0):
        if current != None:
            stack.append(current)
            current = current.leftNode
        else:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.rightNode


if __name__ == '__main__':
    #                           1
    #                         /   \
    #                        2     3
    #                      /   \
    #                     4      5

    # pre_order ==> root, left, right
    # in_order ==> left, root, right
    # post_order ==> left, right, root ()

    node = Node(1)
    node.leftNode = Node(2)
    node.rightNode = Node(3)
    node.leftNode.leftNode = Node(4)
    node.leftNode.rightNode = Node(5)

    # print("in_order_traversal_recursive ==>")
    # in_order_traversal_recursive(node)
    # print()
    # print("pre_order_traversal_recursive ==>")
    # pre_order_traversal_recursive(node)
    # print()
    print("post_order_traversal_recursive ==>")
    post_order_traversal_recursive(node)
    print()
    # print("pre_order_traversal_iterative ==>")
    # pre_order_traversal_iterative(node)
    # print()
    # print("in_order_traversal_iterative ==>")
    # in_order_traversal_iterative(node)

    print("post_order_traversal_iterative ==>")
    post_order_traversal_iterative(node)
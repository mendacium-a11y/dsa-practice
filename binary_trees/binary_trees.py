from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return
    
    # Create an empty queue for level-order traversal
    queue = deque()
    
    # Enqueue the root node with its level (level 0)
    queue.append((root, 0))
    
    current_level = 0  # Initialize the current level
    
    while queue:
        current_node, node_level = queue.popleft()
        
        # If the level changes, print a newline to start a new level
        if node_level > current_level:
            # print("\nLevel", node_level, ": ", end='')
            print()
            current_level = node_level
        
        # Print the data of the current node
        print(current_node.data, end=' ')
        
        # Enqueue the left child with its level (level + 1) if it exists
        if current_node.left:
            queue.append((current_node.left, node_level + 1))
        
        # Enqueue the right child with its level (level + 1) if it exists
        if current_node.right:
            queue.append((current_node.right, node_level + 1))

# Example usage
if __name__ == '__main__':
    # Creating a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("Level-order traversal of the binary tree:")
    level_order_traversal(root)

# ast_node.py
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        """
        Initialize a Node in the Abstract Syntax Tree (AST).
        
        Args:
            node_type (str): "operator" for AND/OR, "operand" for conditions.
            left (Node): Left child node.
            right (Node): Right child node.
            value (Any): The value associated with the operand (e.g., age, salary).
        """
        self.node_type = node_type  # "operator" or "operand"
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Operand value for comparison

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value})"


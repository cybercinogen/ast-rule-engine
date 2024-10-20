
from rule_parser import parse_rule
from utils import parse_condition, compare
from ast_node import Node  # Import the Node class here
from zeotap_functions import evaluate_custom_function  # To evaluate custom business logic

def create_rule(rule_string):
    """Create a rule by parsing the rule string and returning the AST."""
    return parse_rule(rule_string)

def evaluate_rule(ast, data):
    """Recursively evaluate the AST based on node type (operator or operand)."""
    if ast.node_type == 'operator':
        if ast.value == 'AND':
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == 'OR':
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)

    elif ast.node_type == 'operand':
        # Special check for custom functions
        if "total_user_spend" in ast.value:
            return evaluate_custom_function("total_user_spend", data) > 50000
        
        # Parse the condition (e.g., user.age > 18)
        condition = ast.value
        print(f"Evaluating condition: {condition}")  # Debug output
        attribute, operator, value = parse_condition(condition)
        return compare(data.get(attribute), operator, value)  # Ensure to use .get() for safe access
    
    return False  # Fallback if no valid node_type found

def rebuild_ast(ast_dict):
    """Rebuild the AST from its dictionary representation (e.g., when retrieved from the database)."""
    if ast_dict['node_type'] == 'operator':
        # Recursive call to rebuild left and right nodes
        return Node(
            node_type=ast_dict['node_type'],
            left=rebuild_ast(ast_dict['left']),
            right=rebuild_ast(ast_dict['right']),
            value=ast_dict['value']
        )
    elif ast_dict['node_type'] == 'operand':
        # Operand nodes only have a value
        return Node(
            node_type=ast_dict['node_type'],
            value=ast_dict['value']
        )

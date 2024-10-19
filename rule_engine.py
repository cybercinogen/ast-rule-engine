from rule_parser import parse_rule
from utils import parse_condition, compare
from ast_node import Node  # Import Node class here
from zeotap_functions import evaluate_custom_function

def create_rule(rule_string):
    return parse_rule(rule_string)

def evaluate_rule(ast, data):
    if ast.node_type == 'operator':
        if ast.value == 'AND':
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == 'OR':
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    elif ast.node_type == 'operand':
        if "total_user_spend" in ast.value:
            return evaluate_custom_function("total_user_spend", data) > 50000
        condition = ast.value
        attribute, operator, value = parse_condition(condition)
        return compare(data[attribute], operator, value)
    return False

def rebuild_ast(ast_dict):
    if ast_dict['node_type'] == 'operator':
        return Node(
            node_type=ast_dict['node_type'],
            left=rebuild_ast(ast_dict['left']),
            right=rebuild_ast(ast_dict['right']),
            value=ast_dict['value']
        )
    elif ast_dict['node_type'] == 'operand':
        return Node(
            node_type=ast_dict['node_type'],
            value=ast_dict['value']
        )

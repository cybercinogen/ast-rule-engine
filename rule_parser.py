# rule_parser.py
from ast_node import Node

def parse_rule(rule_string):
    """
    Parse a rule string and create an AST.
    
    Args:
        rule_string (str): The rule in string format (e.g., "age > 30 AND department = 'Sales'")
    
    Returns:
        Node: The root node of the generated AST.
    """
    # Split rule by the "AND" operator (you can extend this to handle more complex operators)
    if 'AND' in rule_string:
        left_rule, right_rule = rule_string.split('AND', 1)
        left_node = parse_rule(left_rule.strip())
        right_node = parse_rule(right_rule.strip())
        return Node(node_type='operator', left=left_node, right=right_node, value='AND')

    elif 'OR' in rule_string:
        left_rule, right_rule = rule_string.split('OR', 1)
        left_node = parse_rule(left_rule.strip())
        right_node = parse_rule(right_rule.strip())
        return Node(node_type='operator', left=left_node, right=right_node, value='OR')

    # Base case: it's an operand
    else:
        return Node(node_type='operand', value=rule_string.strip())
    
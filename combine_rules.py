from rule_engine import create_rule
from ast_node import Node

def combine_rules(rule_strings):
    """
    Combines multiple rule strings into a single AST.
    
    Args:
        rule_strings (list): List of rule strings to combine.
    
    Returns:
        Node: Root node of the combined AST.
    """
    if not rule_strings:
        return None
    
    combined_ast = create_rule(rule_strings[0])

    for rule_string in rule_strings[1:]:
        new_ast = create_rule(rule_string)
        # Combine them using AND, but this can be optimized for frequent operators
        combined_ast = Node(
            node_type='operator',
            left=combined_ast,
            right=new_ast,
            value='AND'
        )

    return combined_ast
 

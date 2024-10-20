# execution_engine.py
from rule_engine import OperandNode

class ExecutionEngine:
    def __init__(self, rule_ast):
        self.rule_ast = rule_ast

    def evaluate(self, context):
        # Evaluates the rule AST on the provided context (user data)
        if isinstance(self.rule_ast, OperandNode):
            return eval(self.rule_ast.value, {}, context)  # Safe evaluation of the rule
        return None

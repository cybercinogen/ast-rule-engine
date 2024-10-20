from flask import Flask, request, jsonify
from rule_engine import create_rule, evaluate_rule
from combine_rules import combine_rules
from database import store_rule, modify_rule, retrieve_rule
from zeotap_functions import register_custom_functions

app = Flask(__name__)

# Register custom functions for the rule engine
register_custom_functions()

@app.route('/')
def home():
    return "Welcome to the AST Rule Engine!"

# Define the Node class (ensure this is in the rule_engine file)
class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            "node_type": self.node_type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }

# Test case: Create individual rules and verify AST
@app.route('/test_create_rules', methods=['GET'])
def test_create_rules():
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    
    ast1 = create_rule(rule1)
    ast2 = create_rule(rule2)
    
    return jsonify({
        "message": "Individual rules created and ASTs generated",
        "rule1_ast": ast1.to_dict(),  # Use to_dict() to convert to JSON serializable format
        "rule2_ast": ast2.to_dict()
    }), 200

# Test case: Combine rules and verify combined AST
@app.route('/test_combine_rules', methods=['GET'])
def test_combine_rules():
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    
    combined_ast = combine_rules([rule1, rule2])
    
    return jsonify({
        "message": "Rules combined",
        "combined_ast": combined_ast.to_dict()  # Use to_dict() to convert to JSON serializable format
    }), 200

# Test case: Evaluate rule against sample user data
@app.route('/test_evaluate_rule', methods=['POST'])
def test_evaluate_rule():
    user_data = request.json.get('user_data')  # Extract user_data from the JSON body

    # Define a sample rule to create the AST
    sample_rule = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    ast = create_rule(sample_rule)  # Create AST from the sample rule

    # Evaluate the rule against user data
    result = evaluate_rule(ast, user_data)

    return jsonify({
        "result": result
    })

# Test case: Explore combining additional rules
@app.route('/test_explore_combine_rules', methods=['GET'])
def test_explore_combine_rules():
    rule1 = "((age > 30 AND department = 'Sales'))"
    rule2 = "(salary > 50000)"
    rule3 = "(experience > 5)"
    
    combined_ast = combine_rules([rule1, rule2, rule3])
    
    return jsonify({
        "message": "Additional rules combined",
        "combined_ast": combined_ast.to_dict()  # Use to_dict() to convert to JSON serializable format
    }), 200

# Bonus: Invalid rule string test
@app.route('/test_invalid_rule', methods=['GET'])
def test_invalid_rule():
    invalid_rule = "((age > 30 AND ))"
    
    try:
        ast = create_rule(invalid_rule)
    except Exception as e:
        return jsonify({
            "message": "Invalid rule string",
            "error": str(e)
        }), 400

# Bonus: Attribute validation test
@app.route('/test_attribute_validation', methods=['POST'])
def test_attribute_validation():
    rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    ast = create_rule(rule_string)
    
    user_data = request.json.get('user_data', {
        "age": 35,
        "dept": "Sales",  # Invalid attribute "dept"
        "salary": 60000,
        "experience": 3
    })
    
    try:
        result = evaluate_rule(ast, user_data)
        return jsonify({
            "message": "Rule evaluated",
            "result": result
        }), 200
    except KeyError as e:
        return jsonify({
            "message": "Attribute validation failed",
            "error": f"Missing attribute: {e}"
        }), 400

# Bonus: Modify rule test
@app.route('/test_modify_rule', methods=['PUT'])
def test_modify_rule():
    rule_id = request.json['rule_id']
    new_rule_string = request.json['new_rule_string']
    
    modify_rule(rule_id, new_rule_string)
    return jsonify({"message": "Rule modified successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)

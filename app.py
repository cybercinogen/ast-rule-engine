from flask import Flask, request, jsonify
from rule_engine import create_rule, evaluate_rule
from combine_rules import combine_rules
from database import store_rule, modify_rule, retrieve_rule
from zeotap_functions import register_custom_functions

app = Flask(__name__)

# Register custom functions for the rule engine
register_custom_functions()

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data['rule_string']
    ast = create_rule(rule_string)
    store_rule(rule_string, ast)
    return jsonify({"message": "Rule created", "ast": ast.__dict__}), 201

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rule_strings = data['rules']
    combined_ast = combine_rules(rule_strings)
    return jsonify({"message": "Rules combined", "combined_ast": combined_ast.__dict__}), 200

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    rule_id = data['rule_id']
    user_data = data['user_data']
    ast = retrieve_rule(rule_id)
    result = evaluate_rule(ast, user_data)
    return jsonify({"result": result}), 200

@app.route('/modify_rule', methods=['PUT'])
def modify_rule_endpoint():
    data = request.json
    rule_id = data['rule_id']
    new_rule_string = data['new_rule_string']
    modify_rule(rule_id, new_rule_string)
    return jsonify({"message": "Rule modified"}), 200

if __name__ == "__main__":
    app.run(debug=True)

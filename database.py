import sqlite3
import json
from rule_engine import create_rule, rebuild_ast

conn = sqlite3.connect('rules.db')
cursor = conn.cursor()

# Function to create the 'rules' table if it doesn't exist
def create_rules_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL,
            ast_json TEXT NOT NULL
        )
    ''')
    conn.commit()

# Call the function to create the table
create_rules_table()

def store_rule(rule_string, ast):
    ast_json = json.dumps(ast, default=lambda o: o.__dict__)
    cursor.execute("INSERT INTO rules (rule_string, ast_json) VALUES (?, ?)", (rule_string, ast_json))
    conn.commit()

def retrieve_rule(rule_id):
    cursor.execute("SELECT ast_json FROM rules WHERE id = ?", (rule_id,))
    rule = cursor.fetchone()
    if rule:
        ast_dict = json.loads(rule[0])
        return rebuild_ast(ast_dict)
    return None

def modify_rule(rule_id, new_rule_string):
    new_ast = create_rule(new_rule_string)
    ast_json = json.dumps(new_ast, default=lambda o: o.__dict__)
    cursor.execute("UPDATE rules SET ast_json = ?, rule_string = ? WHERE id = ?", (ast_json, new_rule_string, rule_id))
    conn.commit()

def list_rules():
    cursor.execute("SELECT id, rule_string FROM rules")
    return cursor.fetchall()

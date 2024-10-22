AST Rule Engine for Zeotap
Overview
The AST Rule Engine for Zeotap is a three-tier application that allows users to define, store, modify, combine, and evaluate rules based on user attributes such as age, department, salary, and experience. The rules are represented using Abstract Syntax Trees (ASTs) to support complex conditional logic. The project includes a simple UI, backend APIs, and a database to manage and store the rules.

Features
Create Rules: Define rules using conditions like age, salary, and department.
Combine Rules: Combine two existing rules using AND or OR operators.
Evaluate Rules: Evaluate a rule against user-provided data to determine if the conditions are met.
Modify Rules: Update existing rules by providing their ID and new rule definition.
Delete Rules: Remove a rule by specifying its ID.
Reset Rules: Clear all stored rules from the database.
Display All Rules: View all stored rules along with their IDs.
Prerequisites
Python: Make sure you have Python 3.7+ installed. You can download Python here.
SQLite: Included with Python but ensure you have SQLite available if using external database management tools.
Virtual Environment (Optional): It's recommended to use a virtual environment for project dependencies.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/cybercinogen/ast-rule-engine.git
cd ast-rule-engine
Create a Virtual Environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Install Flask-CORS: If flask_cors is not included in the requirements.txt:

bash
Copy code
pip install flask-cors
Set Up the Database:

The database will be automatically initialized when you run the project for the first time, creating the rules.db file.
Project Structure
graphql
Copy code
├── app.py                  # Main application file for running the Flask server.
├── database.py             # Manages database operations for storing, modifying, and retrieving rules.
├── rule_engine.py          # Contains logic for creating and evaluating rules.
├── rule_parser.py          # Parses rule strings into ASTs.
├── combine_rules.py        # Combines multiple rules using logical operators.
├── ast_node.py             # Defines the Node class for representing AST nodes.
├── utils.py                # Helper functions for parsing conditions and validating attributes.
├── index.html              # Frontend for interacting with the rule engine.
├── requirements.txt        # Python dependencies for the project.
├── README.md               # Project documentation.
└── rules.db                # SQLite database file for storing rules.
Running the Project
Start the Flask Server:

bash
Copy code
python app.py
The server will start at http://127.0.0.1:5000/.
Access the UI:

Open a web browser and go to http://127.0.0.1:5000/ to access the rule engine interface.
Usage Instructions
Create a Rule
Enter a rule in the "Create Rule" input box (e.g., age > 30 AND department = 'Sales').
Click "Create Rule".
If successful, you will see a message confirming the rule creation. If the rule already exists, you'll be notified.
Combine Rules
Enter two rules in the "Combine Rules" input boxes (e.g., age > 30 and salary > 50000).
Click "Combine Rules".
The rules will be combined using an AND operator. If the combination is successful, a message will appear.
Evaluate a Rule
Enter a rule and user data (e.g., age > 30 AND department = 'Sales', along with age, department, salary, and experience).
Click "Evaluate Rule".
The result will display whether the provided user data satisfies the rule.
Modify a Rule
Enter the rule ID and new rule in the "Modify Rule" section.
Click "Modify Rule" to update the rule.
Delete a Rule
Enter the rule ID in the "Delete Rule" input box.
Click "Delete Rule" to remove the rule from the database.
Reset All Rules
Click "Reset Rules" to delete all rules from the database.
Show All Rules
Click "Show All Rules" to display all stored rules with their IDs.
Sample Rules
Rule 1: age > 30 AND department = 'Sales'
Rule 2: salary > 50000 OR experience > 5
Rule 3: (age < 25 AND department = 'Marketing') OR (age >= 35 AND department = 'Management')
Rule 4: age >= 25 AND age <= 40
Common Issues and Troubleshooting
ModuleNotFoundError for flask_cors:
Make sure to install Flask-CORS using pip install flask-cors.
500 Internal Server Error:
Check the console logs for detailed error messages.
Ensure that the rules follow the correct syntax before creating or combining.
Database Issues:
If the database does not initialize properly, delete rules.db and restart the server to create a fresh database.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.
License
This project is licensed under the MIT License.

Acknowledgments
Thanks to the Zeotap team for providing the assignment guidelines.
Special thanks to all the contributors and libraries that made this project possible.

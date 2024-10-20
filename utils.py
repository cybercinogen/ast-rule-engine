# utils.py

# Define allowed attributes globally
allowed_attributes = {"age", "salary", "experience", "department"}

def parse_condition(condition):
    """
    Parse a condition string (e.g., "age > 30") into attribute, operator, and value.
    """
    print(f"Parsing condition: {condition}")  # Debug output
    if '>' in condition:
        attribute, value = condition.split('>')
        if not attribute or not value:
            raise ValueError("Invalid comparison: Missing attribute or value")
        validate_attributes(attribute.strip())
        return attribute.strip(), '>', int(value.strip())

    elif '<' in condition:
        attribute, value = condition.split('<')
        if not attribute or not value:
            raise ValueError("Invalid comparison: Missing attribute or value")
        validate_attributes(attribute.strip())
        return attribute.strip(), '<', int(value.strip())

    elif '=' in condition:
        attribute, value = condition.split('=')
        if not attribute or not value:
            raise ValueError("Invalid comparison: Missing attribute or value")
        validate_attributes(attribute.strip())
        return attribute.strip(), '=', value.strip().replace("'", "")

    raise ValueError("Unsupported condition format")

def validate_attributes(attribute):
    """
    Validates that the attribute is part of the allowed attribute set.
    """
    print(f"Validating attribute: {attribute}")  # Debug output
    if attribute not in allowed_attributes:
        raise ValueError(f"Invalid attribute: {attribute}")

def compare(attribute_value, operator, condition_value):
    """
    Compare an attribute value against a condition value.
    """
    if operator == '>':
        return attribute_value > condition_value
    elif operator == '<':
        return attribute_value < condition_value
    elif operator == '=':
        return attribute_value == condition_value
    return False

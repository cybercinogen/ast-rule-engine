custom_functions = {}

def total_user_spend(data):
    """
    Custom function to calculate total user spend across campaigns.
    """
    return sum(data.get('campaign_spend', []))

def register_custom_functions():
    """
    Register custom functions that can be used in the rule engine.
    """
    custom_functions['total_user_spend'] = total_user_spend

def evaluate_custom_function(function_name, data):
    if function_name in custom_functions:
        return custom_functions[function_name](data)
    raise ValueError(f"Custom function '{function_name}' not found")

import traceback

def validate_code(code_str):
    try:
        exec(code_str, {})
        return True, None
    except Exception as e:
        return False, traceback.format_exc()
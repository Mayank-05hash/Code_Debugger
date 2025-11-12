def get_feedback(error_msg):
    if "SyntaxError" in error_msg:
        return "🔍 Check your syntax — maybe a missing colon or bracket?"
    elif "NameError" in error_msg:
        return "🧠 Looks like you're using a variable that hasn't been defined."
    elif "TypeError" in error_msg:
        return "⚙️ Type mismatch! Are you using the right data types?"
    else:
        return "🤔 Something’s off — read the error message carefully!"
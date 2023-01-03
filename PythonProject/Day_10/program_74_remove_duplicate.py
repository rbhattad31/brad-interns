import re

def remove_Duplicates_From_lines():
    regex = r'\b(\w+)(?:\W+\1\b)+'
    return re.sub(regex, r'\1', lines, flags=re.IGNORECASE)


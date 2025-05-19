def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        amount_of_spaces = (length - len(string)) // 2
        space = " " * amount_of_spaces
        return f"{space}{string}{space}"
    
        
print(format_string("abaa", 15))
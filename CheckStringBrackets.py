def check_string_brackets(input_string):
    if input_string.count('(') == input_string.count(')') and input_string[0] != ')' or input_string[-1] != '(':
        return 'YES'
    else:
        return 'NO'
    
print(check_string_brackets(input_string=input('Enter the bracketed sequence: ')))


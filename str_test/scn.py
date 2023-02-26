import re

with open('test.py', 'r') as f:
    source = f.read()

# Singleline strings
sngl_string = r'([\'\"])(.*?)(\1)'
sngl_strings = re.findall(sngl_string, source)

# Multiline strings
mult_string =  r'([\'\"]{3})(.*?)(\1)'
mult_strings = re.findall(mult_string, source, re.DOTALL)

printv = lambda v: {print("".join(i)) for i in v}
k = printv(sngl_strings)
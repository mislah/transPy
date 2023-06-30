from io import BytesIO
import tokenize

with open('test.py', 'r') as f:
   data = f.read()

tokens = tokenize.tokenize(BytesIO(data.encode('utf-8')).readline) 
source = list()
for token in tokens:
   if token.type == tokenize.STRING:
      token = token._replace(string="$")
   elif token.type == tokenize.COMMENT:
      token = token._replace(string="#")
   source.append(token)

transp = tokenize.untokenize(source).decode('utf-8')
print(transp)
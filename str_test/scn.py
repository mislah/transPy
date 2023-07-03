from io import BytesIO
import tokenize

with open('str_test/test.py', 'r') as f:
   source = f.read()

# map offsets of each line from (0,0)
pos = 0
offset = dict()
for i, x in enumerate(source.splitlines(keepends=True)):
   offset[i+1] = pos
   pos += len(x)

# find position of strings
strings = list()
tokens = tokenize.tokenize(BytesIO(source.encode('utf-8')).readline) 
for token in tokens:
   if token.type == tokenize.STRING or token.type == tokenize.COMMENT:
      start = offset[token.start[0]] + token.start[1]
      end = offset[token.end[0]] + token.end[1]
      strings.append((start, end))

# separate source into tokenstreams and strings
lines = []
for start, end in strings[::-1]:
   lines.append({'type': 'tstream', 'val': source[end:]})
   lines.append({'type': 'sstream', 'val': source[start:end]})
   source = source[:start]
lines.append({'type': 'tstream', 'val': source})
lines.reverse()

for i in lines:
   print(i)
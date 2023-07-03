import json
import _lexer
lib = json.load(open('_tokens.json', encoding = 'utf8'))

def parse(path_in, path_out):
    tokens = _lexer.lex(path_in)
    with open(path_out, 'w', encoding = 'utf8') as outf: 
        for i in tokens:
            if i['type'] == 'tstream':
                for j in lib:
                    i['val'] = i['val'].replace(j, lib[j])
            outf.write(i['val'])     
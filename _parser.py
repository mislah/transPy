import json
lib = json.load(open('_tokens.json', encoding = 'utf8'))

def parse(path_in, path_out):
    with open(path_in, encoding = 'utf8') as inf:
        with open(path_out, 'w', encoding = 'utf8') as outf: 
            for i in inf:
                for j in lib:
                    i = i.replace(j, lib[j])
                outf.write(i)     
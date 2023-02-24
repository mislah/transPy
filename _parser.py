import _tokens

def parse(path_in, path_out):
    with open(path_in, encoding = 'utf8') as inf:
        with open(path_out, 'w', encoding = 'utf8') as outf: 
            for i in inf:
                for j in _tokens.lib:
                    i = i.replace(j,_tokens.lib[j])
                outf.write(i)     
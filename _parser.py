lib = {
    'പറയൂ': 'print',
    'ആണേൽ': 'if',
    'അല്ലേൽ': 'elif',
    'അതല്ലേൽ': 'else',
    'ഇനിമുതൽ': 'def',
    'കൊണ്ടോയിക്കോ': 'return',
    'ആവാത്തെവരെ': 'while',
    'പരിശോധിക്കൂ': 'assert',
    'അല്ല': 'not',
    'സത്യം': 'True',
    'തെറ്റ്': 'False',
    'നിർത്തൂ': 'break',
    'ചോദിക്കൂ': 'input',
    'പൂർണ്ണസംഖ്യ': 'int',
}


def parse(path_in, path_out):
    with open(path_in, encoding='utf8') as inf:
        with open(path_out, 'w', encoding='utf8') as outf:
            for i in inf:
                for j in lib:
                    i = i.replace(j, lib[j])
                outf.write(i)


parse('test.ty', 'out.py')

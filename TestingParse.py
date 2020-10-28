import random

def sign_num(a, b):
    n = random.randint(a, b)
    if random.random() < 0.5:
        return '(-{})'.format(n)
    else:
        return str(n)

def num(a, b):
    return str(random.randint(a,b))

def add(a, b, parens=False):
    n1 = num(a, b)
    n2 = num(a, b)
    if parens:
        return '({} + {})'.format(n1, n2)
    else:
        return '{} + {}'.format(n1, n2)

def sign_add(a, b, parens=False):
    n1 = sign_num(a, b)
    n2 = sign_num(a, b)
    if parens:
        return '({} + {})'.format(n1, n2)
    else:
        return '{} + {}'.format(n1, n2)

dico = {'NUM': num, 'SIGNNUM': sign_num, 'ADD': add, 'SIGN_ADD': sign_add}

def fill_in(txt):
    argv = txt.strip().split()
    return dico[argv[0]](int(argv[1]), int(argv[2]))

def parse(txt):
    if '[' not in txt:
        return txt
    else:
        i = txt.index('[')
        j = txt.index(']')
        return txt[:i] + fill_in(txt[i+1:j])  + parse(txt[j+1:])

#  use database approach here.
assignments = ['[ADD 3 8]', '([ADD 4 9])\cdot [NUM 2 8]', '[SIGNNUM 3 19] ( + [ADD -3  6])']
for a in assignments:
    print(parse(a))
    
    

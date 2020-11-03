import random

class RandomHandler:
    def __init__(self):
        self.rs =''
        self.ri =0
    
    def fixrand(self, a,b):
        self.ri= random.randint(a,b)
        self.rs=str(self.ri)
        return ''
    
    def multrand(self, a,b):
        x=random.randint(a,b)
        return str(x*self.ri)
    
    def recallr(self, a,b):
        return self.rs
        
    
    #a,b left in bc the parser needs it.
    def sign(self,a,b):
        if random.random()<0.5:
            return '+'
        else:
            return '-'
    
    def sign_num(self,a, b):
        n = random.randint(a, b)
        if random.random() < 0.5:
            return '(-{})'.format(n)
        else:
            return str(n)

    def num(self,a, b):
        return str(random.randint(a,b))

    def add(self,a, b, parens=False):
        n1 = self.num(a, b)
        n2 = self.num(a, b)
        if parens:
            return '({} + {})'.format(n1, n2)
        else:
            return '{} + {}'.format(n1, n2)

    def sign_add(self,a, b, parens=False):
        n1 = self.sign_num(a, b)
        n2 = self.sign_num(a, b)
        if parens:
            return '({} + {})'.format(n1, n2)
        else:
            return '{} + {}'.format(n1, n2)

    dico = {'FIXRAND': fixrand, 'MULTRAND' : multrand, 'RECALLR' : recallr, 'SIGN' : sign, 'NUM': num, 'SIGNNUM': sign_num, 'ADD': add, 'SIGN_ADD': sign_add}

    def fill_in(self,txt):
        argv = txt.strip().split()
        return self.dico[argv[0]](self,int(argv[1]), int(argv[2]))

    def parse(self,txt):
        if '[' not in txt:
            return txt
        else:
            i = txt.index('[')
            j = txt.index(']')
            return txt[:i] + self.fill_in(txt[i+1:j])  + self.parse(txt[j+1:])

#================TESTING========================
#rh = RandomHandler()
#a=rh.parse('(4[SIGN 1 2]5*x)((-5)-9*x)')
#print(a)

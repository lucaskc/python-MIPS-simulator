"""
class Olar:
	i = None
	def __init__(self):
		self.i = 5 
	@property
	def f(self):
		return "hello world"	

a = Olar()
print(a.f())
print(a.i)
"""

class Instruction(object):
    def __init__(self, **input):
        self.result = None
        
        self.source1RegValue = None 
        self.source2RegValue = None
        self.values = {
                       'op': None,
                       'dest': None,
                       's1': None,
                       's2': None,
                       'immed': None,
                       'target': None
        }
        self.controls = {'aluop'   : None,
                         'regRead' : None,
                         'regWrite': None,
                         'readMem' : None,
                         'writeMem': None, }

        for key in input:
            if key in self.values.keys():
                self.values[key] = input[key]
            else:
                self.controls[key] = input[key]
    
    def __str__(self):
        str = "%s\t%s %s %s %s %s" % (self.values['op'],
                                  self.values['dest'] if self.values['dest'] else "",
                                  self.values['s1'] if self.values['s1'] else "",
                                  self.values['s2'] if self.values['s2'] else "",
                                  self.values['immed'] if self.values['immed'] else "",
                                  self.values['target'] if self.values['target'] else "")
        return str
    
    def __repr__(self):
        return repr(self.values)
        
class Nop(Instruction):
    pass
#nop singleton
Nop = Nop()

class InstructionParser(object):
    def __init__(self):
        self.instructionSet = {
            'rtype': ['add', 'sub', 'and', 'or'],
            'itype': ['bne', 'lw', 'sw']
        }    

    def parseFile(self, filename):
        with open(filename) as f:
            data = list(filter((lambda x: x != '\n'), f.readlines()))
            
            instructions = [self.parse(a.replace(',',' ')) for a in data]
            return instructions

    def parse(self, s):
        s = s.split()
        
        instr = s[0]
        
        if instr in self.instructionSet['rtype']:
            return self.createRTypeInstruction(s)
        elif instr in self.instructionSet['itype']:
            return self.createITypeInstruction(s)    
        else:
            raise ParseError("Invalid parse instruction")

    #TODO should be figuring out controls dynamically based on the op
    def createRTypeInstruction(self, s):
        return Instruction(op=s[0], dest=s[1], s1=s[2], s2=s[3], regRead=1, regWrite=1, aluop=1)

    def createITypeInstruction(self, s):
        memread = s[0] == "lw" 
        memwrite = s[0] == "sw"
        if (memread or memwrite):
            import re 
            regex = re.compile("(\d+)\((\$r\d+)\)")
            match = regex.match(s[2])
            
            immedval = match.group(1) 
            sval = match.group(2)
            if s[0] == "lw" :
                return Instruction(op=s[0], dest = s[1], s1=sval, immed = immedval, regRead = 1,regWrite = 1, aluop=1,  readMem = 1)
            else :
                return Instruction(op=s[0],  s1 = s[1], s2=sval,immed = immedval, regRead = 1, aluop=1, writeMem = 1)

        if (s[0] == 'bne'):
            return Instruction(op=s[0], s1=s[1] , s2= s[2], immed = s[3], regRead = 1, aluop = 1)

        return Instruction(op=s[0], dest=s[1], s1=s[2], immed=s[3], regRead=1, regWrite=1, aluop=1)


class ParseError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
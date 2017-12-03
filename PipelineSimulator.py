from Instruction import *
import collections 

class PipelineSimulator(object): 
    operations = {'add' : '+', 'addi' : '+', 'sub' : '-', 'subi' : '-', 
                  'and' : '&', 'andi' : '&', 'or'  : '|', 'ori'  : '|'} 
                  
    def __init__(self,instrCollection):
        self.instrCount = 0
        self.cycles = 0
        self.hazardList = []
        self.__done = False
        self.branched = False
        self.stall = False
        
        #self.pipeline is a list<PipelineStage>
        #with the mapping of:
        #   0 = Fetch
        #   1 = Write Back
        #   2 = Read
        #   3 = Execute 
        #   4 = Data Access
        self.pipeline = [None for x in range(0,5)]

        self.pipeline[0] = FetchStage(Nop, None, self)
        self.pipeline[1] = WriteStage(Nop, None, self)
        self.pipeline[2] = ReadStage(Nop, None, self)
        self.pipeline[3] = ExecStage(Nop, None, self)
        self.pipeline[4] = DataStage(Nop, None, self)

        # array of DebugINfo objects, will store all the information of the simulation
        self.simulationInfo = []
        
        # ex: {'$r0' : 0, '$r1' : 0 ... '$r31' : 0 }
        self.registers = dict([("$r%s" % x, 0) for x in range(32)]) 
        
        # set up the instruction memory construct, a list index starting at 0
        # and continuing to 0xffc
        self.instructionMemory = dict([(x*4, 0) for x in range(int(0xffc/4))])

        # set up the data memory construct, a list index starting at 0
        # and continuing to 0x4000
        self.dataMemory = dict([(x*4, 0) for x in range(int(0x4000/4))])

        # programCounter to state where in the instruction collection
        # we are. to find correct spot in instruction memory add 0x100  
        self.programCounter = 0x1000

        # the list of instruction objects passed into the simulator,
        # most likely created by parsing text 
        self.instrCollection = instrCollection
       
        # populate main memory with our text of the instructions
        # starting at 0x100
        y=0
        for instr in self.instrCollection:
           self.instructionMemory[0x1000 + y] = instr
           y += 4
    
    def step(self):
        self.cycles +=1
        cycleInfo = DebugInfo(self.cycles)
        #shift the instructions to the next logical place
        #technically we do the Fetch instruction here, which is why 
        #FetchStage.advance() does nothing

        #MUST KEEP THIS ORDER
        self.pipeline[1] = WriteStage(self.pipeline[4].instr, self.pipeline[4].pipeline, self)
        if self.stall :
            self.pipeline[4] = DataStage(Nop, self.pipeline[3].pipeline, self)
            self.stall = False
        else :
            self.pipeline[4] = DataStage(self.pipeline[3].instr, self.pipeline[3].pipeline, self)
            self.pipeline[3] = ExecStage(self.pipeline[2].instr, self.pipeline[2].pipeline, self)
            self.pipeline[2] = ReadStage(self.pipeline[0].instr, self.pipeline[0].pipeline, self)
            self.pipeline[0] = FetchStage(None, cycleInfo, self)
         
        #call advance on each instruction in the pipeline
        for pi in self.pipeline:
                pi.advance()


        print(cycleInfo.pipelineRegs['ID/EX']['PC'])


        for key, value in self.registers.items():
            cycleInfo.mainRegs[key] = self.registers[key]

        #now that everything is done, remove the register from
        # the hazard list
        if (self.pipeline[1].instr.controls['regWrite']) :
            self.hazardList.pop(0)
        
        self.simulationInfo.append(cycleInfo)

        self.checkDone()

        #if we stalled our branched we didn't want to load a new
        # so keep the program counter where it is
        if self.stall or self.branched:
            self.programCounter -= 4 
            self.branched = False
    
    def checkDone(self):
        """ Check if we are done and set __done variable """
        self.__done = True
        for pi in self.pipeline:
            if pi.instr is not Nop:
                self.__done = False
    
    def run(self):
        """ Run the simulator, call step until we are done """
        while not self.__done:
            self.step()
            self.debug()
        for value in self.simulationInfo:
            print(value.pipelineRegs['IF/ID']['IR'])
            print(value.pipelineRegs['ID/EX']['IR'])
            print(value.pipelineRegs['EX/MEM']['IR'])
            print(value.pipelineRegs['MEM/WB']['IR'])
            print()
    
    def getForwardVal(self, regName):
        """ Forward the proper value based on the given register name
            If the value is not ready, return "GAH" 
        """
        if (self.pipeline[4] is not Nop 
                and self.pipeline[4].instr.result is not None
                and self.pipeline[4].instr.values['dest'] == regName) :
                    return self.pipeline[4].instr.result
        elif (self.pipeline[1] is not Nop
                and self.pipeline[1].instr.values['dest'] == regName ):
                    return self.pipeline[1].instr.result
        else :#this value used to be False, but python treats False and 0 the same
            return "GAH" 

    ### DEBUGGING INFORMATION PRINTING ### 
    def debug(self):
        print ("######################## debug ###########################")
        self.printStageCollection() 
        self.printRegFile()
        print ("\n<ProgramCounter>", self.programCounter)
        self.printPipeline()   
        print ("<CPI> : " , float(self.cycles) / float(self.instrCount) )
        print ("<Hazard List> : " , self.hazardList)

    def printPipeline(self):
        print ("\n<Pipeline>")
        print (repr(self.pipeline[0])) 
        print (repr(self.pipeline[2])) 
        print (repr(self.pipeline[3])) 
        print (repr(self.pipeline[4])) 
        print (repr(self.pipeline[1])) 

    def printRegFile(self):
        #"""
        print ("\n<Register File>")
        for k,v in sorted(list(self.registers.items())):
            if len(k) != 3:
                print (k, " : " , v, end=' ')
            else :
                print ("\n",k, " : ", v, end=' ')
                
    def printStageCollection(self):
        print ("<Instruction Collection>")
        for index, item in sorted(list(self.instructionMemory.items())):
            if item != 0:
                print (index, ": ", str(item))

class PipelineStage(object):
    def __init__(self, instruction, pipelineRegs, simulator):
        self.instr = instruction
        self.pipeline = pipelineRegs
        self.simulator = simulator
        
    def advance(self):
        pass
    
    def __repr__(self):
        return str(self) + ':\t' + str(self.instr)
    
class FetchStage(PipelineStage):
    def advance(self):
        """ 
        Fetch the next instruction according to simulator program counter
        """
        if self.simulator.programCounter < (len(self.simulator.instrCollection) * 4 + 0x1000):
            self.simulator.instrCount += 1
            self.instr = self.simulator.instructionMemory[self.simulator.programCounter]
        else:
            self.instr = Nop
        self.simulator.programCounter += 4

        if (self.pipeline is not None):
            self.pipeline.pipelineRegs['IF/ID']['IR'] = str(self.instr)[:]
            self.pipeline.pipelineRegs['IF/ID']['PC'] = self.simulator.programCounter
         
    def __str__(self):
        return 'Fetch Stage\t'
    
class ReadStage(PipelineStage):
    def advance(self):
        """
        Read the necessary registers from the registers file
        used in this instruction 
        """
        immed = 0
        areg = 0
        breg = 0
        if(self.instr.controls['regRead']):
            self.instr.source1RegValue = self.simulator.registers[self.instr.values['s1']]
            areg = self.instr.source1RegValue

            if (self.instr.values['immed'] and
                #these instructions require special treatment
                 not( self.instr.values['op'] == 'bne' or self.instr.values['op'] == 'beq' 
                     or self.instr.values['op'] =='lw' or self.instr.values['op'] =='sw')): 
                #check to see if it is a hex value
                if "0x" in self.instr.values['immed']:
                    self.instr.source2RegValue = int(self.instr.values['immed'],16)
                else :
                    self.instr.source2RegValue = int(self.instr.values['immed'])
                immed = self.instr.source2RegValue
                
            elif self.instr.values['s2']:
                self.instr.source2RegValue = self.simulator.registers[self.instr.values['s2']]
                breg = self.instr.source2RegValue
                    
        if self.instr.values['op'] == 'j':
            # Set the program counter to the raw target address
            if "0x" in self.instr.values['target']:
                    targetval = int(self.instr.values['target'], 16)
            else :
                    targetval = int(self.instr.values['target'])
            self.simulator.programCounter = targetval
            # Set the other instructions currently in the pipeline to a Nop
            self.simulator.pipeline[0] = FetchStage(Nop, self)

        if (self.pipeline is not None):
            self.pipeline.pipelineRegs['ID/EX']['IR'] = str(self.pipeline.pipelineRegs['IF/ID']['IR'])[:]
            self.pipeline.pipelineRegs['ID/EX']['PC'] = self.pipeline.pipelineRegs['IF/ID']['PC']
            self.pipeline.pipelineRegs['ID/EX']['IMM'] = immed
            self.pipeline.pipelineRegs['ID/EX']['A'] = areg
            self.pipeline.pipelineRegs['ID/EX']['B'] = breg

    def __str__(self):
        return 'Read from Register'
    
class ExecStage(PipelineStage):
    def advance(self):
        """
        Execute the instruction according to its mapping of 
        assembly operation to Python operation
        """
        
        ALUResult = 0
        if self.instr is not Nop and self.instr.controls['aluop']:
            #if we have a hazard in either s1 or s2, 
            # grab the value from the other instructions
            # in the pipeline
            if self.instr.values['s1'] in self.simulator.hazardList :
                forwardVal = self.simulator.getForwardVal(self.instr.values['s1'])
                if forwardVal != "GAH":
                    self.instr.source1RegValue = forwardVal
                else :
                    self.simulator.stall = True
                    return
            if self.instr.values['s2'] in self.simulator.hazardList :
                forwardVal = self.simulator.getForwardVal(self.instr.values['s2'])
                if forwardVal != "GAH" :
                    self.instr.source2RegValue = forwardVal
                else :
                    self.simulator.stall = True
                    return
            
            #append the destination register to the hazard list 
            if self.instr.controls['regWrite'] :
                self.simulator.hazardList.append(self.instr.values['dest'])    

            #calculate the offset of the lw and sw instructions
            if  self.instr.values['op'] == 'lw':
                self.instr.source1RegValue = self.instr.source1RegValue + int(self.instr.values['immed'])
                ALUResult = self.instr.source1RegValue
            elif  self.instr.values['op'] == 'sw':
                self.instr.source2RegValue = self.instr.source2RegValue + int(self.instr.values['immed'])
                ALUResult = self.instr.source2RegValue

            elif self.instr.values['op'] == 'jr':
                self.simulator.programCounter = self.instr.source1RegValue
                # Set the other instructions currently in the pipeline to a Nop
                self.simulator.pipeline[0] = FetchStage(Nop, self)
                self.simulator.pipeline[2] = ReadStage(Nop, self)
            elif self.instr.values['op'] == 'bne':
                if self.instr.source1RegValue != self.instr.source2RegValue:
                    # Set the program counter to the target address 
                    # subtract 8 to account for 2 instructions we have loaded into fetch and read
                    self.simulator.programCounter = self.simulator.programCounter + (int(self.instr.values['immed']) * 4) - 8
                    ALUResult = self.simulator.programCounter
                    # Set the other instructions currently in the pipeline to Nops
                    self.simulator.pipeline[0] = FetchStage(Nop, None, self)
                    self.simulator.pipeline[2] = ReadStage(Nop, None, self)
                    self.simulator.branched = True
            elif self.instr.values['op'] == 'beq':
                if self.instr.source1RegValue == self.instr.source2RegValue:
                    # Set the program counter to the target address
                    self.simulator.programCounter = self.simulator.programCounter + (int(self.instr.values['immed']) * 4) - 8
                    ALUResult = self.simulator.programCounter
                    # Set the other instructions currently in the pipeline to Nops
                    self.simulator.pipeline[0] = FetchStage(Nop, None, self)
                    self.simulator.pipeline[2] = ReadStage(Nop, None, self)
                    self.simulator.branched = True
            else :         
                if (self.instr.values['op'] == 'slt'):
                    val = 1 if self.instr.source1RegValue < self.instr.source2RegValue else 0
                    self.instr.result = val
                elif (self.instr.values['op'] == 'nor'):
                    self.instr.result = ~(self.instr.source1RegValue | self.instr.source2RegValue)
                else:
                    self.instr.result = eval("%d %s %d" % 
                                                        (self.instr.source1RegValue,
                                                        self.simulator.operations[self.instr.values['op']],
                                                        self.instr.source2RegValue))
                ALUResult = self.instr.result

        if (self.pipeline is not None):
            self.pipeline.pipelineRegs['EX/MEM']['IR'] = str(self.pipeline.pipelineRegs['ID/EX']['IR'])[:]
            self.pipeline.pipelineRegs['EX/MEM']['ALUOUT'] = ALUResult
            self.pipeline.pipelineRegs['EX/MEM']['COND'] = self.simulator.branched
            self.pipeline.pipelineRegs['EX/MEM']['B'] = self.pipeline.pipelineRegs['ID/EX']['B']
                
    def __str__(self):
        return 'Execute Stage\t'
    
class DataStage(PipelineStage):
    def advance(self):
        """
        If we have to write to main memory, write it first
        and then read from main memory second
        """
 
        if self.instr.controls['writeMem']:
            self.simulator.dataMemory[self.instr.source2RegValue] = self.instr.source1RegValue
        elif self.instr.controls['readMem']:
            self.instr.result = self.simulator.dataMemory[self.instr.source1RegValue]

        if (self.pipeline is not None):
            self.pipeline.pipelineRegs['MEM/WB']['IR'] = str(self.pipeline.pipelineRegs['EX/MEM']['IR'])[:]
            self.pipeline.pipelineRegs['MEM/WB']['ALUOUT'] = self.pipeline.pipelineRegs['EX/MEM']['ALUOUT']
            self.pipeline.pipelineRegs['MEM/WB']['LMD'] = self.instr.result

    def __str__(self):
        return 'Main Memory'
    
class WriteStage(PipelineStage):
    def advance(self):
        """
        Write to the register file
        """
        if self.instr.controls['regWrite']:
            if self.instr.values['dest'] == '$r0':
                #Edit: don't raise exception just ignore it
                #raise Exception('Cannot assign to register $r0')    
                pass
            elif self.instr.values['dest']:
                self.simulator.registers[self.instr.values['dest']] = self.instr.result
                
    def __str__(self):
        return 'Write to Register'

class DebugInfo:
    def __init__(self, cycle):
        self.cycle = cycle
        
        self.mainRegs = {}

        self.pipelineRegs = {}
        self.pipelineRegs['IF/ID'] = {}
        self.pipelineRegs['IF/ID']['IR'] = ''
        self.pipelineRegs['IF/ID']['PC'] = 0

        self.pipelineRegs['ID/EX'] = {}
        self.pipelineRegs['ID/EX']['A'] = 0
        self.pipelineRegs['ID/EX']['B'] = 0
        self.pipelineRegs['ID/EX']['PC'] = 0
        self.pipelineRegs['ID/EX']['IR'] = ''
        self.pipelineRegs['ID/EX']['IMM'] = 0

        self.pipelineRegs['EX/MEM'] = {}
        self.pipelineRegs['EX/MEM']['IR'] = ''
        self.pipelineRegs['EX/MEM']['ALUOUT'] = 0
        self.pipelineRegs['EX/MEM']['COND'] = False
        self.pipelineRegs['EX/MEM']['B'] = 0

        self.pipelineRegs['MEM/WB'] = {}
        self.pipelineRegs['MEM/WB']['IR'] = ''
        self.pipelineRegs['MEM/WB']['ALUOUT'] = 0
        self.pipelineRegs['MEM/WB']['LMD'] = 0
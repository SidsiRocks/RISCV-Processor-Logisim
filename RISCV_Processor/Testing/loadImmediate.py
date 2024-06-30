from simpleAssembler import *
#check for load immediate
print(romHeaderTxt())
printInstructionArr(arrPseudoInstrucHex(["li",{"rd":1,"Imm":0xfffffff5}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":1,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["beq",{"rs1":0,"rs2":0,"Imm":0}]))

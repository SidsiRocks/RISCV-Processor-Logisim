from simpleAssembler import *
#simple fibonacci code example
print(romHeaderTxt())
print(buildInstrucOnlyInstrucHex(["addi",{"rd":1,"rs1":0,"Imm":1}])) #Begn
print(buildInstrucOnlyInstrucHex(["addi",{"rd":2,"rs1":0,"Imm":1}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":3,"rs1":0,"Imm":10}]))
print(buildInstrucOnlyInstrucHex(["beq",{"rs1":3,"rs2":0,"Imm":12}])) #LoopStr
print(buildInstrucOnlyInstrucHex(["addi",{"rd":3,"rs1":3,"Imm":-1}]))
print(buildInstrucOnlyInstrucHex(["add",{"rd":4,"rs1":1,"rs2":2}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":1,"rs1":2,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":2,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["beq",{"rs1":0,"rs2":0,"Imm":-10}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":1,"Imm":0}]))#Exit
print(buildInstrucOnlyInstrucHex(["beq",{"rs1":0,"rs2":0,"Imm":0}]))

from simpleAssembler import *
#sanity check code
print(romHeaderTxt())
print(buildInstrucOnlyInstrucHex(["addi",{"rd":1,"rs1":0,"Imm":1023}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":2,"rs1":1,"Imm":105}]))
print(buildInstrucOnlyInstrucHex(["add",{"rd":3,"rs1":2,"rs2":1}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":1,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":2,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":3,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["beq",{"rs1":0,"rs2":0,"Imm":0}]))

from simpleAssembler import *
print(romHeaderTxt())
print(buildInstrucOnlyInstrucHex(["addi",{"rd":1,"rs1":0,"Imm":10}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":2,"rs1":0,"Imm":123}]))
print(buildInstrucOnlyInstrucHex(["sw",{"rs2":2,"rs1":1,"Imm":6}]))
print(buildInstrucOnlyInstrucHex(["lw",{"rd":3,"rs1":1,"Imm":6}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":3,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["beq",{"rs1":0,"rs2":0,"Imm":0}]))

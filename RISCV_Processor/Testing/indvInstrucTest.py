from simpleAssembler import *
print(romHeaderTxt())
print(buildInstrucOnlyInstrucHex(["addi",{"rd":1,"rs1":0,"Imm":1023}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":2,"rs1":1,"Imm":105}]))
print(buildInstrucOnlyInstrucHex(["add",{"rd":3,"rs1":2,"rs2":1}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":1,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":2,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":3,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["xor",{"rd":4,"rs1":1,"rs2":2}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["xori",{"rd":4,"rs1":1,"Imm":1128}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["or",{"rd":4,"rs1":1,"rs2":2}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["ori",{"rd":4,"rs1":1,"Imm":1128}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["and",{"rd":4,"rs1":1,"rs2":2}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["andi",{"rd":4,"rs1":1,"Imm":1128}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":5,"rs1":0,"Imm":2}]))
print(buildInstrucOnlyInstrucHex(["sll",{"rd":4,"rs1":1,"rs2":5}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["slli",{"rd":4,"rs1":1,"Imm":2}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["srl",{"rd":4,"rs1":1,"rs2":5}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["srli",{"rd":4,"rs1":1,"Imm":2}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":4,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["slt",{"rd":5,"rs1":1,"rs2":2}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":5,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["slt",{"rd":5,"rs1":2,"rs2":1}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":5,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["slti",{"rd":5,"rs1":1,"Imm":1128}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":5,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["slti",{"rd":5,"rs1":2,"Imm":1023}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":5,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["beq",{"rs1":0,"rs2":0,"Imm":0}]))

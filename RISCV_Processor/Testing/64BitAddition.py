#64 bit addition code
from simpleAssembler import *
print(romHeaderTxt())
printInstructionArr(arrPseudoInstrucHex(["li",{"rd":1,"Imm":0x0f9fff0e}]))
printInstructionArr(arrPseudoInstrucHex(["li",{"rd":2,"Imm":0xffffffff}]))
printInstructionArr(arrPseudoInstrucHex(["li",{"rd":3,"Imm":0x09c2dca0}]))
printInstructionArr(arrPseudoInstrucHex(["li",{"rd":4,"Imm":0x5f01faca}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":5,"rs1":0,"Imm":0}])) #set carryin to zero
print(buildInstrucOnlyInstrucHex(["add",{"rd":6,"rs1":2,"rs2":4}]))
print(buildInstrucOnlyInstrucHex(["sltu",{"rd":7,"rs1":6,"rs2":2}]))
print(buildInstrucOnlyInstrucHex(["add",{"rd":6,"rs1":6,"rs2":5}]))
print(buildInstrucOnlyInstrucHex(["sltu",{"rd":9,"rs1":6,"rs2":5}]))
print(buildInstrucOnlyInstrucHex(["or",{"rd":7,"rs1":7,"rs2":9}]))
print(buildInstrucOnlyInstrucHex(["add",{"rd":5,"rs1":0,"rs2":7}])) #first 32 bit addition complete making cout to cin
print(buildInstrucOnlyInstrucHex(["add",{"rd":8,"rs1":1,"rs2":3}]))
print(buildInstrucOnlyInstrucHex(["sltu",{"rd":7,"rs1":8,"rs2":1}]))
print(buildInstrucOnlyInstrucHex(["add",{"rd":8,"rs1":8,"rs2":5}]))
print(buildInstrucOnlyInstrucHex(["sltu",{"rd":9,"rs1":8,"rs2":5}]))
print(buildInstrucOnlyInstrucHex(["or",{"rd":7,"rs1":7,"rs2":9}]))
print(buildInstrucOnlyInstrucHex(["add",{"rd":5,"rs1":0,"rs2":7}])) #second 32 bit addition complete making cout to cin
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":6,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["addi",{"rd":0,"rs1":8,"Imm":0}]))
print(buildInstrucOnlyInstrucHex(["beq" ,{"rs1":0,"rs2":0,"Imm":0}]))
opcodeDict = {
    "R": 0b0110011,
    "I": 0b0010011,
    "Load": 0b0000011,
    "Store": 0b0100011,
    "Branch": 0b1100011
}
funct3 = {
    "add": 0x0,"addi": 0x0,
    "sub": 0x0,
    "xor": 0x4,"xori": 0x4,
    "or": 0x6,"ori": 0x6,
    "and": 0x7,"andi": 0x7,
    "sll": 0x1,"slli": 0x1,
    "srl": 0x5,"srli": 0x5,
    "sra": 0x5 ,"srai": 0x5,
    "slt": 0x2,"slti": 0x2,
    "sltu": 0x3,"sltiu": 0x3,

    "lw": 0x2,
    "sw": 0x2,
    "bge" : 0x0
}
aluOpDict = {
    "add": 0,"addi": 0,
    "sub": 12,"subi": 12,
    "xor": 4,"xori": 4,
    "or": 6,"ori": 6,
    "and": 7,"andi": 7,
    "sll": 1,"slli": 1,
    "srl": 5,"srli": 5,
    "slt": 2,"slti": 2,
    "sltu": 3,"stliu": 3,
    "lw":0,
    "sw":0,
    "beq":12
}
funct7 = {
    "add": 0x00,
    "sub": 0x20,
    "xor": 0x00,
    "or": 0x00,
    "and": 0x00,
    "sll": 0x00,
    "srl": 0x00,
    "sra": 0x00,
    "slt": 0x00,
    "sltu": 0x00
}
instrucTypeDict = {
    "add": "R",
    "sub": "R",
    "xor": "R",
    "or": "R",
    "and": "R",
    "sll": "R",
    "srl": "R",
    "sra": "R" ,
    "slt": "R",
    "sltu": "R",
    "addi": "I",
    "xori": "I",
    "ori": "I",
    "andi": "I",
    "slli": "I",
    "srli": "I",
    "srai": "I",
    "slti": "I",
    "sltiu": "I",
    "lw": "Load",
    "sw":"Store",
    "bge" : "Branch" 
}
def signExtend(immTxt,instrucType):
    topBit = immTxt[0]
    immExtendTxt = topBit*20 + immTxt
    if instrucType == "Branch":
        immExtendTxt = immExtendTxt[:-1] + '0'
    return immExtendTxt
def handleRtype(arr):
    argDict = arr[1]
    rs1 = '{0:05b}'.format(argDict["rs1"])
    rs2 = '{0:05b}'.format(argDict["rs2"])
    rd = '{0:05b}'.format(argDict["rd"])
    opcodeTxt = '{0:07b}'.format(opcodeDict["R"])
    funct3Txt = '{0:03b}'.format(funct3[arr[0]])
    funct7Txt = '{0:07b}'.format(funct7[arr[0]])
    instrucTxt = opcodeTxt + rd + funct3Txt + rs1 + rs2 + funct7Txt
    aluTxt = '{0:04b}'.format(aluOpDict[arr[0]])
    #           ["Instr"   ,"Wr","R1","R2","branch","RAMwrite","regSrc","Imm" ,"ALUop","write","ALUSrc"]
    resultArr = [instrucTxt,rd  ,rs1 ,rs2 ,"0"     ,"0"       ,"0"     ,'x'*32,aluTxt ,"1"    ,"0"] 
    return resultArr
def handleItype(arr):
    argDict = arr[1]
    rs1 = '{0:05b}'.format(argDict["rs1"])
    rd = '{0:05b}'.format(argDict["rd"])
    opcodeTxt = '{0:07b}'.format(opcodeDict["I"])
    funct3Txt = '{0:03b}'.format(funct3[arr[0]])
    ImmTxt = '{0:12b}'.format(argDict["Imm"])
    immExtendTxt = signExtend(ImmTxt,"I")
    instrucTxt = opcodeTxt + rd + funct3Txt + rs1 + ImmTxt
    aluTxt = '{0:04b}'.format(aluOpDict[arr[0]])
    #           ["Instr"   ,"Wr","R1","R2" ,"branch","RAMwrite","regSrc","Imm"       ,"ALUop","write","ALUSrc"]
    resultArr = [instrucTxt,rd  ,rs1 ,'x'*5,"0"     ,"0"       ,"0"     ,immExtendTxt,aluTxt ,"1"    ,"1"]
    return resultArr
def handleLoadType(arr):
    argDict = arr[1]
    opcodeTxt = '{0:07b}'.format(opcodeDict["Load"])
    rs1 = '{0:05b}'.format(argDict["rs1"])
    rd  = '{0:05b}'.format(argDict["rd"])
    funct3Txt = '{0:03b}'.format(funct3[arr[0]])
    ImmTxt    = '{0:12b}'.format(argDict["Imm"])
    immExtendTxt = signExtend(ImmTxt,"Load")
    instrucTxt   = opcodeTxt + rd + funct3Txt + rs1 + ImmTxt
    aluTxt = '{0:04b}'.format(aluOpDict[arr[0]])
    #           ["Instr"   ,"Wr","R1","R2" ,"branch","RAMwrite","regSrc","Imm"       ,"ALUop","write","ALUSrc"]
    resultArr = [instrucTxt,rd  ,rs1 ,'x'*5,"0"     ,"0"       ,"1"     ,immExtendTxt,aluTxt ,"1"    ,"1"]
    return resultArr
def handleStoreType(arr):
    argDict = arr[1]
    opcodeTxt = "{0:07b}".format(opcodeDict["Store"])
    rs1 = '{0:05b}'.format(argDict["rs1"])
    rs2 = '{0:05b}'.format(argDict["rs2"])
    funct3Txt = '{0:03b}'.format(funct3[arr[0]])
    ImmTxt    = '{0:12b}'.format(argDict["Imm"])
    ImmLowerTxt = ImmTxt[0:4]
    ImmUpperTxt = ImmTxt[5:11]
    immExtendTxt = signExtend(ImmTxt,"Store")
    instrucTxt = opcodeTxt + ImmLowerTxt + funct3Txt + rs1 + rs2 + ImmUpperTxt
    aluTxt = '{0:04b}'.format(aluOpDict[arr[0]])
    #           ["Instr"   ,"Wr" ,"R1","R2" ,"branch","RAMwrite","regSrc","Imm"        ,"ALUop","write","ALUSrc"]
    resultArr = [instrucTxt,'x'*5,rs1 ,rs2  ,"0"     ,"1"       ,"1"     , immExtendTxt,aluTxt ,"0"    ,"1"     ]
    return resultArr
def handleBranchType(arr):
    argDict = arr[1]
    opcodeDict = "{0:07b}".format(opcodeDict["Branch"])
    rs1 = "{0:05b}".format(argDict["rs1"])
    rs2 = "{0:05b}".format(argDict["rs2"])
    funct3Txt = '{0:03b}'.format(funct3[arr[0]])
    ImmTxt = '{0:03b}'.format(argDict["Imm"])
    ImmLowerTxt  = ImmTxt[10] + ImmTxt[0:3]
    ImmUpperTxt  = ImmTxt[4:9] + ImmTxt[11]
    immExtendTxt = signExtend(ImmTxt,"Branch")  
    instrucTxt   = opcodeTxt + ImmLowerTxt + funct3Txt + rs1 + rs2 + ImmUpperTxt
    #           ["Instr"   ,"Wr" ,"R1","R2" ,"branch","RAMwrite","regSrc","Imm"        ,"ALUop","write","ALUSrc"]
    resultArr = [instrucTxt,'x'*5,rs1 ,rs2  ,"1"     ,"0"       ,"0"     ,immExtendTxt ,aluTxt ,"0"    ,"0"     ]
    return resultArr
instucFunc = {
    "R": handleRtype,
    "I": handleItype,
    "Load": handleLoadType,
    "Store": handleStoreType,
    "Branch": handleBranchType
}
def buildInstruc(arr):
    typeInstruc = instrucTypeDict[arr[0]]
    resultArr = instucFunc[typeInstruc](arr)
    return resultArr
def arr2Txt(arr):
    result = ""
    for elm in arr:
        result = result + elm + " "
    return result
def headerTxt():
    return "Instr[32] Wr[5] R1[5] R2[5] branch RAMwrite regSrc Imm[32] ALUOp[4] write ALUSrc"
resultArr = buildInstruc(["add",{"rs1":4,"rs2":2,"rd":3}])
resultTxt = arr2Txt(resultArr)

print(headerTxt())
print(arr2Txt(buildInstruc(["add",{"rs1":4,"rs2":2,"rd":3}])))
print(arr2Txt(buildInstruc(["add",{"rs1":2,"rs2":0,"rd":0}])))
print(arr2Txt(buildInstruc(["add",{"rs1":1,"rs2":0,"rd":3}])))

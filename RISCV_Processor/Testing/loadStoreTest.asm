addi x1,x0,10
addi x2,x0,123
sw x2,x1(6) #store value 123(7b in hexadecimal) at address 16 (adress has to be aligned with 4 byte multiples)
lw x3,x1(6) #load value at memory adress 16 into register 3
addi x0,x3,0 #print the value stored at register 3(expected 7b)
beq x0,x0,0
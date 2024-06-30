li x1,0000 1111 1001 1111 1111 1111 0000 1110
#     0    f    9    f    f    f    0    e



li x2,1111 1111 1111 1111 1111 1111 1111 1111
#     f    f    f    f    f    f    f    f



li x3,0000 1001 1100 0010 1101 1100 1010 0000
#     0    9    c    2    d    c    a    0



li x4,0101 1111 0000 0001 1111 1010 1100 1010
#     5    f    0    1    f    a    c    a



addi x5,x0,0
add  x6,x2,x4
sltu x7,x6,x2
add  x6,x6,x5
sltu x9,x6,x5
or   x7,x7,x9
add  x5,x0,x7 #first 32 bit addition complete
add  x8,x1,x3
sltu x7,x8,x1
add  x8,x8,x5
sltu x9,x8,x5
or   x7,x7,x9 
add  x5,x0,x7 #second 32 bit additon complete and carry out moved to carry in 
addi x0,x6,0 #printing lower 32 bit 1593965257 with cur example 5F01FAC9 in hexadecimal
addi x0,x8,0 #printing higher 32 bit 425909167 with cur example 1962DBAF in hexadecimal
beq x0,x0,0

addi x1,x0,1 #Begn
addi x2,x0,1
addi x3,x0,10
beq  x3,x0,12 #LoopStart
addi x3,x3,-1
add  x4,x1,x2
addi x1,x2,0
addi x2,x4,0
beq x0,x0,-10 #going back to loop start 
addi x0,x1,0 #printing out 89 in decimal 59 in hexadecimal
beq  x0,x0,0
"""
    Assuming that fib[0] = 1 fib[1] = 1
"""
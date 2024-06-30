addi x1,x0,12 #n is 12
addi x2,x0,0  #running sum is 0
beq  x1,x0,8 #LoopStr
add  x2,x2,x1 
addi x1,x1,-1
beq  x0,x0,-6
addi x0,x2,0 #Exit for given x1 x2=78 (4e in hexadecimal)
beq  x0,x0,0
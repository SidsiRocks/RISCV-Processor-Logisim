addi x1,x0,1023 #tested addi and add
addi x2,x1,105 #1128 here
add x3,x2,x1 #2151 here
addi x0,x1,0 #printing 1023 in decimal 3ff in hexadecimal
addi x0,x2,0 #printing 1128 in decimal 468 in hexadecimal
addi x0,x3,0 #printing 2151 in decimal 867 in hexadecimal
xor x4,x1,x2 #1943 here
addi x0,x4,0 #printing 1943 in decimal 797 in hexadecimal
xori x4,x1,1128 #should be same as before
addi x0,x4,0 #printing 1943 in decimal 797 in hexadecimal
or x4,x1,x2 #2047 here
addi x0,x4,0 #printing 2047 in decimal 7ff in hexadecimal
ori x4,x1,1128 #should be same as before 
addi x0,x4,0 #printing 2047 in decimal 7ff in hexadecimal
and x4,x1,x2 #104 here 
addi x0,x4,0 #printing 104 in decimal 68 in hexadecimal
andi x4,x1,1128 #should be same as before 
addi x0,x4,0 #printing 104 in decimal 68 in hexadecimal
addi x5,x0,2
sll x4,x1,x5 #4092 here 
addi x0,x4,0 #printing 4092 in decimal ffc in hexadecimal
slli x4,x1,2 #should be same as before 
addi x0,x4,0 #printing 4092 in decimal ffc in hexadecimal
srl x4,x1,x5 #255 here 
addi x0,x4,0 #printing 255 in decimal ff in hexadecimal
srli x4,x1,2 #should be same as before
addi x0,x4,0 #printing 255 in decimal ff in hexadecimal
slt x5,x1,x2 #1023 < 1128 hence x5 = 1
addi x0,x5,0 #printing 1 
slt x5,x2,x1 #1128 >= 1023 hence x5 = 0
addi x0,x5,0 #printing 0
slti x5,x1,1128 #1023 < 1128 hence x5 = 1
addi x0,x5,0 #printing 1
slti x5,x2,1023 #1128 >= 1023 hence x5 = 0
addi x0,x5,0 #printing 0
beq x0,x0,0 #to ensure program doesnt start reading invalid instructions 

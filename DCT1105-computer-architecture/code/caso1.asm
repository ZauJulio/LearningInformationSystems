.text 				
.globl main 		
main:
lw $s6, vector
lw $s1,0($s6)
lw $s2,4($s6)
add $s3,$s1,$s2
sw $s3,12($s6)
lw $s4,8($s6)
add $s5,$s1,$s4
sw $s5,16($s6)

.data 
vector: .word 5 15 25
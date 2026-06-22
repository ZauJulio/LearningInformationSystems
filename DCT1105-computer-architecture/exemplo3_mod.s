.text 				
.globl main 		
main:
	lw $s0,g
	lw $s1,h
	lw $s2,i
	lw $s3,k
	lw $s4,f 
	move $a0,$s0		# Carrega no reg. temporario $a0 com 5 (g=5)
	move $a1,$s1		# Carrega no reg. temporario $a1 com 4 (h=4)
	move $a2,$s2		# Carrega no reg. temporario $a2 com 2 (i=1)
	move $a3,$s3		# Carrega no reg. temporario $a3 com 2 (j=3)
        jal leaf                # Chama o procedimento leaf
        move $s4,$v0		# salva resultado na memória
	
	# impressao da saída no console
	la	$a0, msg0	# Carrega endereco da msg0 em $a0
	jal printStr		
	la	$a0, lf		# Carrega endereco da lf em $a0
	jal printStr		
	la	$a0, msg1	# Carrega endereco da msg1 em $a0
	jal printStr		
	la	$a0, open	# Carrega endereco de '(' em $a0
	jal printStr
	move	$a0, $s0	# Carrega inteiro g ($s0) em $a0 para impressao
	jal printInt
	la	$a0, plus	# Carrega endereco de '+' em $a0
	jal printStr
	move	$a0, $s1	# Carrega inteiro h ($s1) em $a0 para impressao
	jal printInt
	la	$a0, close	# Carrega endereco de ')' em $a0
	jal printStr 
	la	$a0, minus	# Carrega endereco de '-' em $a0
	jal printStr
	la	$a0, open	# Carrega endereco de '(' em $a0
	jal printStr
	move	$a0, $s2	# Carrega inteiro i ($s2) em $a0 para impressao
	jal printInt
	la	$a0, plus	# Carrega endereco de '+' em $a0
	jal printStr
	move	$a0, $s3	# Carrega inteiro k ($s3) em $a0 para impressao
	jal printInt
	la	$a0, close	# Carrega endereco de ')' em $a0
	jal printStr
	la	$a0, lf		# Carrega endereco da lf em $a0
	jal printStr
 	la	$a0, msg1	# Carrega endereco da msg1 em $a0
	jal printStr
	move	$a0, $s4	# Carrega inteiro f ($s4) em $a0 para impressao
	jal printInt
	la	$a0, lf		# Carrega endereco da lf em $a0
	jal printStr

	# Sai do programa
	li	$v0,10		# codigo do exit = 10
	syscall
.end main

.globl leaf
.ent leaf
leaf:
	addi $sp, $sp, -4      # ajusta a pilha para criar espaco para 1 itens
	sw   $s0, 0($sp)       # salva $s0 para uso posterior do chamador
        add  $t0, $a0, $a1     # $t0 = g + h   
        add  $t1, $a2, $a3     # $t1 = i + j
        sub  $s0, $t0, $t1     # f = $t0 - $t1 
        add  $v0, $s0, $zero   # retorna f
        lw   $s0, 0($sp)       # restaura $s0 para o valor anterior a chamada 
        addi $sp, $sp, 4       # ajusta a pilha deletando 1 itens
        jr  $ra                # salta de volta para o chamador
.end leaf

.globl printStr
.ent printStr
printStr:
	# Imprime uma string cujo endereço esta carregado e $a0
	li	$v0, 4		# Codigo do syscall print_string = 4
	syscall
	jr $ra
.end printStr

.globl printInt
.ent printInt
printInt:
	# Imprime o valor de um inteiro colocado em $a0
	li	$v0, 1		# Codigo do syscall print_int = 1
	syscall
	jr $ra 
.end printInt

.data
g:	.word 5
h:	.word 4
i:	.word 1
k:	.word 2
	.align 2
f:	.space 4
msg0:	.asciiz "f = (g + h) - (i + k)"
msg1:	.asciiz "f = "
plus:   .asciiz " + "
minus:	.asciiz " - "
open: 	.asciiz "("
close:	.asciiz ")"
lf:     .asciiz "\n"

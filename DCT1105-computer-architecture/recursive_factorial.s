.text 				
.globl main 
.ent main
main:
    lw $a0,n        # Carrega o reg. $a0 com o valor n (n=3)
    jal fact        # Chama o procedimento leaf
    sw $v0,answer   # Armazena o valor retornado na memoria 
    move $s0,$v0    # Move o valor de $v0 para $s0
    li $v0,1        # Codigo de syscall print_int = 1
    move $a0, $s0   # Carrega inteiro para impressao em $a0
    syscall         # Imprime 
    li $v0,10       # codigo do exit = 10
    syscall         # Sai do programa
.end main

.globl fact 
.ent fact
fact:
    addi $sp, $sp, -8     # Ajusta a pilha para armazenar 2 itens (push)
    sw   $a0, 0($sp)      # Salva o argumento n
    sw   $ra, 4($sp)      # Salva o endereço de retorno
    slti $t0, $a0, 1      # Testa se $a0 < 1 (n < 1)
    beq  $t0, $zero, gCase   # se n>=1, salta para gCase (caso geral)
    addi $v0, $zero, 1    # retorna 1 (caso base)
    addi $sp, $sp, 8      # retira os 2 itens da pilha
    jr   $ra 

gCase:
    addi $a0, $a0, -1     # n>=1: argumento será n-1, para a chamada recusiva de fact
    jal  fact             # chama fact(n-1)
    lw   $ra, 4($sp)      # restaura o endereço de retorno
    lw   $a0, 0($sp)      # retorna do jal, restaura argumento n
    addi $sp, $sp, 8      # ajusta o apontador de pilha para deletar 2 itens
    mul  $v0, $a0, $v0    # retorna n * fact( n - 1)
    jr   $ra              # retorna ao chamador
.end fact

.data

n:      .word 3
answer: .word 0


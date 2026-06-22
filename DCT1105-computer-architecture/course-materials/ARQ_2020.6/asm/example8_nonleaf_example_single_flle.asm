#Example 8 - Chamada ao procedimento fatorial recursivo  

.data
  _result: .word 0
  _prompt: .asciiz "Digite um número para calcular seu fatorial: "
  _answer: .asciiz "Fatorial = "

.text
.globl _main
  _main:
     jal read_input
     move $a0, $v0
     jal fact
     sw $v0, _result
     move $a0,$v0
     jal print
     #Termina o programa
     li $v0, 10
     syscall 
  L1:
     addi $a0, $a0, -1     # n>=1: argumento será n-1, para a chamada recusiva de fact
     jal  fact             # chama fact(n-1)
     lw   $a0, 0($sp)      # retorna do jal, restaura argumento n 
     lw   $ra, 4($sp)      # restaura o endereço de retorno
     addi $sp, $sp, 8      # ajusta o apontador de pilha para deletar 2 itens
     mul  $v0, $a0, $v0    # retorna n * fact( n - 1)
     jr   $ra              # retorna ao chamador
  fact:
     addi $sp, $sp, -8     # Ajusta a pilha para armazenar 2 itens
     sw   $ra, 4($sp)      # Salva o endereço de retorno
     sw   $a0, 0($sp)      # Salva o argumento n
     slti $t0, $a0, 1      # Testa se n($a0) < 1
     beq  $t0, $zero, L1   # se n>=1, salta para L1
     addi $v0, $zero, 1    # retorna 1
     addi $sp, $sp, 8      # retira os 2 itens da pilha
     jr   $ra              # retorna ao chamador

  read_input:
     li $v0, 4   #print string
     la $a0, _prompt  #$a0 = endereço da string terminada em \0 (.asciiz)
     syscall
     li $v0, 5   #read integer (coloca em $v0)
     syscall
     jr $ra

  print:
     li $v0, 4   #print string
     la $a0, _answer #$a0 = endereço da string terminada em \0 (.asciiz)
     syscall
     li $v0, 1   # print integer
     lw $a0, _result #$a0 = inteiro para imprimir
     syscall
     jr $ra
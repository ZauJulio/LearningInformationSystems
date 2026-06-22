#Example 7 - Chamada ao procedimento f = (g + h) – (i + j);  

.data
  _f: .word 0
  _g: .word 5
  _h: .word 4
  _i: .word 2
  _j: .word 1 

.text
.globl _main
  _main:
  #Carrega os valores das variáveis nos registradores MEM -> REG
  sw $gp, 0($sp) #apenas para mostrar onde está o ponteiro $sp
  lw $a0, _g
  lw $a1, _h
  lw $a2, _i
  lw $a3, _j
  #Exemplo de registradores em uso pelo chamador
  li $t1, 12
  li $t0, 15
  li $s0, 20
  #Realiza o calculo chamando o procedimento
  jal leaf_example
  sw $zero, 0($sp) #apenas para mostrar que $sp foi restaurado corretamente
  #Retorna o valor do resultado para a memória REG -> MEM
  move $s0,$v0
  sw $s0, _f
  #Termina o programa
  li $v0, 10
  syscall        

.globl leaf_example
  leaf_example:
  addi $sp, $sp, -12     # ajusta a pilha para criar espaço para 3 itens
  sw   $t1, 8($sp)       # salva $t1 para uso posterior do chamador
  sw   $t0, 4($sp)       # salva $t0 para uso posterior do chamador
  sw   $s0, 0($sp)       # salva $s0 para uso posterior do chamador 
  add  $t0, $a0, $a1     # $t0 = g + h   
  add  $t1, $a2, $a3     # $t1 = i + j
  sub  $s0, $t0, $t1     # f = $t0 - $t1 
  add  $v0, $s0, $zero   # retorna f
  lw   $s0, 0($sp)       # restaura $s0 para o valor anterior a chamada 
  lw   $t0, 4($sp)       # restaura $t0 para o valor anterior a chamada
  lw   $t1, 8($sp)       # restaura $t1 para o valor anterior a chamada             
  addi $sp, $sp, 12      # ajusta a pilha deletando 3 itens
  jr  $ra                # salta de volta para o chamador  

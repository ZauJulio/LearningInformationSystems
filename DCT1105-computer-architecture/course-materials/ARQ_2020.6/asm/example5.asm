#Example 5 - Laços de repetição
#exemplo while (save[i]  ==  k) i += 1;

 
.data
  _i: .word 0
  _k: .word 2
  _save: .word 2, 2, 3, 4, 5      # Array de words (inteiros) 
.text
.globl _main
  _main:
  #Carrega os valores das variáveis nos registradores MEM -> REG
  lw $s3, _i
  lw $s5, _k
  la $s6, _save
  #Realiza o calculo
  Loop:
  sll $t1,$s3,2    # $t1=i*4 (offset)
  add $t1,$t1,$s6  # $t1=$s6+$t1 (endereço)
  lw $t0,0($t1)    # $t0=save[i]
  bne $t0,$s5,Exit # Se save[i]!=k => Exit
  addi $s3,$s3,1   # $s3=$s3+1 (incremento)
  j Loop           # Salta de volta para Loop
  Exit:            # Termina o laco
  #Termina o programa
  li $v0, 10
  syscall        
          
        

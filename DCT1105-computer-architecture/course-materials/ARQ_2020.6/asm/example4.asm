#Example 4 - Condicionais (Tomada de ecisão)
#exemplo if (i == j) f = g + h; else f = g – h;
 
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
  lw $s1, _g
  lw $s2, _h
  lw $s3, _i
  lw $s4, _j
  #Realiza o calculo
  bne $s3,$s4,Else  #se i!=j => Else
  add $s0,$s1,$s2   #f=g+h (se i!=j pula, se i==j executa) 
  j Exit            #salto incondicional para Exit
  Else:
  sub $s0,$s1,$s2   #se i!=j, f=g-h  
  Exit:
  #Retorna o valor do resultado para a memória REG -> MEM
  sw $s0, _f
  #Termina o programa
  li $v0, 10
  syscall        
          
        

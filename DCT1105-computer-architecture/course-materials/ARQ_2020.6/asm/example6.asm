#Example 6 - La�os de repeti��o
#exemplo for(i=0;i<5;i++){ a[i]+=5; }
 
.data
  _i: .word 0
  _a: .word 1, 2, 3, 4, 5      # Array de words (inteiros) 
.text
.globl _main
  _main:
  
  #Carrega os valores das vari�veis nos registradores MEM -> REG
  lw $s1, _i
  li $t0, 5
  la $s6, _a
  
  #Realiza o calculo
  loop:
  beq $s1, $t0, end  # se i==10 termina
  
  sll $t2, $s1, 2    # $t2=i*4 (offset)
  add $t2, $t2, $s6  # $t2=$s6+$t2 (endere�o
  lw $t3, 0($t2)     # $t3=a[i]
  
  addi $t3, $t3, 5   # #t3+=5 (inc. de a[i])
  
  sw $t3, 0($t2)     #
  
  addi $s1, $s1, 1   # i+=1 (inc. de i)
  
  j loop             # Salta pra o teste
  end:
  #Termina o programa
  li $v0, 10
  syscall        
          
        

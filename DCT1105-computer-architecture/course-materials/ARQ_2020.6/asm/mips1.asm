# Q2 2020_6
#Implementar:
# for(i=0;i<5;i++){
#    F[i] = A[B[i]] - 5 + i;
# }
#resultado esperado F = 9, 5, 1, 23, 69  
#Declare i inteiro e igual a zero
#Declare F inteiro com 5 posi��es e inicialize todas com 0
#Declare A inteiro com 5 posi��es e inicialize com 14 9 4 25 70
#Declare B inteiro com 5 posi��es e inicialize com 0 1 2 3 4
.data
   i: .word 0			# Variável de laço
   F: .word 0, 0, 0, 0, 0	# Array de words (inteiros)
   A: .word 14, 9, 4, 25, 70	# Array de words (inteiros)
   B: .word 0, 1, 2, 3, 4	# Array de words (inteiros)


.text

.globl _main
  _main:
  #Carrega os valores das vari�veis nos registradores MEM -> REG
  lw $s5, F	# Carregando o array F em $s5
  lw $s6, A	# Carregando o array A em $s6
  lw $s7, B	# Carregando o array B em $s7
  
  li $s0, 5	# Carregando o número de iterações do loop em $s0
  lw $s1, i	# Carregando o contador imediato iniciando em 0 em $s1
  
  #Realiza o calculo
  loop:
  beq $s1, $s1, end  # se i==10 termina

  add $t0, $s7, $s1	# Carregando o valor de B no index atual em $t0
  lb $t1, 0($t0)	# Salvando o valor em $t1
  
  add $t2, $s6, $t1	# Carregando o valor de B no index atual em $t2
  lb $t3, 0($t2)	# Salvando o valor em $t3
  
  addi $t3, $t3, -5	# Operação A[B[i]] - 5
  add $t3, $t3, $s1	# Agora somando com i
  
  sw $t4, 0($t3)	# Salvando a soma
  
  addi $s1, $s1, 1	# i+=1 (inc. de i)
  j loop		# Salta pra o teste
  end:
  
  #Termina o programa
  li $v0, 10
  syscall        
          
        

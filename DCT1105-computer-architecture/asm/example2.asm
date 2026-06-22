.data
  _i: .word 0
  _f: .word 1
  _g: .word 1
.text
.globl _main
  _main:
  lw $s1, _f
  lw $s2, _g
  lw $s3, _i
  #Realiza o calculo
  and $s3, $s1, $s2
  #Retorna o valor do resultado para a mem�ria REG -> MEM
  sw $s0, _f
  #Termina o programa
  li $v0, 10
  syscall        
          
        

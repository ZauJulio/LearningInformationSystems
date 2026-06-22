#Example 3 - Operações lógicas (sll, srl, and, andi, or, ori, nor)

.data
.text
.globl _main
  _main:
  #Carrega os valores imediatos nos REGISTRADORES
  li $s0, 0x00000009
  li $s1, 0x00003c00
  li $s2, 0x00000dc0
  #Realiza o calculo
  sll $t0, $s0, 4     #0x00000090
  srl $t1, $t0, 2     #0x00000024
  and $t2, $s1, $s2   #0x00000c00
  or  $t3, $s1, $s2   #0x000003dc0
  andi $t4, $s2, 255  #(255 16bits)0x00ff => 0x000000c0
  ori  $t5, $s2, 15   #(15 16bits)0x000f  => 0x00000dcf
  nor  $t6, $s1,$zero # not $s0 => 0xffffc3ff 
  #Termina o programa
  li $v0, 10
  syscall        
          
        

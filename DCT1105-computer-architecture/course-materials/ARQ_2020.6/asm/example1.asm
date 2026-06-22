#Example 1 - Declaração de variáveis e tipos de dados
# Declaração segue a forma: 
# label: .type valores 

#.data - Seção onde os dados armazenados em memória
#(RAM), de modo similar as variáveis em linguagens 
#de alto nível
.data
  # Tamanho dos tipos de dados
  _str0: .asciiz "FIM"
  #_byte: .byte 'b'                          # 1 byte
  #_halfword: .byte 'a'
  #00350061 0x10010000(+0) ou 0x10010000
  #especificamente 0x61 (ASCII) -> a (caractere)
  _halfword: .word 65536                       # 2 bytes
  #_halfword: .half 53 (alinha com a half word superior)
  #00350061 0x10010000(+2) ou 0x10010002
  #especificamente 0035, 0x35 -> 53 (decimal)
  _word: .word -3                            # 4 bytes
  #_word: .word 3
  #00000003 0x10010000(+4) ou 0x10010004
  _float: .float 3.5                        # 4 bytes
  #_float: .float 3.5 
  #40600000 0x10010000(+8) ou 0x10010008 
  #0100 0000 0110 0000 0000 0000 0000 0000
  #sinal = 0 (+)
  #expoente = 1000 0000 -> 128 - 127(excesso) = 1
  #mantissa = 110 0000 0000 0000 0000 0000
  #interpretação 1,11 x 2^1 = 11,1 (binário) -> 3,5 (decimal)
  _str1: .asciiz "Hello World\n"  # string terminada em null
  _num1: .word 42                 # Inteiro são words (32 bits)
  _arr1: .word 1, 2, 3, 4, 5      # Array de words (inteiros)
  _arr2: .byte 'a', 'b','c','d'   # Array de chars (1 byte cada)
  _buffer: .space 20              # Aloca espaço na RAM em bytes 
                                  #(mas sem atribuir zero)
                                  #alocou 5 palavras, 20/4 = 5
  _num2: .word 16                 # Mais um inteiro
  
  .align 2         # Alinhamento de memória dos dados, 
                   # o número indica o alinhamento de bytes
                   # em potências de 2. 
                   #(.align 2 representa alinhamento de
                   # palavra, pois 2^2 = 4 bytes)

#.text - Seção que contém instruções e a lógica do programa
.text

#.globl _main - Declara um label de instruções como
# global, tornando-o acessivel por outros arquivos
.globl _main
  _main:
  #imprime "Hello World"
  #service 4 (imprimir string guardada a partir do
  #endereço especificado em $a0)
  li $v0, 4 
  la $a0, _str1 #load address, carrega em $a0 o endereço de _str1
  syscall
  #termina o programa retornando o controle ao SO
  li $v0, 10 #sevice 10, pára ou termina o programa
  syscall


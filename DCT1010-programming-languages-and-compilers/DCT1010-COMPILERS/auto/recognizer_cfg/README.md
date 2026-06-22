# Reconhecedor de Expressões Aritméticas (CFG)

Desenvolva um reconhecedor de expressões aritméticas sem parentização, por exemplo: "((17 + 91) - (67 * (15 / 5)))". Considerando números inteiros não negativos e as operações de soma, subtração, multiplicação e divisão.

- (i) definir gramática regular

```md
1. Símbolos Terminais (Tokens):

Números inteiros não negativos
Operadores: +, -, *, /

2. Símbolos Não Terminais:

<expressao>: representa uma expressão aritmética.

3. Produções:

<expressao> ::= ( <expressao> <operador> <expressao> ) | <termo>
<termo> ::= <numero> <termo> | <numero>
<operador> ::= + | - | * | /
<numero>: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

-

<expressao>: Uma expressão é composta por parênteses seguido por uma expressão, um operador e outra expressão, ou um termo.
<termo>: Um termo é composto por um número inteiro não negativo seguido por um termo, ou um número.
<operator>: Representa um operador aritmético.
<numero>: Representa um número inteiro não negativo.
```

- (ii) descrever o autômato finito que reconhece a linguagem

1. Alfabeto:

Símbolos terminais da linguagem, que são números inteiros não negativos (0-9), operadores (+, -, *, /), parênteses (()), e o símbolo de fim de cadeia ($).

1. Conjunto de Estados:

Estados: q0, q1, q2, q3, q4, q5, q6, q7
Inicial: q0
Final: q7 ou, possivelmente, q1

1. Transições:

- **q0 -> q1** if next **isNumber**
- **q1 -> q1** if next **isNumber**
- **q1 -> q1** if next is "$"
- **q0 -> q2** if next is **(**
- **q2 -> q2** if next is **(**
- **q2 -> q3** if next **isNumber**
- **q3 -> q3** if next **isNumber**
- **q3 -> q4** if next *isOperator*
- **q4 -> q3** if next is **(**
- **q4 -> q5** if next **isNumber**
- **q5 -> q5** if next **isNumber**
- **q5 -> q6** if next is **)**
- **q6 -> q6** if next is **)**
- **q6 -> q4** if next *isOperator*
- **q6 -> q7** if next is "$"

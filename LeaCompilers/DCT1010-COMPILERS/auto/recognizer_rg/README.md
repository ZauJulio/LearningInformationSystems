# Reconhecedor de Expressões Aritméticas (RG)

Desenvolva um reconhecedor de expressões aritméticas sem parentização, por exemplo: "17 + 91 - 67 * 15 / 5". Considerando números inteiros não negativos e as operações de soma, subtração, multiplicação e divisão.

- (i) definir gramática regular

```md
1. Símbolos Terminais (Tokens):

Números inteiros não negativos
Operadores: +, -, *, /

2. Símbolos Não Terminais:

<expressao>: representa uma expressão aritmética.

3. Produções:

<expressao> ::= <expressao> <operador> <expressao> | <termo>
<termo> ::= <numero> <termo> | <numero>
<operador> ::= + | - | * | /
<numero>: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

-

<expressao>: Uma expressão é composta por um termo seguido opcionalmente por + ou - e outra expressão.
<termo>: Um termo é composto por um fator seguido opcionalmente por * ou / e outro termo.
<fator>: Um fator pode ser um número inteiro não negativo ou uma expressão entre parênteses.
<numero>: Representa um número inteiro não negativo.
```

- (ii) descrever o autômato finito que reconhece a linguagem

1. Alfabeto:

Símbolos terminais da linguagem, que são números inteiros não negativos (0-9), operadores (+, -, *, /) e o símbolo de fim de entrada EOF.

2. Conjunto de Estados:

Estados: q0 (inicial), q1, q2, q3.

3. Transições:

- **q0** -> **q1** if next **isNumber**
- **q1** -> **q1** if hasMoreThanOneDigit
- **q1** -> **q2** if next *isOperator*
- **q2** -> **q1** if next **isNumber**
- **q1** -> **q3** if next isEndOfInput (EOF)

# Avaliação 03 - Admnistração de Servidores de Rede

Aluno: Zaú Júlio Araújo Galvão

## Questão 2

a) O NAT é responsável por realizar as traduções de endereços IP privado para endereços IP públicos e vice-versa. Com essa técnica uma rede precisa somente de um endereço público, diminuindo o número de endereços alocados para a rede.

b) A notação CIDR tem a finalidade de realizaar o roteamento com menor disperdício de endereços alocados. Com uma máscara de tamanho variável, as redes podem solicitar intervalos de endereços menores que os oferecidos pelas classes de endereços, (A, B e C), diminuindo assim o disperdício de endereços reservados.

## Questão 3

a) Comprima ao máximo:

- i. 2001:0db8:0000:1200:0ef0:0000:0000:0003

  - 2001:db8:0:1200:ef0::3

- ii. 2001:0db8::ca5a:0000:2000

  - 2001:db8::ca5a:0:2000

- iii. 2001:0db8:face:b00c:0000:0000:0100:00ab

  - 2001:db8:face:b00c::100:ab

b) Descomprima ao máximo:

- i. 2001:db8:0:ca1::1:abcd

  - 2001:0db8:0000:ca1:0000:0000:0001:abcd

- ii. 2001:db8:4::2

  - 2001:0db8:0004:0000:0000:0000:0000:0002

- iii. 2001:db8:200::bdb:110

  - 2001:0db8:0200:0000:0000:0000:0bdb:0110

## Questão 4

a) Como funciona o processo de atribuição de IID no formato EUI-64?

```txt
IPv6: fe80::c6cc:5161:2e99:b9e4/64
MAC: CC-CD-23-5A-23-A1
```

- Inverter o pneultimo byte do MAC

  - -> CC-CD-23-5A-23-A1 -> CE-CD-23-5A-23-A1

- Adicionar 0xFFFE no meio do endereço

  - -> CE-CD-23-5A-23-A1 -> CE-CD-23-FF-FE-5A-23-A1

b) Como esse processo de automatizar a atribuição de IPs pode ser útil no funcionamento de um enlace local (link local) com prefixo FE80::/64.

A atribuição automatizada de endereços otimiza o processo de configuração de endereços IPv6 em uma rede, pois não é necessário configurar manualmente os endereços IPv6 em cada dispositivo da rede.

c) Pensando na questão de segurança, outra forma de atribuição é através da geração aleatória e de forma temporária. Que problema de segurança pode haver com a utilização do padrão EUI-64 para os usuários?

Como o padrão EUI-64 é baseado no endereço MAC do dispositivo, o endereço IPv6 pode ser facilmente descoberto por um atacante, o que pode comprometer a segurança da rede.

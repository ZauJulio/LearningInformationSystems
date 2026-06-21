# LearningInformationSystems

Repositório **unificado** de aprendizado da graduação em **Sistemas de Informação — UFRN**.

Consolida os repositórios da família `Lea*` e os projetos de aprendizado relacionados num
único lugar, **preservando o histórico de commits completo** de cada origem (autores e datas
originais). Cada pasta de topo corresponde a um repositório/projeto de origem e mantém
`git log` e `git blame` rastreáveis nativamente.

> Centralização feita via `git filter-repo --to-subdirectory-filter` + merges de histórias
> independentes — nenhum commit foi perdido. Veja [`MANIFEST.md`](./MANIFEST.md) para a
> proveniência de cada pasta.

## Índice

### Disciplinas (UFRN — BSI)
| Pasta | Disciplina |
|---|---|
| `LeaDataStructures` | Estrutura de Dados |
| `LeaPWEB` | Programação Web |
| `LeaIA` | Inteligência Artificial |
| `LeaOperationalSystems` | Sistemas Operacionais |
| `LeaATP_III_IA` | Tópicos Avançados em Programação III (IA) |
| `LeaSAD` | Sistemas de Apoio à Decisão (regressão linear) |
| `LeaDB2` | Banco de Dados II *(local, sem repo prévio)* |
| `LeaPOOII` | Programação Orientada a Objetos II *(local)* |
| `LeaCompilers` | Compiladores *(local)* |

### Estudos / temas
| Pasta | Tema |
|---|---|
| `LeaRust` *(privado)* | Estudos de Rust |
| `LeaPyQt` | Estudos de PyQt |
| `LeaLA` *(privado)* | Álgebra Linear |
| `LeaSec` *(privado)* | Segurança |
| `LeaSecClass` | Segurança — material de aula (cripto, rede, código seguro, esteganografia) *(local)* |
| `LeaCaesarCipher` | Cifra de César (Rust) *(local)* |
| `Learning` | Agregador de projetos de aprendizado |

### Extensões de IA / Machine Learning
| Pasta | Conteúdo |
|---|---|
| `TicTacToe` | Jogo da velha (IA) |
| `MLP_Sinc` | Aproximação da função sinc (MLPRegressor) |
| `VowelRecognition` | Reconhecimento de vogais (Sklearn) |
| `LogicGatesPerceptron` | Perceptron para portas lógicas |

## Rastreabilidade

- Histórico por pasta: `git log -- <Pasta>/`
- Autoria linha a linha: `git blame <Pasta>/<arquivo>`
- Origem de cada pasta e camadas de edição local: [`MANIFEST.md`](./MANIFEST.md)

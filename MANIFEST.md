# MANIFEST — Proveniência e rastreabilidade

Este repositório foi montado consolidando repositórios `Lea*` e projetos de aprendizado,
preservando todo o histórico de commits. Repositórios de origem **não foram apagados** —
permanecem intactos no GitHub para conferência.

## Como o histórico foi preservado

1. Cada repositório de origem foi clonado e reescrito com
   `git filter-repo --to-subdirectory-filter <Pasta>` (move todos os commits para dentro da
   subpasta, mantendo autor, data e mensagem originais).
2. Cada história foi integrada ao repositório unificado com
   `git merge --allow-unrelated-histories`.
3. Onde havia **cópia local divergente** (em `~/Desktop/UFRN_S/Lea/`), as edições/arquivos
   locais não versionados foram aplicados por cima como um commit `reconcile(...)`, de modo que
   tanto o histórico do GitHub quanto as edições locais ficam preservados.

Resultado: `git log -- <Pasta>/` e `git blame` funcionam por pasta. **110 commits originais**
preservados.

## Pastas com origem em repositório do GitHub

| Pasta | Repo de origem | Visibilidade origem | Commits orig. | Camada local |
|---|---|---|---:|---|
| `LeaSec` | ZauJulio/LeaSec | privado | 1 | — (local `experiments/` vazio) |
| `LeaRust` | ZauJulio/LeaRust | privado | 1 | — |
| `LeaLA` | ZauJulio/LeaLA | privado | 10 | — |
| `LeaPyQt` | ZauJulio/LeaPyQt | público | 2 | — |
| `LeaSAD` | ZauJulio/LeaSAD | público | 2 | — |
| `LeaOperationalSystems` | ZauJulio/LeaOperationalSystems | público | 2 | — (local `LeaSO` idêntico) |
| `LeaIA` | ZauJulio/LeaIA | público | 3 | ✅ `reconcile` (prolog, search, reinforcement, learning, Pipfile) |
| `LeaPWEB` | ZauJulio/LeaPWEB | público | 34 | ✅ `reconcile` (next.config.js + edições) |
| `LeaDataStructures` | ZauJulio/LeaDataStructures | público | 11 | — |
| `Learning` | ZauJulio/Learning | público | 12 | — |
| `TicTacToe` | ZauJulio/TicTacToe | público | 6 | — |
| `MLP_Sinc` | ZauJulio/MLP_Sinc | público | 4 | — |
| `VowelRecognition` | ZauJulio/VowelRecognition | público | 8 | — |
| `LogicGatesPerceptron` | ZauJulio/LogicGatesPerceptron | público | 8 | — |
| `LeaATP_III_IA` | ZauJulio/LeaATP_III_IA | público | 6 | ✅ `reconcile` (RegressorTestBase.ipynb + read.py) |
| `Sig-Library` | ZauJulio/Sig-Library (fork) | público | 49 | — (projeto em grupo; sem cópia local) |

> Nota: `LeaIA` referenciava `LogicGatesPerceptron`, `MLP_Sinc`, `TicTacToe` e
> `VowelRecognition` como submódulos (gitlinks vazios preservados em `.gitmodules`). O conteúdo
> real desses projetos está nas pastas de topo homônimas deste repositório.

## Submódulos (git submodule)

Projetos ainda em evolução são referenciados como submódulo (não vendorizados), mantendo o
histórico no repositório de origem.

| Pasta | Submódulo → | Branch |
|---|---|---|
| `Taskiano` | `git@github.com:ZauJulio/Taskiano.git` | `main` |

## Pastas locais sem repositório prévio no GitHub

Conteúdo que existia apenas em `~/Desktop/UFRN_S/Lea/` (sem histórico de versionamento anterior).
Adicionado como commit único de importação.

| Pasta (normalizada) | Origem local | Observação |
|---|---|---|
| `LeaDB2` | `Lea/LeaDB2` | Banco de Dados II (TypeScript) |
| `LeaPOOII` | `Lea/LeaPOOII` | Programação Orientada a Objetos II |
| `LeaCompilers` | `Lea/compilers` | Compiladores (DCT1010) |
| `LeaSecClass` | `Lea/class-security` | Material de aula de segurança |
| `LeaCaesarCipher` | `Lea/sec-caeser` | Cifra de César (Rust); `target/` de build excluído |

## Fora de escopo (não incluídos — permanecem como repos independentes)

`ZSOM`, `minisom-scikit-learn-contribution`, `dksom` (pesquisa em Self-Organizing Maps) —
mantidos separados a pedido.

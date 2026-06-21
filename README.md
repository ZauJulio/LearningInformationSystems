<div align="center">

# 🎓 Learning · Information Systems

**A unified archive of my undergraduate learning — Information Systems, UFRN.**

Every `Lea*` study repository and related learning project, consolidated into a single
place with **complete commit history preserved** — original authors, dates and messages intact.

</div>

---

## 📌 About

For years my coursework and study repositories lived scattered across dozens of small
repos. This repository brings them together so the history stays **traceable**: each
top-level folder maps to one source repository and keeps native `git log` and `git blame`.

History was preserved with `git filter-repo --to-subdirectory-filter` followed by merges of
independent histories — **no commit was lost**. Active, still-evolving projects are included
as **git submodules** instead of being vendored. See [`MANIFEST.md`](./MANIFEST.md) for the
full provenance of every folder.

```bash
# clone including submodules
git clone --recurse-submodules git@github.com:ZauJulio/LearningInformationSystems.git
```

## 🗂️ Contents

### Courses (UFRN — BSI)
| Folder | Course |
|---|---|
| [`LeaDataStructures`](./LeaDataStructures) | Data Structures |
| [`LeaPWEB`](./LeaPWEB) | Web Programming |
| [`LeaIA`](./LeaIA) | Artificial Intelligence |
| [`LeaOperationalSystems`](./LeaOperationalSystems) | Operating Systems |
| [`LeaATP_III_IA`](./LeaATP_III_IA) | Advanced Topics in Programming III (AI) |
| [`LeaSAD`](./LeaSAD) | Decision Support Systems (linear regression) |
| [`LeaDB2`](./LeaDB2) | Databases II *(local-only)* |
| [`LeaPOOII`](./LeaPOOII) | Object-Oriented Programming II *(local-only)* |
| [`LeaCompilers`](./LeaCompilers) | Compilers *(local-only)* |

### Studies & topics
| Folder | Topic |
|---|---|
| [`LeaRust`](./LeaRust) 🔒 | Rust |
| [`LeaPyQt`](./LeaPyQt) | PyQt |
| [`LeaLA`](./LeaLA) 🔒 | Linear Algebra |
| [`LeaSec`](./LeaSec) 🔒 | Security |
| [`LeaSecClass`](./LeaSecClass) | Security coursework — cryptology, networking, secure code, steganography *(local-only)* |
| [`LeaCaesarCipher`](./LeaCaesarCipher) | Caesar cipher (Rust) *(local-only)* |
| [`Learning`](./Learning) | Learning-projects aggregator |

### AI / Machine Learning
| Folder | Content |
|---|---|
| [`TicTacToe`](./TicTacToe) | Tic-tac-toe (AI) |
| [`MLP_Sinc`](./MLP_Sinc) | Sinc-function approximation (MLPRegressor) |
| [`VowelRecognition`](./VowelRecognition) | Vowel recognition (scikit-learn) |
| [`LogicGatesPerceptron`](./LogicGatesPerceptron) | Perceptron for logic gates |

### Projects
| Folder | Content |
|---|---|
| [`Sig-Library`](./Sig-Library) | Library-management system prototype (Programming course, DCT1106) |
| [`graphya`](./graphya) | Programming language for knowledge extraction |
| [`Taskiano`](./Taskiano) ↗️ | To-do application — **git submodule** → [`ZauJulio/Taskiano`](https://github.com/ZauJulio/Taskiano) |
| [`CutTheChase`](./CutTheChase) ↗️ | Event-map app — Web Programming course (DCT1109) — **git submodule** → [`ZauJulio/CutTheChase`](https://github.com/ZauJulio/CutTheChase) |

🔒 = sourced from a private repository · ↗️ = git submodule

## 🔎 Traceability

```bash
git log -- LeaPWEB/            # full original history of a folder
git blame LeaPWEB/src/...      # line-by-line authorship
git submodule update --init    # populate submodules (Taskiano)
```

Folder origins and local-edit layers are documented in [`MANIFEST.md`](./MANIFEST.md).

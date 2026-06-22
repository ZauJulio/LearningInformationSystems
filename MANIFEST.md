# MANIFEST — Provenance & Traceability

This repository consolidates undergraduate learning material (Information Systems, UFRN),
organized **by discipline** using the official course codes. Commit history of every source
repository was preserved. Source repositories were **not deleted** — they remain on GitHub.

## How content was integrated

- **Vendored with history** — each source repo was rewritten into its discipline folder with
  `git filter-repo --to-subdirectory-filter` and merged with `git merge --allow-unrelated-histories`.
  `git log -- <folder>/` and `git blame` work natively.
- **Submodules** — still-evolving projects are referenced as git submodules (not vendored).
- **Course materials** — slides/notes/assignments extracted from local course archives
  (`UFRN_S/01_Disciplinas`) into each discipline's `course-materials/`. **Exams are excluded.**
- **Local-only** — folders that never had a prior repository were imported as-is.

## Disciplines (folder → source)

| Folder (discipline) | Code | Source repo | History | Course materials |
|---|---|---|---|---|
| `DCT0008-data-structures` | DCT0008 | ZauJulio/LeaDataStructures | vendored | ✅ (+ YouTube lecture links) |
| `DCT1010-programming-languages-and-compilers` | DCT1010 | ZauJulio/LeaCompilers (local) + `graphya` | vendored | — |
| `DCT1106-programming` | DCT1106 | ZauJulio/Sig-Library (fork, group) | vendored | — |
| `DCT1108-object-oriented-programming-ii` | DCT1108 | local-only | imported | — |
| `DCT1109-web-programming` | DCT1109 | ZauJulio/LeaPWEB (+ `CutTheChase` submodule) | vendored | — |
| `DCT1304-linear-algebra` | DCT1304 | ZauJulio/LeaLA 🔒 | vendored | ✅ |
| `DCT1401-artificial-intelligence` | DCT1401 | ZauJulio/LeaIA (+ AI extensions) | vendored | ✅ |
| `DCT2101-operating-systems` | DCT2101 | ZauJulio/LeaOperationalSystems | vendored | ✅ |
| `DCT2202-database-design-and-administration` | DCT2202 | local-only | imported | ✅ |
| `DCT2403-decision-support-systems` | DCT2403 | ZauJulio/LeaSAD | vendored | — |
| `DCT2602-machine-learning` | DCT2602 | ZauJulio/Learning | vendored | ✅ |
| `DCT4302-special-topics-in-information-security-i` | DCT4302 | ZauJulio/LeaSec 🔒 + local material | vendored + imported | — |
| `DCT4403-advanced-topics-in-programming-iii` | DCT4403 | ZauJulio/LeaATP_III_IA | vendored | ✅ |
| `DCT0435-ethics` | DCT0435 | — | — | ✅ |
| `DCT1105-computer-architecture` | DCT1105 | — | — | ✅ |
| `DCT1305-probability-and-statistics` | DCT1305 | — | — | ✅ |
| `DCT2102-computer-networks` | DCT2102 | — | — | ✅ |
| `DCT2201-databases` | DCT2201 | — | — | ✅ |
| `DCT2301-software-engineering-i` | DCT2301 | — | — | ✅ |
| `DCT2304-software-testing` | DCT2304 | — | — | ✅ |
| `DCT3202-accounting-and-costs` | DCT3202 | — | — | ✅ |
| `DCT4101-network-server-administration` | DCT4101 | — | — | ✅ |
| `BSI3103-it-entrepreneurship` | BSI3103 | — | — | ✅ |

## AI sub-projects (under `DCT1401-artificial-intelligence/`)

Originally "extensions of the AI repository", vendored with history:
`TicTacToe`, `MLP_Sinc`, `VowelRecognition`, `LogicGatesPerceptron`
(each from the homonymous `ZauJulio/*` repo).

## Submodules

| Path | Submodule → | Branch |
|---|---|---|
| `DCT1109-web-programming/CutTheChase` | `ZauJulio/CutTheChase` | `master` |
| `extra-studies/taskiano` | `ZauJulio/Taskiano` | `main` |
| `thesis/features-analyzer` | `ZauJulio/FeaturesAnalyzer` | `main` |

## Thesis (`thesis/`)

Undergraduate final project (TCC, 2024.2). `document/` holds the thesis text and defense
slides; `features-analyzer/` is the thesis software as a submodule.

## Extra studies (`extra-studies/`)

Non-discipline personal studies: `pyqt`, `rust`, and the `taskiano` submodule.

## Notes

- 🔒 = sourced from a private repository.
- Video lectures (e.g. Data Structures) are **linked** to the professor's YouTube channel
  instead of stored — see `DCT0008-data-structures/VIDEO_LECTURES.md`.
- Exams, virtual-environments and build artifacts are excluded (`.gitignore`).

## Out of scope

`ZSOM`, `minisom-scikit-learn-contribution`, `dksom` (Self-Organizing Maps research) — kept
as separate repositories by request.

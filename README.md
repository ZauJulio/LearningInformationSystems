<div align="center">

# 🎓 Learning · Information Systems

**A unified archive of my undergraduate learning — Information Systems (BSI), UFRN.**

Coursework, study repositories and projects, organized **by discipline** (official course
codes) with **complete commit history preserved** — original authors, dates and messages intact.

</div>

---

## 📌 About

This repository consolidates years of undergraduate work into one place, organized by
discipline (e.g. `DCT0008-data-structures`). Each folder keeps native `git log` / `git blame`;
still-evolving projects are included as **git submodules**; lecture slides live in each
discipline's `course-materials/`. See [`MANIFEST.md`](./MANIFEST.md) for full provenance.

```bash
# clone including submodules
git clone --recurse-submodules git@github.com:ZauJulio/LearningInformationSystems.git
```

## 🗂️ Disciplines

### Programming & Software Engineering
| Folder | Discipline |
|---|---|
| [`DCT1106-programming`](./DCT1106-programming) | Programming (Sig-Library) |
| [`DCT1108-object-oriented-programming-ii`](./DCT1108-object-oriented-programming-ii) | Object-Oriented Programming II |
| [`DCT1109-web-programming`](./DCT1109-web-programming) | Web Programming (+ CutTheChase ↗️) |
| [`DCT2301-software-engineering-i`](./DCT2301-software-engineering-i) | Software Engineering I |
| [`DCT2304-software-testing`](./DCT2304-software-testing) | Software Testing |
| [`DCT4403-advanced-topics-in-programming-iii`](./DCT4403-advanced-topics-in-programming-iii) | Advanced Topics in Programming III (AI) |
| [`DCT1010-programming-languages-and-compilers`](./DCT1010-programming-languages-and-compilers) | Programming Languages & Compilers (+ graphya) |

### Systems & Networks
| Folder | Discipline |
|---|---|
| [`DCT0008-data-structures`](./DCT0008-data-structures) | Data Structures (+ 📺 [video lectures](./DCT0008-data-structures/VIDEO_LECTURES.md)) |
| [`DCT1105-computer-architecture`](./DCT1105-computer-architecture) | Computer Architecture |
| [`DCT2101-operating-systems`](./DCT2101-operating-systems) | Operating Systems |
| [`DCT2102-computer-networks`](./DCT2102-computer-networks) | Computer Networks |
| [`DCT4101-network-server-administration`](./DCT4101-network-server-administration) | Network Server Administration |

### Data, AI & Machine Learning
| Folder | Discipline |
|---|---|
| [`DCT1401-artificial-intelligence`](./DCT1401-artificial-intelligence) | Artificial Intelligence (+ AI extensions) |
| [`DCT2602-machine-learning`](./DCT2602-machine-learning) | Machine Learning |
| [`DCT2403-decision-support-systems`](./DCT2403-decision-support-systems) | Decision Support Systems |
| [`DCT2201-databases`](./DCT2201-databases) | Databases |
| [`DCT2202-database-design-and-administration`](./DCT2202-database-design-and-administration) | Database Design & Administration |
| [`DCT1305-probability-and-statistics`](./DCT1305-probability-and-statistics) | Probability & Statistics |

### Security · Mathematics · Business
| Folder | Discipline |
|---|---|
| [`DCT4302-special-topics-in-information-security-i`](./DCT4302-special-topics-in-information-security-i) 🔒 | Special Topics in Information Security I |
| [`DCT1304-linear-algebra`](./DCT1304-linear-algebra) 🔒 | Linear Algebra |
| [`DCT3202-accounting-and-costs`](./DCT3202-accounting-and-costs) | Accounting & Costs |
| [`BSI3103-it-entrepreneurship`](./BSI3103-it-entrepreneurship) | IT Entrepreneurship |
| [`DCT0435-ethics`](./DCT0435-ethics) | Ethics |

## 🎓 Thesis & Studies
| Folder | Content |
|---|---|
| [`thesis`](./thesis) | Undergraduate final project (TCC) + `features-analyzer` ↗️ |
| [`extra-studies`](./extra-studies) | Non-discipline studies: PyQt, Rust, Taskiano ↗️ |

🔒 = sourced from a private repository · ↗️ = git submodule

## 🔎 Traceability

```bash
git log -- DCT1109-web-programming/      # full history of a discipline folder
git blame DCT1109-web-programming/src/...
git submodule update --init --recursive  # populate submodules
```

Folder origins, submodules and integration details: [`MANIFEST.md`](./MANIFEST.md).

> 📌 Exams and heavy media (videos, virtualenvs) are excluded via `.gitignore`; video
> lectures are linked to their source instead of stored.

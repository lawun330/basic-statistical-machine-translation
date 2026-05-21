# Basic Statistical Machine Translation

## Overview

## Error-Free PBSMT Workflow

- Install Moses and GIZA++
- Optionally configure paths in 
    - config.baseline, generate_configs.pl,
    - generate_sgms.pl, src2sgm.pl, and ref2sgm.pl
- Create config.baseline for two translation directions using `generate_configs.pl`
- Create SGMs using `generate_sgms.pl`
- Copy the `mkcls` file from the `giza-pp/mkcls-v2/` folder to the `giza-pp/GIZA++-v2/` folder
- Install ImageMagick and Graphviz using sudo
- Edit line 950 of `ubuntu-17.04/moses/scripts/generic/mteval-v13a.pl` to use *\p{Line_Break=Hyphen}* instead of *\p{Line_Break}*

## Dataset

- [Sayar's G2P dataset](https://github.com/ye-kyaw-thu/AIE-F/tree/main/slide-code/class-13and14/data)

## File Structure
```
/
...
├── img/
├── notebooks/
│
├── baseline/
│   ├── logs/
│   ├── my-ph/
│   │   ├── corpus/
│   │   ├── evaluation/
│   │   ├── lm/
│   │   ├── model/
│   │   ├── steps/
│   │   ├── training/
│   │   ├── tuning/
│   └── ph-my/
│       └── ...
│
├── data/
│   ├── g2p-par/                    # originally Sayar's
│   ├── cleaned/
│   │   └── test-sgm/
│   │       ├── generate_sgms.pl    # originally Sayar's
│   │       ├── src2sgm.pl          # originally Sayar's
│   │       └── ref2sgm.pl          # originally Sayar's
│   └── logs/
│
├── syl-normalizer/                 # originally Sayar's
│
├── config.baseline                 # originally Sayar's # modified paths # uncomment multi-bleu
├── generate_configs.pl             # originally Sayar's # modified paths
└── run-baseline.pl                 # originally Sayar's # modified paths
```

## References

- [Moses SMT Framework](https://www.statmt.org/moses-release/RELEASE-4.0/binaries/)
- [In-Class Tutorial](https://github.com/ye-kyaw-thu/AIE-F/tree/main/slide-code/class-13and14/SMT_Tutorial)
- [PBSMT Example](https://github.com/ye-kyaw-thu/MTRSS/tree/master/pbsmt)

## Note

This project was done for educational purposes as an assignment for the AI Engineering Fundamentals class taught by [*Sayar Ye Kyaw Thu*](https://github.com/ye-kyaw-thu).
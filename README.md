# Basic Statistical Machine Translation

## Overview

## Error-Free PBSMT Workflow

- Use Ubuntu-native Perl v5.38
- Install Moses and GIZA++
- Optionally configure paths in 
    - config.baseline, generate_configs.pl,
    - generate_sgms.pl, src2sgm.pl, and ref2sgm.pl
- Create config.baseline for two translation directions using `generate_configs.pl`
- Create SGMs using `generate_sgms.pl`
- Copy the `mkcls` file from the `giza-pp/mkcls-v2/` folder to the `giza-pp/GIZA++-v2/` folder
- Install ImageMagick and Graphviz using sudo
- Edit `ubuntu-17.04/moses/scripts/generic/mteval-v13a.pl`:
    ```perl
    line 950: \p{Line_Break} # replace this
    line 950: \p{Line_Break=Hyphen} # with this
    ```

## Dataset

- [Sayar's G2P dataset](https://github.com/ye-kyaw-thu/AIE-F/tree/main/slide-code/class-13and14/data)

## File Structure
```
/
...
├── img/
├── notebooks/
│
├── baseline/           # run1 to run3 with data v1
│   ├── logs/
│   ├── my-ph/
│   │   ├── corpus/
│   │   ├── evaluation/
│   │   ├── lm/
│   │   ├── model/
│   │   ├── steps/
│   │   ├── training/
│   │   └── tuning/
│   └── ph-my/
│       └── ...
├── baseline2/          # run4 to run6 with data v2
│   └── ...
│
├── data/
│   ├── g2p-par/                    # originally Sayar's
│   ├── cleaned/                    # preprocessed data (version 1)
│   │   ├── ...
│   │   └── test-sgm/
│   │       ├── generate_sgms.pl    # originally Sayar's
│   │       ├── src2sgm.pl          # originally Sayar's
│   │       └── ref2sgm.pl          # originally Sayar's
│   ├── cleaned_2/                  # preprocessed data (version 2)
│   │   └── ...
│   └── logs/
│
├── syl-normalizer/     # originally Sayar's # modified to merge with previous token for athat (်) cases
│
├── config.baseline     # originally Sayar's # modified paths # uncomment multi-bleu
├── generate_configs.pl # originally Sayar's # modified paths
└── run-baseline.pl     # originally Sayar's # modified paths
```

## References

- [Moses SMT Framework](https://www.statmt.org/moses-release/RELEASE-4.0/binaries/)
- [GIZA](https://github.com/moses-smt/giza-pp)
- [MGIZA](https://github.com/moses-smt/mgiza)
- [In-Class Tutorial](https://github.com/ye-kyaw-thu/AIE-F/tree/main/slide-code/class-13and14/SMT_Tutorial)
- [PBSMT Example](https://github.com/ye-kyaw-thu/MTRSS/tree/master/pbsmt)

## Note

This project was done for educational purposes as an assignment for the AI Engineering Fundamentals class taught by [*Sayar Ye Kyaw Thu*](https://github.com/ye-kyaw-thu).
#!/usr/bin/env bash
cd /home/lawun330/Desktop/basic-statistical-machine-translation/baseline2/ph-my/tuning/tmp.3
/home/lawun330/NLP/ubuntu-17.04/moses/bin/extractor --sctype BLEU --scconfig case:true  --scfile run5.scores.dat --ffile run5.features.dat -r /home/lawun330/Desktop/basic-statistical-machine-translation/data/cleaned_2/dev.my -n run5.best100.out.gz

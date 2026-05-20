#!/usr/bin/env bash
cd /home/lawun330/Desktop/basic-statistical-machine-translation/baseline/ph-my/tuning/tmp.2
/home/lawun330/NLP/ubuntu-17.04/moses/bin/extractor --sctype BLEU --scconfig case:true  --scfile run4.scores.dat --ffile run4.features.dat -r /home/lawun330/Desktop/basic-statistical-machine-translation/data/cleaned/dev.my -n run4.best100.out.gz

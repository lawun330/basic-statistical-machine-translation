#!/usr/bin/env bash
cd /home/lawun330/Desktop/basic-statistical-machine-translation/baseline2/ph-my/tuning/tmp.2
/home/lawun330/NLP/ubuntu-17.04/moses/bin/extractor --sctype BLEU --scconfig case:true  --scfile run6.scores.dat --ffile run6.features.dat -r /home/lawun330/Desktop/basic-statistical-machine-translation/data/cleaned_2/dev.my -n run6.best100.out.gz

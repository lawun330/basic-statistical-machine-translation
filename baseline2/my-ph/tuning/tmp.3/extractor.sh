#!/usr/bin/env bash
cd /home/lawun330/Desktop/basic-statistical-machine-translation/baseline2/my-ph/tuning/tmp.3
/home/lawun330/NLP/ubuntu-17.04/moses/bin/extractor --sctype BLEU --scconfig case:true  --scfile run8.scores.dat --ffile run8.features.dat -r /home/lawun330/Desktop/basic-statistical-machine-translation/data/cleaned_2/dev.ph -n run8.best100.out.gz

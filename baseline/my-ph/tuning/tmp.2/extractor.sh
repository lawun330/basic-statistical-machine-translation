#!/usr/bin/env bash
cd /home/lawun330/Desktop/basic-statistical-machine-translation/baseline/my-ph/tuning/tmp.2
/home/lawun330/NLP/ubuntu-17.04/moses/bin/extractor --sctype BLEU --scconfig case:true  --scfile run3.scores.dat --ffile run3.features.dat -r /home/lawun330/Desktop/basic-statistical-machine-translation/data/cleaned/dev.ph -n run3.best100.out.gz

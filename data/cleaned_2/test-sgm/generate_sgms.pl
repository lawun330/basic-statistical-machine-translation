#!/usr/bin/perl
use strict;

# written by Ye, NECTEC
# for MTRSS, YTU, Myanmar

my @langs;

foreach my $trainFile ( <../train.[a-z][a-z]> ) # -- EDIT HERE --
{                        
        $trainFile =~ m/train.([a-z][a-z])/;
        push @langs, $1;
}

foreach my $lang (@langs)
{ 
    `./ref2sgm.pl $lang > test.$lang.ref.sgm`;
    `./src2sgm.pl $lang > test.$lang.src.sgm`;
}
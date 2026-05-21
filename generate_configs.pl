#!/usr/bin/perl

# Preparing configuration files for PBSMT experiments
# Output: one configuration file for baseline or PBSMT
# *** Before you run this script, you should prepare training, development and test parallel-data in advance!!!

# Written by Finch-san and Ye
# We used this script for running our NAACL paper:
# Ye Kyaw Thu, Andrew Finch and Eiichiro Sumita, 
# "Interlocking Phrases in Phrase-based Statistical Machine Translation",
# In Proceedings of the NAACL-HLT 2016, June 12-17, San Diego, US, pp. 1076-1081.

# Last updated 9 Oct 2019, @Machine Translation Research Summer School, YTU, Myanmar

use strict;

my @langs;

# you have to update the PBSMT experiment path!!!
my $smtpath = "/home/lawun330/Desktop/basic-statistical-machine-translation"; # -- EDIT HERE --

# you have to update the data path for running PBSMT experiment!!!
foreach my $trainFile ( </home/lawun330/Desktop/basic-statistical-machine-translation/data/cleaned_2/train.[a-z][a-z]> ) # -- EDIT HERE --
{                        
        $trainFile =~ m/train.([a-z][a-z])/;
        
        push @langs, $1;
}

foreach my $expt (qw/baseline2/)
{
die("$smtpath/$expt") if (-d "$smtpath/$expt");
`mkdir $smtpath/$expt`;
    foreach my $src (@langs)
    {
    	foreach my $trg (@langs)
    	{
    		next if $src eq $trg;
            #next if $src ne "my" and $trg ne "my";
    
    		my $pair = "${src}-${trg}";
    		my $configFile = "$smtpath/$expt/$pair/config.${expt}.$pair";

    		`mkdir $smtpath/$expt/$pair`;

    		open FILE, ">$configFile" or die;
    
    		print FILE "# Config file for $pair ($expt)\n";
    		print FILE "\n[GENERAL]\n";
    		print FILE "working-dir = $smtpath/$expt/$pair\n";
    		print FILE "input-extension = ${src}\n";
    		print FILE "output-extension = ${trg}\n";
    		print FILE "pair-extension = ${pair}\n";
    		print FILE "\n";
    		close FILE;

    		`cat $configFile $smtpath/config.$expt > $smtpath/tmp`;
    		`mv $smtpath/tmp $configFile`;
   	    }
    }
}
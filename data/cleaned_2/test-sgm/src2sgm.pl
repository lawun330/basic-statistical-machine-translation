#!/usr/bin/perl
use strict;

# written by Ye, NECTEC
# for MTRSS, YTU, Myanmar

my $src = shift;

print "<srcset setid=\"Burmese_G2P_data\" srclang=\"any\">\n"; # -- EDIT HERE --
print "<doc docid=\"none\" genre=\"100\" origlang=\"$src\">\n";

open FILE, "../test.$src" or die; # -- EDIT HERE --

my $id=1;

while( <FILE> )
{
	chomp;
	
	print "<seg id=\"$id\">$_ </seg>\n";
	$id++;
}

print "</doc>\n</srcset>\n";
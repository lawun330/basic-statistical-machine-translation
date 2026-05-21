#!/usr/bin/perl
use strict;

# written by Ye, NECTEC
# for MTRSS, YTU, Myanmar

my $trg = shift;

print "<refset trglang=\"$trg\" setid=\"Burmese_G2P_data\" srclang=\"any\">\n"; # -- EDIT HERE --
print "<doc sysid=\"ref\" docid=\"none\" genre=\"100\" origlang=\"any\">\n";

open FILE, "../test.$trg" or die; # -- EDIT HERE --
             
my $id=1;

while( <FILE> )
{
	chomp;
	
	print "<seg id=\"$id\">$_ </seg>\n";
	$id++;
}

print "</doc>\n</refset>\n";
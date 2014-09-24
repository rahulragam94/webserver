#!/usr/bin/perl
chdir '/home/rahul/Downloads/DCPlusPlus-xxx-src/dcpp/';
opendir my $dir,'/home/rahul/Downloads/DCPlusPlus-xxx-src/dcpp/';
my @filelist=readdir ($dir);
foreach my $filename (@filelist){
open CURRENT,$filename;
my $found=0;
#print "$filename"."\n";
while(<CURRENT>&&($found==0)){
my $contents=<CURRENT>;	
if($contents=~m/Lock/){
print "$filename"."\n";
$found=1;
}
}
}

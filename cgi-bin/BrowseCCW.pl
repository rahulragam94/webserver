#!/usr/bin/perl
use strict;
use WWW::Mechanize;

my $username= "ee12b102";
my $password= "9TI\@f+w0";
my $URL= "http://ccw.iitm.ac.in/";
my $URL2= "http://ccw.iitm.ac.in/?q=/IITMHostels/hostelstats/SHARAVATHI";
my $outfile = "out.html";


print "Content-type: text/html\n\n";
my $mech=WWW::Mechanize->new();

$mech->get($URL);
$mech->form_id('user-login-form');
$mech->field(name => "$username");
$mech->field(pass=> "$password");
$mech->click_button(value=>"Log in");
$mech->get($URL2);

my $response = $mech->content(); 
open(OUTFILE, ">>$outfile");
print OUTFILE "$response";
close(OUTFILE);

my @links= $mech->links();
my $i=0;
mkdir "Pics";
while($links[$i]){
	if($links[$i]->url()=~'/?q=/IITMHostels/sinfo/(.+)$'){
		$mech->get("http://photos.iitm.ac.in/byroll.php?roll=$1");
		print "$1\n";
		$response=$mech->content();
		#if($response){
			open(OUTFILE,">./Pics/$1.jpg");
			print OUTFILE "$response";
			close(OUTFILE);
		#}
	}
	$i=$i+1;
}
		

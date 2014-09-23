#!/usr/bin/perl -w
 use DBI;
  $dbh = DBI->connect('dbi:mysql:perltest','root','kundi') or die "Connection Error: $DBI::errstr\n";
  $sql = "select * from samples";
  $sth = $dbh->prepare($sql); 
  $sth->execute or die "SQL Error: $DBI::errstr\n"; 
  while (@row = $sth->fetchrow_array) 
  { print "@row\n"; 
	  }

#!/usr/bin/perl

# Use CGI methods to get parameters
use CGI;
my $cgi = CGI->new();
my %params = $cgi->Vars;


# Print document header
print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
  <title>POST/GET Variable Dump</title>
</head>
<body>

HTML


# If there is POST data, dump it
#   else display "No Data"
if ($ENV{REQUEST_METHOD} eq "POST" ) {

  # Header for data
  print "<h2>POST Data</h2>\n";
  print "<pre>\n<p>\n";

  # Walk through data
  foreach my $key (sort keys %params) {
    
    # If multiple values, display as such
    my $size = @{$cgi->{$key}};
    if ($size > 1) {
      my $count = 0;
      for (@{$cgi->{$key}}) {
        print "  $key\[$count\] => ", $cgi->{$key}[$count], "\n";
        $count++;
      }
    } else {
      # Display single value
      print "  $key => $cgi->{$key}[0]", "\n";
    }
    print "\n";
  }
  print "</pre>\n</p>\n";
} else {
  print "<h2>No POST Data</h2>\n";
}

# If there is GET data, dump it
#   else display "No Data"
if ($ENV{REQUEST_METHOD} eq "GET" ) {

  # Header for data
  print "<h2>GET Data</h2>\n";
  print "<pre>\n<p>\n";

  # Walk through data
  foreach my $key (sort keys %params) {

  # If multiple values, display as such
    my $size = @{$cgi->{$key}};
    if ($size > 1) {
      my $count = 0;
      for (@{$cgi->{$key}}) {
        print "  $key\[$count\] => ", $cgi->{$key}[$count], "\n";
        $count++;
      }
    } else {
      # Display single value
      print "  $key => $cgi->{$key}[0]", "\n";
    }
    print "\n";
  }
  print "</pre>\n</p>\n";
} else {
  print "<h2>No GET Data</h2>\n";
}


# Close document
print "</body>\n</html>";

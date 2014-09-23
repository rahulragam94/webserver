#!/usr/bin/perl

# Use the DBI library with the MySQL DBD
use DBI;
use DBD::mysql;


# Document header (doctype -> body tag)
sub docheader() {

print <<HTML;
Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1.dtd">
<html>
<head>
  <title>MySQL Query Result</title>
</head>
<body>

HTML

} # End docheader()


# Connect the DB with the given creds
sub connectDB($$$$) {

  my $host = shift;
  my $user = shift;
  my $password = shift;
  my $database = shift;

  $dblink = DBI->connect($host, $database, $user, $password);

  return $dblink;

}  # End connectDB()


# Do the query, return the result
sub doquery($$) {

  my $dblink = shift;
  my $sql_statement = shift;

  $result = $dblink->query($sql_statement);

  return $result;

} # End doquery()


# Output the results of the query in a table
sub dotable($) {

  my $result = shift;

print <<HTML;
<table border="1" cellpadding="5">
<tr>

HTML

  my $ttl_rows = $result->affectedrows;
  my @col_names = $result->name;

  for ($i=0; $i <= $ttl_rows - 1; $i++) {
    print "  <th>".$col_names[$i]."</th>\n";
  }

  print "</tr>\n";

  for ($rows = 1; $rows <= $ttl_rows; $rows++) {
    print "<tr>\n";
    @rowdata = $result->fetchrow;
    foreach $data (@rowdata) {
      print "  <td>".$data."</td>\n";
    }
    print "</tr>\n";
  }  

  print "</table>\n";

} # End dotable()


# Document footer (close tags and end document)
sub docfooter() {

print <<HTML;
</body>
</html>

HTML

}  # End docfooter()


sub main() {

  # Set up DB access vars
  my $host = "localhost";
  my $database = "mysqlsamp";
  my $user = "webuser";
  my $password = "password99";

  # Connect the DB
  $link = connectDB("localhost","webuser","password99","mysqlsamp");

# Set up and perform query
$query = <<HTML;
SELECT computers.comp_id as computer_id,
       mice.mouse_model as mouse_model,
       computers.comp_location as location
  FROM computers, mice
  WHERE mice.mouse_type = "USB"
  AND computers.comp_location like "A%"
  AND mice.mouse_comp = computers.comp_id

HTML

  $result = doquery($link,$query);

  # Do document header
  docheader();

  # Do results in table
  dotable($result);

  # Do document footer
  docfooter();


}  # End main()


# Kick it all off
main();



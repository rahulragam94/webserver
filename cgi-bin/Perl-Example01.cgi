#!/usr/bin/perl

# Use the Time::Piece library for our date/time needs
use Time::Piece;

# Set up the variables (today, month, year)
#  today = m/d/y
sub setvars() {

  # Default is today
  my $day = localtime->mday();
  my $month = localtime->mon();
  my $year = localtime->year();
  my $today = $month."/".$day."/".$year;
 
  # Return vars in a hash 
  my %t = ("today" => $today,
            "month" => $month,
            "year" => $year);
  return %t;
}  # End setvars()


# Do the document header
sub docheader($$) {

  my $month = shift;
  my $year = shift;

my $t = Time::Piece->strptime($month,"%m");
$month_text = $t->strftime("%B");

# Print the document header (up to first date row)
print <<HTML;
Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1.dtd">
<html>
<head>
  <title>Calendar - $month_text $year</title>
  <style type="text/css">
    tr.weekdays td { width: 100px;
                     text-align: center;
                   }
    tr.week td { width: 100px;
                 height: 100px;
                 color: black;  }
  </style>
</head>
<body>
<table border="1">

<!-- Controls and calendar title (month) -->
<tr>
  <td colspan="7" align="center">
    <strong>
      $month_text $year
    </strong>
  </td>
</tr>

<!-- Day of week header row -->
<tr class="weekdays">
  <th>Sunday</th>
  <th>Monday</th>
  <th>Tuesday</th>
  <th>Wednesday</th>
  <th>Thursday</th>
  <th>Friday</th>
  <th>Saturday</th>
</tr>

<!-- Calendar (days) start here -->

HTML

}  # End docheader()


# Do the document footer (close tags, end doc)
sub docfooter() {

print <<HTML;
<!-- Close all open tags, end document -->
</table>
</body>
</html>

HTML

} # End docfooter()


# Print an empty day (cell)
sub emptyday() {

print <<HTML;
  <td align="right" valign="top">&nbsp;</td>

HTML

} # End emptyday()


# Print a day cell
sub day($$$$) {

  my $today = shift;
  my $month = shift;
  my $day = shift;
  my $year = shift;
  my $font = "";

  my $curday = $month."/".$day."/".$year;
  if ( $curday eq $today ) {
    $font = " style=\"color: red;\"";
  }

print <<HTML;
  <td align="right" valign="top" $font>$day</td>

HTML

} # End day()


# Open or close a row
sub weekrow($) {

  my $cmd = shift;

  if ($cmd eq "open") {
    print "<tr class=\"week\">\n";
  }
  if ($cmd eq "close") {
      print "</tr>\n";
  }

}  # End weekrow()


# Main program body
sub main() {

  # Set the date vars
  my %vars = setvars();
  my $today = $vars{'today'};
  my $month = $vars{'month'};
  my $year = $vars{'year'};

  # Do the header and open first row
  docheader($month,$year);
  weekrow("open");

  # Set up first weekday and 1st day (m/1/y)
  my $t = Time::Piece->strptime($month."/1/".$year,
                                "%m/%d/%Y");

  my $first_weekday = $t->strftime("%w") + 1;
  my $day = 1;

  # Print empty days up to the first weekday of month
  for ($weekday = 1; $weekday < $first_weekday; $weekday++) {
    emptyday();
  }

  my $last_day = $t->month_last_day;

  # Do rest of month while we have a valid date
  while ($day <= $last_day) {
    # If SUN, open the row
    if ($weekday == 1) {
      weekrow("open");
    }
    # Print day and increment
    day($today,$month,$day,$year);
    $weekday++;
    $day++;
    # If SAT, close row reset weekday
    if ($weekday > 7) {
      weekrow("close");
      $weekday = 1;
    }

  }

  # Close current week
  while ($weekday != 1 && $weekday <= 7) {
    emptyday();
    $weekday++;
  }

  # Close document
  docfooter();

} # End main();


# Kick it all off
main();



#!/usr/bin/python

import cgitb, os, sys
cgitb.enable()
sys.stderr = sys.stdout

import cgi
import time
import calendar

from datetime import date

def decrement_month(month, year):
     prev_month = month - 1
     if prev_month <= 0:
        prev_month = 12
        prev_year = year -1
     else:
        prev_year = year
     return prev_month, prev_year

def increment_month(month, year):
     next_month = month + 1
     if next_month > 12:
        next_month = 1
        next_year = year +1
     else:
        next_year = year
     return next_month, next_year


print '''Content-Type: text/html\n\n

     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0//EN"
         "http://www.w3.org/TR/xhtml1/DTD/xhtml1.dtd">'''

form = cgi.FieldStorage()

today = date.today()

if form.has_key('month') and form.has_key('year'):
    # Use month and year from form submission
    thisyear = int(form.getvalue('year'))
    thismonth = int(form.getvalue('month'))
    
    if form.has_key('next'):
        thismonth, thisyear = increment_month(thismonth, thisyear)
    elif form.has_key('prev'):
        thismonth, thisyear = decrement_month(thismonth, thisyear)
        
    if thisyear == today.year and thismonth == today.month:
        thisday = today.day
    else:
        thisday = -1
else:
    # Use today
    thisyear = today.year
    thismonth = today.month
    thisday = today.day
     
     
def docheader(month, year):
     ''' month is an integer month number
         year is an integer year '''

     t = time.strptime(str(month), '%m')
     month_text = time.strftime('%B', t)

     my_name = os.environ['SCRIPT_NAME']
     
     data = '''<html>
     <head>
        <title>Calendar - %(month_text)s %(year)s</title>
        <style type="text/css">
          tr.weekdays td { width: 100px;
                       text-align: center;
                     }
          tr.week td { width: 100px;
                   height: 100px;
                   color: black; }
        </style>
     </head>

     <body>
     <form method="POST" action="%(my_name)s">
     <table border="1">

     <!-- Controls and calendar title (month) -->
     <tr>
     <td colspan="1" align="left">
     <input type="submit" name="prev" value="&lt;&lt;" />
     <input type="hidden" name="month" value="%(month)d" />
     <input type="hidden" name="year" value="%(year)d" />
     </td>
     <td colspan="5" align="center">
     <strong>
     %(month_text)s %(year)s
     </strong>
     </td>
     <td colspan="1" align="right">
     <input type="submit" name="next" value="&gt;&gt;" />
     </td>
     </tr>
     </form>

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
    ''' %  locals()
    
     return data
     
def do_calendar(thismonth, thisyear, thisday):

     calendar.setfirstweekday(6) #Set first day of week to Sunday
     month = calendar.monthcalendar(thisyear, thismonth)
     print docheader(thismonth, thisyear)
     for week in month:
         i=0
         print '<tr class="week">'
         for day in week:
             if int(day) == int(thisday):
                  print '   <td align="right" valign="top" style="color: red">'
                  print '    <b>',day,'</b>'
             elif int(day):
                  print '   <td align="right" valign="top">'
                  print '    <b>',day,'</b>'
             else:
                  print '   <td align="right" valign="top">'
                  print '   &nbsp;</td>'
         print '</tr>'
     print '</table>'
     print '</body></html>'

do_calendar(thismonth, thisyear, thisday)

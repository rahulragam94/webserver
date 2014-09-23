#!/usr/bin/python

import os, sys
import cgi
import time
import calendar

from datetime import datetime

date = datetime.now().date()
today= date.strftime("%m %Y")
thisyear = date.strftime("%Y")
thismonth = date.strftime("%m")
thisday = date.strftime("%d")

def docheader(month, year):
     ''' month is a string with the month number
         year is a string with the year '''

     t = time.strptime(month, '%m')
     month_text = time.strftime('%B', t)

     data = '''Content-type: text/html

     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0//EN"
         "http://www.w3.org/TR/xhtml1/DTD/xhtml1.dtd">
     <html>
     <head>
        <title>Calendar - %(month)s %(year)s</title>
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
     <table border="1">
 
     <!-- Calendar title (month) -->
     <tr>
        <td colspan="7" align="center">
          <strong>
            %(month)s %(year)s 
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
    ''' %  { 'month':month_text, 'year':year }
     return data

def do_calendar(thismonth, thisyear):

     calendar.setfirstweekday(6) #Set first day of week to Sunday
     month = calendar.monthcalendar(int(thisyear),int(thismonth))
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

do_calendar(thismonth, thisyear)

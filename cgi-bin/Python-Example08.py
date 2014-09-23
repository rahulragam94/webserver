#!/usr/bin/python

import MySQLdb
import MySQLdb.cursors
import cgi

def printheader():
     print """Content-Type: text/html

     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
     <html>
       <head>
        <title>MySQL Query Result</title>
       </head>
     <body>\n\n"""

def getdata():       
     conn = MySQLdb.Connect(
         host='localhost', user='webuser',
         passwd='password99', db='mysqlsamp',compress=1)
     cursor = conn.cursor()
     cursor.execute("""SELECT computers.comp_id as computer_id,
         mice.mouse_model as mouse_model,
         computers.comp_location as location
         FROM computers, mice
         WHERE mice.mouse_type = "USB"
         AND computers.comp_location like "A%"
         AND mice.mouse_comp = computers.comp_id;""")

     print ''' 
     <table border="1" cellpadding="5">
     '''
     rows = cursor.fetchall()

     print "<tr>"
     for col in cursor.description:
          print '<td>%s</td>' % col[0]
     print "</tr>"
   
     for row in rows:
          print "<tr>"
          for cell in row:
              print "<td> %s </td>" % cell
          print "</tr>"

     cursor.close()
     conn.close()

# Document footer (close tags and end document)
def docfooter():
     
     print ''' 
     </body>
     </html>
     
     '''
     
# End docfooter()

printheader()
getdata()
docfooter()

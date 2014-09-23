#! /usr/bin/python
import os, sys
import cgi

print '''Content-type: text/html

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1.dtd">
    <html> <head> <title>MySQL Query Result</title> </head>
    <body>
    <table border="1" cellpadding="5"><form>'''


#Initialize found_post_data variable
found_post_data = False
#Check whether there is POST data
if ( os.environ['REQUEST_METHOD'] == 'POST' ):
    form = cgi.FieldStorage()
    #If the form filled in by cgi.FieldStorage isn't empty
    if form.list != []:
        found_post_data = True
        print "<b>POST DATA</b><br><br>"
        #Iterate over all the keys printing the key and it's value
        for key in form:
             datalist = form.getlist(key)
             if len(datalist) == 1:
                  print "%s => %s<br>" % (key,datalist[0])
             else:
                  for i, item in enumerate(datalist):
                       print "%s[][%d]=> %s<br>" % (key, i, item)

#If there is no post data, say so.
if not found_post_data:
    print "<b>No POST data.</b><br>"

print '<br>'

# Get a dict with all the query parameters
query_params = os.environ.has_key('QUERY_STRING') \
    and cgi.parse_qs(os.environ['QUERY_STRING'], keep_blank_values=True)

if query_params:
    print "<b>GET DATA</b><br><br>"
    for key, value in query_params.iteritems():
        if len(value) == 1:
              print "%s => %s<br>" % (key,value[0])
        else:
              for i, item in enumerate(value):
                   print "%s[][%d]=> %s<br>" % (key, i, item)

else:
    #If there is no GET data,say so.
    print "<b>No GET data.</b><br>"


print "</form></table></body></html>"

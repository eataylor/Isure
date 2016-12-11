
from django import template

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

from wordpress_xmlrpc.methods import posts 

register = template.Library()

#@register.simple_tag
@register.inclusion_tag('archive.html')
def archive():

    	print "*************Enter archivs **************"
        theseposts = ''

    	client = Client('http://intersure.tmcmarkets.com/xmlrpc.php', 'taylorea@gmail.com', 'indigo9a')
	theseposts = client.call(posts.GetPosts({'post_status': 'publish'}))

	linklist=[]
	for item in theseposts:
	    if item.post_status == "publish": 
	       #print item.date_modified.year,item.date_modified.month,item.post_status,item.title,item.slug,"\n"
	       thispostdate = str(item.date_modified.year)+'/'+str(item.date_modified.month)
               #print "This Post Date = ",thispostdate 
	       if thispostdate in linklist or thispostdate == "2016/11":
		   pass
	       else:
		   linklist.append(thispostdate)
	#print linklist               

	linktext = []
	months = ['January','February','March','April','May','June','July','August','September','October','November','December'] 
	for item in linklist: 
	    datesplit = item.split("/")
	    thismonth = months[int(datesplit[1])-1] + ' ' +datesplit[0]
	    #print "This month = ",thismonth,item 
	    linktext.append(thismonth)

        zippedlist = zip(linklist,linktext)
	    
	     


    
        return {'zippedlist': zippedlist}

 


from django import template

register = template.Library()

@register.filter(name='namesplit')
def namesplit(name): # Only one argument.
     """splits a string """
     namesplit = name.split(' ',2)
     print "******", len(namesplit)
     print namesplit 
     if len(namesplit) < 2:
        newname = name
     else:
        newname = namesplit[0] + ' '+namesplit[1]
        if namesplit[1] == "&":
           newname = newname + namesplit[2] 
        
     return newname

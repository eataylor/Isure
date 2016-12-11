
from django import template

from Isure.models  import Directory 

register = template.Library()

#@register.simple_tag
@register.inclusion_tag('locations.html')
def get_locations():

    #print "*************Enter get_quick_links **************"

    #Rel = PressRel.objects.all()
    Locations = Directory.objects.all()
    
     

    
    return {'Locations': Locations}

 

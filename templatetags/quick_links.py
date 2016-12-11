
from django import template

from Isure.models  import PressRel,LocalLinks 

register = template.Library()

#@register.simple_tag
@register.inclusion_tag('ql1.html')
def get_quick_links():

    #print "*************Enter get_quick_links **************"

    #Rel = PressRel.objects.all()
    Links = LocalLinks.objects.all()

    
    return {'links': Links}

@register.inclusion_tag('ql2.html')
def get_quick_rels():

    #print "*************Enter get_quick_rels **************"

    Rels = PressRel.objects.all()
    #Links = LocalLinks.objects.all()

    
    return {'rels': Rels}

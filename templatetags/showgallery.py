
from django import template

from photo.models  import Album

register = template.Library()

#@register.simple_tag
@register.inclusion_tag('showgallery.html')
def showgallery():

    print "*************Enter show Gallery **************"

    #Rel = PressRel.objects.all()
    albumdict = {}
    albumdict1 = {}
    imagelist = [] 
    #albums = Album.objects.all()
    albums = Album.objects.filter(public=True).order_by('-id')
    for album in albums:

        images = album.images_as_list() 
        thumbs = album.images_thumbs() 
        galleries = zip(images,thumbs)
        albumdict[album.title]=galleries
     
     
    #print "******the dictionary is ",albumdict
    return {'albumdict': albumdict}

 

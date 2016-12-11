from django.contrib import admin

# Register your models here.

from Isure.models import Directory,QuickLinks,Event,PressRel,LocalLinks
from Isure.models import Commercials,Personals,AccessList
 

class DirectoryAdmin(admin.ModelAdmin):
    #fields = ['firstname','lastname']
     
    def save_model(self, request, obj, form, change):
        #obj.user = request.user
         
        print "***Enter Directory Save_model in admin ***"
         
        
        if change:
           if 'tags' in form.changed_data:
               print " Found tags in changed form "
               taglist = obj.tags
               print "list = ",taglist
           else:
               print "  tags Not in changed form "
        else:
           print "Not a Change"
        
        obj.save()
     



    ordering = ('AgencyName',)
    list_display   = ('AgencyName','BusinessType' )
    fieldsets = [
    ('Contact', {'fields': (('AgencyName'),('PrimaryContactFN', 'PrimaryContactLN','ContactTitle','ContactEmail','DirectLine'))}),
     
     ('URL', {'fields': (('url',))}), 
     
     ('Business Type', {'fields': (('BusinessType',))}),
     
     ('Principals', {'fields': (('principals',))}),
     ('Employees', {'fields': (('employees',))}),

     ('Business Breakdown', {'fields': (('Revenue'),('CommPct','BenePct','PersPct' ))}),

     ('Office Systems', {'fields': (('CRM','AMS' ))}),

     ('Tags', {'fields': (('tags',))}),
        ('Address', {'fields': (('HQAddress','HQAddress2','HQCity','HQState','HQZip','HQCountry'))}),
        ('Key Contact', {'fields': (('KeyContactFN','KeyContactLN','KeyContactEmail','KeyContactPhone'))}),
        ('Lat/Long', {'fields': (('HQLat','HQLong'))}),
        ('Logo Image', {'fields': (('Image',))}),
        ('Diff', {'fields': (('Differentiator',))}),
        ('Commercial Lines', {'fields': (('commercialLines',))}),
        ('Personal Lines', {'fields': (('personalLines',))}),
        
     ('Key Goals', {'fields': (('goals1','goals2','goals3',))}),
     ('Awards/Accolades', {'fields': (('awards1','awards2','awards3',))}), 

    ]
    filter_horizontal = ('commercialLines','personalLines',)

class AccessListAdmin(admin.ModelAdmin):
      ordering = ('last_name',)
      list_display   = ('last_name','first_name','email'  )
      fieldsets = [
    ('Access List', {'fields': (('last_name','first_name','email'),)}),
    ]


class CommercialsAdmin(admin.ModelAdmin):
      list_display   = ('Name',  )
      fieldsets = [
    ('Company Name', {'fields': (('Name'),)}),
    ]
class PersonalsAdmin(admin.ModelAdmin):
      list_display   = ('Name',  )
      fieldsets = [
    ('Company Name', {'fields': (('Name'),)}),
    ]


class PressRelAdmin(admin.ModelAdmin):
      list_display   = ('postDate','blurb',  )
      fieldsets = [
    ('Press Release', {'fields': (('postDate'),('filename', 'blurb','publish'))}),
    ]


class LocalLinksAdmin(admin.ModelAdmin):
      list_display   = ('postDate','blurb',  )
      fieldsets = [
    ('Local Links', {'fields': (('postDate'),('blurb', 'link','publish'))}),
    ]


class QuickLinksAdmin(admin.ModelAdmin):
      list_display   = ('Linktype',  )
      fieldsets = [
    ('Links', {'fields': (('Linktype'),('filename', 'eventname','event_id'))}),
      ]

class EventAdmin(admin.ModelAdmin):
      list_display   = ('EventSummary',  )
      fieldsets = [
    ('Event', {'fields': (('EventText'), )}),
      ]


admin.site.register(AccessList,AccessListAdmin)
admin.site.register(Commercials,CommercialsAdmin)
admin.site.register(Personals,PersonalsAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Directory,DirectoryAdmin)
admin.site.register(LocalLinks,LocalLinksAdmin)
admin.site.register(PressRel,PressRelAdmin)
admin.site.register(QuickLinks,QuickLinksAdmin)

from django.contrib import admin
from dictionnaire.entity.models import Pays, Organisme, TypesOrganisme, TypesCourrier, NaturesCourrier, Workflow

# Register your models here.

admin.site.register(Organisme)
admin.site.register(TypesOrganisme)
admin.site.register(Pays)
admin.site.register(TypesCourrier)
admin.site.register(NaturesCourrier)
admin.site.register(Workflow)




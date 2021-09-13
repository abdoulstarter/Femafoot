from django.contrib import admin
from courrier.models import Courrier
# Register your models here.


admin.site.register(Courrier)
class CourrierAdmin(admin.ModelAdmin):
    list_display = ("titre",
                    "urgence",
                    "organisme",
                    "type_courrier",
                    "nature_courrier",
                    "assigner_a",
                    "date_creation"
                    )
    search_fields = ("titre",
                     "type_courrier",
                     "nature_courrier",
                     "assigner_a"
                     )
    list_filter = ("titre",
                   "type_courrier",
                   "nature_courrier",
                   "assigner_a"
                   )
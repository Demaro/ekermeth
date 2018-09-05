from django.contrib import admin
from .models import Contacto
# Register your models here.



class ContactoAdmin(admin.ModelAdmin):
    list_display = ["id",  "name", "email", "fono", "company", "message"]
    list_editable     = [ "name", "message",  ]
    list_filter	       = [  "name" , "email", ]
    

    # search_fields = ["nombre"]
    class Meta:
        model = Contacto
        

admin.site.register(Contacto, ContactoAdmin)



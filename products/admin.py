from django.contrib import admin
from .models import Producto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id",  "name", "description", "user", "categoria", "precio", "date"]
    list_editable     = [ "name", "description", "user" , "categoria", "precio"]
    list_filter	       = [  "name" , "user", "categoria"]
    

    # search_fields = ["nombre"]
    class Meta:
        model = Producto


class CategoriAdmin(admin.ModelAdmin):
	list_display = ["id", "name"]
	list_editable = ["name"]

	class Meta:
		model = Categoria

        

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Categoria, CategoriAdmin)
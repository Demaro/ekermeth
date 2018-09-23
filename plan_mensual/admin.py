from django.contrib import admin
from .models import Plan_mensual, Gasto_general

class PlanAdmin(admin.ModelAdmin):
    list_display = ["id",  "user", "diario", "date_start", "total",]
    list_editable     = [ "user", "diario", "total",]
    list_filter	       = [  "user" , "diario", "total", "date_start",]
    list_horizontal		= [ "gasto_general" ]
    

    # search_fields = ["nombre"]
    class Meta:
        model = Plan_mensual


class GastoGeneralAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "value", "if_default"]
	list_editable = ["name", "value", "if_default"]

	class Meta:
		model = Gasto_general

        

admin.site.register(Plan_mensual, PlanAdmin)

admin.site.register(Gasto_general, GastoGeneralAdmin)


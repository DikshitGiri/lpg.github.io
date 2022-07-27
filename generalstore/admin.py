
from django.contrib import admin
from generalstore.models import  category, gasentry, gasondemand


admin.site.register(gasentry)
admin.site.register(gasondemand)
admin.site.register(category)


from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(employee)
admin.site.register(head)
admin.site.register(leave)
admin.site.register(apply)
admin.site.register(comment)
admin.site.register(designation)
admin.site.register(department)
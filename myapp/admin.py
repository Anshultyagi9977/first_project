from django.contrib import admin
from myapp import models

# Register your models here.

admin.site.register(models.StudentData)
admin.site.register(models.UserData)
admin.site.register(models.BookDetails)
admin.site.register(models.ConsumerDetails)
admin.site.register(models.ItemInventory)
admin.site.register(models.StudentStatus)
admin.site.register(models.BankDetails)
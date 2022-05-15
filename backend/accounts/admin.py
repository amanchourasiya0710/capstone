from django.contrib import admin
from .models import UserAccount
from .models import Roles, Department
# from forms.models import Roles, Department

# Register your models here.
admin.site.register(Roles)
admin.site.register(Department)

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
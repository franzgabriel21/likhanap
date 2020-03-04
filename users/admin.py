from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


class AccountAdmin(UserAdmin):
	list_display = ('email','username', 'name', 'usertype', 'city', 'street' 'date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Profile)

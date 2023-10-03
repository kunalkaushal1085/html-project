from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User  # Import the User model

class CustomUserAdmin(UserAdmin):
    # Customize the UserAdmin class as needed
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# Register the User model with your custom admin class
admin.site.unregister(User)  # Unregister the default UserAdmin
admin.site.register(User, CustomUserAdmin)  # Register with your custom UserAdmin




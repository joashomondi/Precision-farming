from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# # Register your models here.



class UserAdminConfig(UserAdmin):
    # model = User
    
    search_fields = ('email','first_name', 'last_name')
    ordering = ('date_joined',)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_filter = ('email','user_name','is_active','is_staff')
    list_display = ('email','id', 'is_active','is_staff', 'is_verified')

    fieldsets = (
        (None,{'fields':('email',)}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser', 'is_verified')}),
        

    )

    # formfield_overrides = {
    #     User.<if you want to imply on a certain field> : {'widget': Textarea(attrs={'rows':10,'cols':40})},

    # }

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None,{
        'classes':('wide',),
        'fields':('email', 'password1','password2','is_staff','is_active', 'is_verified'),
        }),

    )

admin.site.register(User, UserAdminConfig)
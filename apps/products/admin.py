from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Product, File, Comment, Advertisement, Favorite, Categories


# Register your models here.

class ImagesInline(admin.StackedInline):
    model = File
    extra = 0


class CommentsInline(GenericTabularInline):
    model = Comment
    fields = ['author', 'message', 'rating']
    readonly_fields = ['author', 'message', 'rating']
    can_delete = False
    verbose_name_plural = 'Comments'
    extra = 1

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, CommentsInline]
    prepopulated_fields = {'slug': ('name',)}
    horizontal_filter = ('category',)
    list_display = ('name', 'price', 'stock_available', 'availability',)
    readonly_fields = ('created_at', 'updated_at')


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'description', 'icon',)
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Advertisement)
admin.site.register(Favorite)


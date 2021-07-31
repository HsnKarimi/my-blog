from django.contrib import admin
from .models import Post,Categoty
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "position","parent", "status")
    list_filter = (["status"])
    search_fields = ("name", "slug")
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(Categoty, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("name","slug","author","publish","status","category_to_str")
    list_filter = ("publish","status")
    search_fields = ("name","subtitle")
    prepopulated_fields = {'slug':("name",)}
    def category_to_str(self,obj):
        return "،".join([category.name for category in obj.category_published()])
    category_to_str.short_description = 'دسته بندی ها'


admin.site.register(Post,PostAdmin)




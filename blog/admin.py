from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):
    """
    Класс для экстра добавления рецептов в админке
    """
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]
    inlines = [RecipeInline]
    # Кнопка сохранить будет и сверху и снизу в админке
    save_as = True
    save_on_top = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)

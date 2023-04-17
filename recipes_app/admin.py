from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class MeasurementUnitAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class RecipeIngredientsInline(admin.TabularInline):
    model = models.RecipeIngredients
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'display_tag', 'author', 'create_at', 'cook_time')
    inlines = [RecipeIngredientsInline]
    list_filter = ('category', 'author', 'cook_time', 'create_at')
    search_fields = ('title',)
    # fieldsets = (
    #     ('Recepto kūrėjas', {'fields': ('create_at', 'author')}),
    #     ('Recepto aprašymas', {'fields': ('title', 'category', 'tags', 'description', 'image')}),
    #     ('Informacija', {'fields': ('serves', 'cook_time', 'directions', 'notes')}),
    # )


class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity', 'measurement_unit')
    list_filter = ('recipe', 'ingredient', 'measurement_unit')
    fieldsets = (
        ('Receptas', {'fields': ('recipe',)}),
        ('Informacija', {'fields': ('ingredient', 'quantity', 'measurement_unit')}),
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'recipe')
    list_filter = ('recipe', 'create_at')
    search_fields = ('name',)


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.MeasurementUnit, MeasurementUnitAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.RecipeIngredients, RecipeIngredientsAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Info)
admin.site.register(models.NewsletterUser)
admin.site.register(models.Newsletter)

from django.contrib import admin

from .models import City, Genre, Author, Documentation


class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'type', 'status')
    list_filter = ('type', 'status')
    search_fields = ('name', 'author')
    list_per_page = 20
    ordering = ('name',)
    actions = ['make_available', 'make_unavailable']


admin.site.register(City)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Documentation, DocumentationAdmin)

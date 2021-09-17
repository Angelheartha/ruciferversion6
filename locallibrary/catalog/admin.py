from django.contrib import admin
from .models import Author, Genre, Book,BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author,AuthorAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    List_filter = ('status','due_bank')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        List_display = ('title', 'author', 'display_genre')


#admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)


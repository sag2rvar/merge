from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import Post, User, Category, Tag, Comment

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        
    export_as_csv.short_description = "Export Selected"

    list_display = ('name', 'text')
    list_filter = ['email'] 

@admin.register(Tag)
class ModelAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        
    export_as_csv.short_description = "Export Selected"

    list_filter = ['name']  


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        
    export_as_csv.short_description = "Export Selected"

    search_fields = ['username']
    list_filter = ['username']


@admin.register(Category)
class UserModelAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        
    export_as_csv.short_description = "Export Selected"

    search_fields = ['name']
    list_filter = ['name']



@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        
    export_as_csv.short_description = "Export Selected"
    list_display = ('title', 'author', 'text', 'created_date')
    search_fields = ['title']
    list_filter = ['title'] 
    autocomplete_fields = ['author', 'category']
    filter_horizontal = ['tags']



# Register your models here.

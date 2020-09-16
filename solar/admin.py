from django.contrib import admin
from solar.models import *
from django import forms


# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'alt', 'image']


admin.site.register(gallery, GalleryAdmin)


class Page_Admin(admin.ModelAdmin):
    list_display = ['title', 'active', 'to_menu']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'active', 'content', 'to_menu', 'image', 'show_image', 'file', 'file2', 'file3',
                       'video_url', 'page_gallery')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        })
    )


admin.site.register(pages, Page_Admin)


class Blog_Admin(admin.ModelAdmin):
    list_display = ['title', 'active', 'date']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'active', 'short_desc', 'desc', 'image')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        })
    )


admin.site.register(blog, Blog_Admin)


class Service_Admin(admin.ModelAdmin):
    list_display = ['title', 'active']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'active', 'short_desc', 'desc', 'image')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords')}
         )
    )


admin.site.register(service, Service_Admin)


class MainSlide_Admin(admin.ModelAdmin):
    exclude = ['sort']
    list_display = ['id', 'title']


admin.site.register(MainSlide, MainSlide_Admin)



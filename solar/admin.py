from django.contrib import admin
from solar.models import *
from django import forms


# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'alt', 'image']


admin.site.register(gallery, GalleryAdmin)


class Page_Admin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'active', 'to_menu']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'active', 'content', 'to_menu', 'image', 'show_image', 'file', 'file2', 'file3',
                       'video_url', 'page_gallery')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords',)
        })
    )


admin.site.register(pages, Page_Admin)


class Blog_Admin(admin.ModelAdmin):
    list_display = ['title', 'active', 'date']
    prepopulated_fields = {'slug': ('title',)}
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
    prepopulated_fields = {'slug': ('title',)}
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


class AboutAdmin(admin.ModelAdmin):
    fields = ['title', 'desc', 'image', 'icon1', 'icon2', 'icon3', 'icon4', 'number1', 'number2', 'number3',
              'number4',
              'text1', 'text2', 'text3', 'text4', 'baner_img', 'baner_title', 'baner_text', ]


admin.site.register(About, AboutAdmin)


class ContactAdmin(admin.ModelAdmin):
    fields = ['map', 'adress', 'phone1', 'phone2', 'email1', 'email2', 'adress_icon', 'phone_icon', 'email_icon']


admin.site.register(Contact, ContactAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'email', 'message']


admin.site.register(ContactMessage, ContactMessageAdmin)


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'active', 'slug', 'cod', 'pdf_file', 'image', 'desc1', 'short_desc', 'desc2', 'category',
              'related_products', 'show_home_block_1', 'show_home_block_2']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'active']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class FooterLinkAdmin(admin.ModelAdmin):
    fields = ['title', 'link']
    list_per_page = 1


admin.site.register(FotterLink, FooterLinkAdmin)

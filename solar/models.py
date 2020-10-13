from django.db import models
from django.shortcuts import reverse
from django.core.validators import FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField
import os


# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=65, null=True, unique=True, verbose_name='Change URL')
    short_desc = models.TextField(max_length=1500, verbose_name='Short Description')
    desc = RichTextUploadingField(blank=True, null=True, verbose_name='Description',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor/ckeditor/plugins/youtube/', 'plugin.js')])
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/blog', blank=True)
    sort = models.IntegerField(default=0)
    ACTIVE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    active = models.CharField(choices=ACTIVE_STATUS_CHOICES, max_length=1, default="1")
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.TextField(max_length=900, blank=True)
    seo_keywords = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail_url', kwargs={'slug': self.slug})

    def clean(self):
        self.slug = self.slug.lower()
        return super(blog, self).save()

    class Meta:
        ordering = ['-date']


class service(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=65, null=True, unique=True, verbose_name='Change URL')
    short_desc = models.TextField(max_length=1500, verbose_name='Short Description')
    desc = RichTextUploadingField(blank=True, null=True, verbose_name='Description',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor/ckeditor/plugins/youtube/', 'plugin.js')])
    image = models.ImageField(upload_to='media/service', blank=True)
    sort = models.ImageField(default=0)
    ACTIVE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    active = models.CharField(choices=ACTIVE_STATUS_CHOICES, max_length=1, default="1")
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.TextField(max_length=900, blank=True)
    seo_keywords = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail_url', kwargs={'slug': self.slug})

    def clean(self):
        self.slug = self.slug.lower()
        return super(service, self).save()

    class Meta:
        ordering = ['sort']


class gallery(models.Model):
    image = models.ImageField(upload_to='media\gallery')
    alt = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.image.name


class pages(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=65, unique=True, null=True, verbose_name='Change URL')
    image = models.ImageField(upload_to='media/pages', null=True, blank=True, verbose_name='Cover image')
    IMAGE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    show_image = models.CharField(max_length=1, choices=IMAGE_STATUS_CHOICES, default="1")
    content = RichTextUploadingField(blank=True, null=True,
                                     external_plugin_resources=[
                                         ('youtube', '/static/ckeditor/ckeditor/plugins/youtube/', 'plugin.js')])
    STATIC_PAGE_CHOICES = (('contact', 'contact'), ('blog', 'blog'), ('null', 'null'))
    static = models.CharField(max_length=25, choices=STATIC_PAGE_CHOICES, default='null')
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.TextField(max_length=900, blank=True)
    seo_keywords = models.CharField(max_length=500, blank=True)
    ACTIVE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    active = models.CharField(choices=ACTIVE_STATUS_CHOICES, max_length=1, default="1")
    TO_MENU_STATUS_CHOICES = (("0", 'Dont show'), ("1", 'Show'))
    to_menu = models.CharField(choices=TO_MENU_STATUS_CHOICES, max_length=1, default="1", verbose_name='Show to menu')
    sort = models.IntegerField(default=0)
    file = models.FileField(upload_to='media/pages/files', validators=[FileExtensionValidator(['pdf', 'rtf', 'xlsx'])],
                            null=True, blank=True, verbose_name='Attach file')
    file2 = models.FileField(upload_to='media/pages/files', validators=[FileExtensionValidator(['pdf', 'rtf', 'xlsx'])],
                             null=True, blank=True, verbose_name='Attach file')
    file3 = models.FileField(upload_to='media/pages/files', validators=[FileExtensionValidator(['pdf', 'rtf', 'xlsx'])],
                             null=True, blank=True, verbose_name='Attach file')
    video_url = models.SlugField(max_length=250, verbose_name='YouTube Video ID', null=True, blank=True)
    page_gallery = models.ManyToManyField(gallery, blank=True)

    def file_extension(self):
        extension = os.path.splitext(self.file.name)[1]
        if extension == '.pdf':
            return 'icon_pdf'
        if extension == '.rtf':
            return 'icon_rtf'
        if extension == '.xlsx':
            return 'icon_xlsx'

    def file_extension2(self):
        extension = os.path.splitext(self.file2.name)[1]
        if extension == '.pdf':
            return 'icon_pdf'
        if extension == '.rtf':
            return 'icon_rtf'
        if extension == '.xlsx':
            return 'icon_xlsx'

    def file_extension3(self):
        extension = os.path.splitext(self.file3.name)[1]
        if extension == '.pdf':
            return 'icon_pdf'
        if extension == '.rtf':
            return 'icon_rtf'
        if extension == '.xlsx':
            return 'icon_xlsx'

    def get_absolute_url(self):
        return reverse('page_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def clean(self):
        self.slug = self.slug.lower()
        return super(pages, self).save()

    class Meta:
        ordering = ['sort']


class MainSlide(models.Model):
    ACTIVE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    active = models.CharField(choices=ACTIVE_STATUS_CHOICES, max_length=1, default="1")
    image = models.ImageField(upload_to='media/slides')
    alt = models.CharField(max_length=150, blank=True)
    img_title = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=200, blank=True)
    btn_link = models.URLField(blank=True)
    btn_title = models.CharField(max_length=100, blank=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort']


class About(models.Model):
    title = models.CharField(max_length=800)
    desc = RichTextUploadingField(blank=True, null=True, verbose_name='Description',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor/ckeditor/plugins/youtube/', 'plugin.js')])
    image = models.ImageField(upload_to='media/pages')
    icon1 = models.ImageField(upload_to='media/pages', blank=True)
    icon2 = models.ImageField(upload_to='media/pages', blank=True)
    icon3 = models.ImageField(upload_to='media/pages', blank=True)
    icon4 = models.ImageField(upload_to='media/pages', blank=True)
    number1 = models.CharField(max_length=50, blank=True)
    number2 = models.CharField(max_length=50, blank=True)
    number3 = models.CharField(max_length=50, blank=True)
    number4 = models.CharField(max_length=50, blank=True)
    text1 = models.CharField(max_length=100, blank=True)
    text2 = models.CharField(max_length=100, blank=True)
    text3 = models.CharField(max_length=100, blank=True)
    text4 = models.CharField(max_length=100, blank=True)
    baner_img = models.ImageField(upload_to='media/pages', blank=True)
    baner_title = models.CharField(max_length=200, blank=True)
    baner_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    map = models.URLField(verbose_name='Google map link', blank=True, null=True, max_length=1000)
    adress = models.CharField(max_length=250)
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    email1 = models.EmailField(max_length=200, blank=True)
    email2 = models.EmailField(max_length=200, blank=True)
    adress_icon = models.ImageField(upload_to='media/pages', null=True)
    phone_icon = models.ImageField(upload_to='media/pages', null=True)
    email_icon = models.ImageField(upload_to='media/pages', null=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1500)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, null=True, verbose_name='Change URL')
    ACTIVE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    active = models.CharField(choices=ACTIVE_STATUS_CHOICES, max_length=1, default="1")

    def get_absolute_url(self):
        return reverse('product_list_url', kwargs={'category_slug': self.slug})

    def clean(self):
        self.slug = self.slug.lower()
        return super(Category, self).save()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, null=True, verbose_name='Change URL')
    cod = models.IntegerField()
    pdf_file = models.FileField(upload_to='media/products/file', validators=[FileExtensionValidator(['pdf'])],
                                null=True,
                                blank=True, verbose_name='Attach PDF file')
    image = models.ImageField(upload_to='media/products')
    desc1 = RichTextUploadingField(null=True, blank=True, verbose_name='Description',
                                   external_plugin_resources=[
                                       ('youtube', '/static/ckeditor/ckeditor/plugins/youtube/', 'plugin.js')])
    short_desc = models.TextField(null=True, blank=True, verbose_name='Short description')
    desc2 = RichTextUploadingField(null=True, blank=True, verbose_name='Propertis',
                                   external_plugin_resources=[
                                       ('youtube', '/static/ckeditor/ckeditor/plugins/youtube/', 'plugin.js')])
    ACTIVE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    active = models.CharField(choices=ACTIVE_STATUS_CHOICES, max_length=1, default="1")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    related_products = models.ManyToManyField('self', blank=True)
    SHOW_HOME_1_CHOICES = (("0", 'Dont show'), ("1", 'Show'))
    SHOW_HOME_2_CHOICES = (("0", 'Dont show'), ("1", 'Show'))
    show_home_block_1 = models.CharField(choices=SHOW_HOME_1_CHOICES, max_length=1, default="1")
    show_home_block_2 = models.CharField(choices=SHOW_HOME_1_CHOICES, max_length=1, default="1")

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})

    def clean(self):
        self.slug = self.slug.lower()
        return super(Product, self).save()

    def __str__(self):
        return self.name


class FotterLink(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.title

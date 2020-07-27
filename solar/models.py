from django.db import models
from django.shortcuts import reverse

# Create your models here.
class pages(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=65, unique=True, null=True, verbose_name='Change URL')
    image = models.ImageField(upload_to='media/pages', null=True, blank=True, verbose_name='Cover image')
    IMAGE_STATUS_CHOICES = (("0", 'Disabled'), ("1", 'Active'))
    show_image = models.CharField(max_length=1, choices=IMAGE_STATUS_CHOICES, default="1")
    content = models.TextField(blank=True)
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
    # file = models.FileField()



    def get_absolute_url(self):
        return reverse('page_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def clean(self):
        self.slug = self.slug.lower()
        return super(pages, self).save()

    class Meta:
        ordering = ['sort']


class blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=65, null=True, unique=True, verbose_name='Change URL')
    short_desc = models.TextField(max_length=1500, verbose_name='Short Description')
    desc = models.TextField(verbose_name='Description')
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
        ordering = ['sort']


class service(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=65, null=True, unique=True, verbose_name='Change URL')
    short_desc = models.TextField(max_length=1500, verbose_name='Short Description')
    desc = models.TextField(verbose_name='Description')
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

from django.shortcuts import render, get_object_or_404
from django.views import View
from solar.models import *
from solar.forms import *
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.utils.translation import gettext as _


# Create your views here.

def index(request):
    page_list = pages.objects.filter(active="1", to_menu="1")
    home_slides = MainSlide.objects.filter(active="1")
    home_blogs = blog.objects.filter(active="1")[:4]
    home_services = service.objects.filter(active="1")[:8]
    home_about = About.objects.get(id=1)
    categorys = Category.objects.filter(active="1")
    home_products_block1 = Product.objects.filter(active="1", show_home_block_1="1")
    home_products_block2 = Product.objects.filter(active="1", show_home_block_2="1")
    home_contact = Contact.objects.get(id=1)
    footer_links = FotterLink.objects.all()
    return render(request, 'solar/index.html',
                  context={'page_list': page_list, 'home_slides': home_slides, 'home_blogs': home_blogs,
                           'home_services': home_services, 'home_about': home_about, 'categorys': categorys,
                           'home_products_block1': home_products_block1, 'home_products_block2': home_products_block2,
                           'home_contact': home_contact, 'footer_links': footer_links})


def ststic_page_url(static):
    try:
        page = get_object_or_404(pages, active="1", static=static)
        return str(page.slug)
    except:
        return "test_migrations_url"


def get_404_page(request, page, page_list, categorys):
    response = render(request, 'solar/404.html', context={'page_list': page_list, 'page': page, 'categorys': categorys})
    response.status_code = 404
    return response


def blog_detail(request, slug):
    blog_item = get_object_or_404(blog, active="1", slug__iexact=slug)
    other_blogs = blog.objects.filter(active="1").exclude(title=blog_item.title)[:8]
    page_list = pages.objects.filter(active="1", to_menu="1")
    page = pages.objects.get(static='blog')
    categorys = Category.objects.filter(active="1")
    return render(request, 'solar/blog_detail.html',
                  context={'blog_item': blog_item, 'page_list': page_list, 'page': page, 'other_blogs': other_blogs,
                           'categorys': categorys})


def service_detail(request, slug):
    service_item = get_object_or_404(service, slug__iexact=slug, active="1")
    other_services = service.objects.filter(active="1").exclude(title=service_item.title)[:8]
    page_list = pages.objects.filter(active="1", to_menu="1")
    page = pages.objects.get(static='service')
    categorys = Category.objects.filter(active="1")
    return render(request, 'solar/service_detail.html',
                  context={'service_item': service_item, 'page_list': page_list, 'page': page,
                           'other_services': other_services, 'categorys': categorys})


def product_list(request, category_slug):
    page_list = pages.objects.filter(active="1", to_menu="1")
    page = pages.objects.get(static='products')
    category = get_object_or_404(Category, slug__iexact=category_slug, active="1")
    categorys = Category.objects.filter(active="1")
    all_products = category.products.filter(active="1")
    paginator = Paginator(all_products, 2)
    page_number = request.GET.get('page', 1)
    products = paginator.get_page(page_number)
    return render(request, 'solar/product_list.html',
                  context={'page_list': page_list, 'page': page, 'category': category, 'products': products,
                           'categorys': categorys})


def product_deatil(request, category_slug, product_slug):
    page_list = pages.objects.filter(active="1", to_menu="1")
    page = pages.objects.get(static='products')
    category = get_object_or_404(Category, slug__iexact=category_slug, active="1")
    product = get_object_or_404(Product, slug__iexact=product_slug)
    related_products = product.related_products.filter(active="1")
    categorys = Category.objects.filter(active="1")
    return render(request, 'solar/product_detail.html',
                  context={'page_list': page_list, 'page': page, 'category': category, 'product': product,
                           'related_products': related_products, 'categorys': categorys})


class Blog:
    def blog_controller(self, request, page, page_list, categorys):
        blogs = blog.objects.filter(active="1")
        return render(request, 'solar/' + page.static + '.html',
                      context={'blogs': blogs, 'page': page, 'page_list': page_list, 'categorys': categorys})


class Service:
    def service_controller(self, request, page, page_list, categorys):
        services = service.objects.filter(active=1)
        return render(request, 'solar/' + page.static + '.html',
                      context={'services': services, 'page': page, 'page_list': page_list, 'categorys': categorys})


class InfoPage:
    def about_controller(self, request, page, page_list, categorys):
        about_content = get_object_or_404(About, id=1)
        return render(request, 'solar/' + page.static + '.html',
                      context={'page': page, 'about_content': about_content, 'page_list': page_list,
                               'categorys': categorys})

    def contact_controller(self, request, page, page_list, categorys):
        contact_content = get_object_or_404(Contact, id=1)
        contact_form = ContactForm()
        if request.method == 'POST':
            new_contact_message = ContactForm(request.POST)
            if new_contact_message.is_valid():
                new_contact_message.save()
                message = "\n".join("{}\t{}".format(k, v) for k, v in new_contact_message.cleaned_data.items())
                try:
                    send_mail('That’s your subject',
                              message,
                              'aa748dff3f9438',
                              ['narek19.96@mail.ru'],
                              fail_silently=False, )
                    send_status = _('Succsess')
                    return render(request, 'solar/' + page.static + '.html',
                                  context={'page': page, 'contact_content': contact_content, 'page_list': page_list,
                                           'contact_form': contact_form, 'send_status': send_status,
                                           'categorys': categorys})
                except BadHeaderError:
                    send_status = _('Something went wrong')
                    return render(request, 'solar/' + page.static + '.html',
                                  context={'page': page, 'contact_content': contact_content, 'page_list': page_list,
                                           'contact_form': contact_form, 'send_status': send_status,
                                           'categorys': categorys})

            else:
                return render(request, 'solar/' + page.static + '.html',
                              context={'page': page, 'contact_content': contact_content, 'page_list': page_list,
                                       'contact_form': contact_form, 'new_contact_message': new_contact_message,
                                       'categorys': categorys})
        else:
            return render(request, 'solar/' + page.static + '.html',
                          context={'page': page, 'contact_content': contact_content, 'page_list': page_list,
                                   'contact_form': contact_form, 'categorys': categorys})


class Static_Page(Blog, Service, InfoPage):
    def render_static_page(self, request, page):
        page_list = pages.objects.filter(active="1", to_menu="1")
        categorys = Category.objects.filter(active="1")
        return getattr(self, page.static + '_controller', get_404_page)(request, page, page_list, categorys)


class Dynamic_Page:
    def render_dynamic_page(self, request, page):
        import os
        file_name = os.path.split(page.file.name)[1]
        file_name2 = os.path.split(page.file2.name)[1]
        file_name3 = os.path.split(page.file3.name)[1]
        page_gallery = page.page_gallery.all()
        page_list = pages.objects.filter(active="1", to_menu="1")
        categorys = Category.objects.filter(active="1")
        return render(request, 'solar/dynamic_page.html',
                      context={'page': page, 'page_list': page_list, 'file_name': file_name, 'file_name2': file_name2,
                               'file_name3': file_name3, 'page_gallery': page_gallery, 'categorys': categorys})


class Page_Controller(View, Dynamic_Page, Static_Page):
    def get(self, request, slug):
        page = get_object_or_404(pages, slug__iexact=slug, active="1")
        if page.static == "null":
            return self.render_dynamic_page(request, page)
        else:
            return self.render_static_page(request, page)

    def post(self, request, slug):
        page = get_object_or_404(pages, slug__iexact=slug, active="1")
        return self.render_static_page(request, page)

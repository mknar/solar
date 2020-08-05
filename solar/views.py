from django.shortcuts import render, get_object_or_404
from django.views import View
from solar.models import *



# Create your views here.

def index(request):
    page_list = pages.objects.filter(active="1", to_menu="1")
    return render(request, 'solar/index.html', context={'page_list': page_list})


def ststic_page_url(static):
    page = get_object_or_404(pages, active="1", static=static)
    return str(page.slug)


def get_404_page(request, page, page_list):
    response = render(request, 'solar/404.html', context={'page_list': page_list, 'page': page})
    response.status_code = 404
    return response


def blog_detail(request, slug):
    blog_item = get_object_or_404(blog, active="1", slug__iexact=slug)
    page_list = pages.objects.filter(active="1", to_menu="1")
    page = pages.objects.get(static='blog')
    return render(request, 'solar/blog_detail.html',
                  context={'blog_item': blog_item, 'page_list': page_list, 'page': page})


def service_detail(request, slug):
    service_item=get_object_or_404(service, slug__iexact=slug, active="1")
    page_list=pages.objects.filter(active="1", to_menu="1")
    page=pages.objects.get(static='service')
    return render(request, 'solar/service_detail.html', context={'service_item': service_item, 'page_list': page_list, 'page': page})

class Blog:
    def blog_controller(self, request, page, page_list):
        blogs = blog.objects.filter(active="1")
        return render(request, 'solar/' + page.static + '.html',
                      context={'blogs': blogs, 'page': page, 'page_list': page_list})


class Service:
    def service_controller(self, request, page, page_list):
        services = service.objects.filter(active=1)
        return render(request, 'solar/' + page.static + '.html',
                      context={'services': services, 'page': page, 'page_list': page_list})


class Static_Page(Blog, Service):
    def render_static_page(self, request, page):
        page_list = pages.objects.filter(active="1", to_menu="1")
        return getattr(self, page.static + '_controller', get_404_page)(request, page, page_list)


class Dynamic_Page:
    def render_dynamic_page(self, request, page):
        page_list = pages.objects.filter(active="1", to_menu="1")
        return render(request, 'solar/dynamic_page.html', context={'page': page, 'page_list': page_list})


class Page_Controller(View, Dynamic_Page, Static_Page):
    def get(self, request, slug):
        page = get_object_or_404(pages, slug__iexact=slug, active="1")
        if page.static == "null":
            return self.render_dynamic_page(request, page)
        else:
            return self.render_static_page(request, page)

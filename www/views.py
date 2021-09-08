# Create your views here.
from www.models import ContactForm, Contacts
from django.shortcuts import render
from www.mailer import contactmailnotify
from django.template import RequestContext
from django.template import Context, loader
from pprint import pprint
from django.http import HttpResponse
import json
from django.shortcuts import redirect
from www.blog_grab import blog_text_grab

def index(request):

    blog_post_dict = blog_text_grab()

    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        if form.is_valid():
            u = form.cleaned_data
            u['ip'] = ip
            p = Contacts(name=u['name'], email=u['email'], message=u['message'], ip_address=ip)
            p.save()
            context = {}
            x = contactmailnotify(u)
            if x:
                #html = render(request, 'admin/thanks.html', context)
                html = redirect('/thanks')
            else:
                #html = render(request, 'admin/error.html', context)
                html = redirect('/error')
            return html
    else:
        form = ContactForm()

    context = {'form': ContactForm, 'blog_post_dict': blog_post_dict}

    # print("form errors : {0}, {1}").format(form.name.errors, form.email.errors)
    html = render(request, 'admin/index.html', context)

    return html

def service_definition_plain(request):

    context = {}
    html = render(request, 'admin/scratch.html', context)
    return html

def privacy(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/privacy.html', context)
    return html

def service_definition(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/service-definition.html', context)
    return html

def pentest(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/pentest-profile.html', context)
    return html

def thanks(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/thanks.html', context)
    return html

def error(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/error.html', context)
    return html

def services(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/services.html', context)
    return html

def software(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/software.html', context)
    return html

def handler404(request, exception):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/404.html', context, status=404)
    return html

def handler500(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/500.html', context, status=500)
    return html

def secdeng(request):

    blog_post_dict = blog_text_grab()
    context = {'blog_post_dict': blog_post_dict}
    html = render(request, 'admin/security_de_engineering.html', context)
    return html

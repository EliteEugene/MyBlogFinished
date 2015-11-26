import json

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.core.mail import mail_admins
from django.core.mail import send_mail
from contact.forms import ContactForm
# Create your views here.

def contact_form(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():

            message = """From: %s <%s>\r\nMessage:\r\n%s\r\n""" % (
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )
            mail_admins('Contact form', message)

            # Only executed with jQuery form request
            if request.is_ajax():
                return HttpResponse('thanks')
            else:
                # render() a form with data (No AJAX)
                # redirect to results ok, or similar may go here
                pass
        else:
            if request.is_ajax():
                # Prepare JSON for parsing
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        er = form.errors[error]
                        errors_dict[error] = unicode(er)

                return HttpResponseBadRequest(json.dumps(errors_dict))
            else:
                # render() form with errors (No AJAX)
                pass
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form':form})



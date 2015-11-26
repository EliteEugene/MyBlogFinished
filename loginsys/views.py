from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm


'''

class LogIn(FormView):
    form_class = LogInForm
    template_name = 'login.html'

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user:
            login(self.request, user)
        return HttpResponseRedirect('/')

class AjaxValidation(FormView):
    form_dict = {
        'login' : LogInForm,
    }

    def get(self, request, *args, **kwrgs):
        return HttpResponseRedirect('/')

    def form_invalid(self, form):
        data = {}
        for k, v in form._errors.iteritems():
            text = {
                'desc' : ', '.join(v),
            }
            if k == '__all__':
                text['key'] = '#%s' % self.request.POST.get('form')
            else:
                text['key'] = '#id_%s' % k
            data.append(text)
        return HttpResponse(json.dumps(data))

    def form_valid(self, form):
        return HttpResponse("thanks")

    def get_form_class(self):
        return self.form_dict[self.reauest.POST.get('form')]

'''


def login(request):
    args ={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    args ={}
    args.update(csrf(request))
    if request.method == "POST":
        username = request.POST.get('username', '')
        password1= request.POST.get('password1', '')
        password2= request.POST.get('password2', '')
        user = auth.authenticate(username=username, password=password2)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
        else:
            user_db = User.objects.create_user(username=username, password=password2)
            user_db.save()
            user_auth = auth.authenticate(username=username, password=password2)
            auth.login(request, user_auth)
            return redirect('/')
    else:
        return render_to_response('register.html', args)

from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from  django.core.urlresolvers import reverse_lazy


@login_required(login_url=reverse_lazy('login_user'))
def index(request):
    return render_to_response('index.html', {}, context_instance = RequestContext(request))


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))
    return render_to_response('login.html', context_instance=RequestContext(request))

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login_user'))
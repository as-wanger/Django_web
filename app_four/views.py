from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import get_template

from app_four import models, forms


# Create your views here.
def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        try:
            user = models.User.objects.get(username=username)
            diaries = models.Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass
    messages.get_messages(request)

    template = get_template('app_four/index.html')
    request_context = RequestContext(request, {})
    request_context.push(locals())
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            userinfo = models.Profile.objects.get(user=user)
        except:
            pass
    template = get_template('app_four/userinfo.html')
    html = template.render(locals())
    return HttpResponse(html)


def login(request):
    if request.user.is_authenticated:
        return redirect('/app_four/')
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/app_four/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
    else:
        login_form = forms.LoginForm()

    template = get_template('app_four/login.html')
    request_context = RequestContext(request, {})
    request_context.push(locals())
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出了")
    return redirect('/app_four/')


@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)

    if request.method == 'POST':
        user = User.objects.get(username=username)
        diary = models.Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "日記已儲存")
            post_form.save()
            return HttpResponseRedirect('/app_four/')
        else:
            messages.add_message(request, messages.INFO, '要張貼日記，每一個欄位都要填...')
    else:
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.INFO, '要張貼日記，每一個欄位都要填...')

    template = get_template('app_four/posting.html')
    request_context = RequestContext(request, {})
    request_context.push(locals())
    html = template.render(context=locals(), request=request)

    return HttpResponse(html)
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import get_template

from app_six import models, forms


# Create your views here.
def index(request):
    today = datetime.datetime.today()
    all_polls = models.Poll.objects.all().order_by('-created_at')
    paginator = Paginator(all_polls, 5)
    p = request.GET.get('p')
    try:
        polls = paginator.page(p)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)
    template = get_template('app_six/index.html')
    request_context = RequestContext(request, {})
    request_context.push(locals())
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


@login_required
def addpollitem(request, pollid=''):
    if request.method == 'POST':
        pollid = request.POST['pollid']
        poll = models.Poll.objects.get(id=pollid)
        new_pollitem = models.PollItem(poll=poll)
        form = forms.PollItemForm(request.POST, instance=new_pollitem)
        if form.is_valid():

            form.save()
            return redirect('app_six/addpollitem/'+pollid)
    else:
        form = forms.PollItemForm()

    poll = models.Poll.objects.get(id=pollid)
    pollitems = models.PollItem.objects.filter(poll=poll)
    template = get_template('app_six/addpollitem.html')
    request_context = RequestContext(request, {})
    request_context.push(locals())
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


@login_required
def addpoll(request):
    if request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        new_poll = models.Poll(user=user)
        form = forms.PollForm(request.POST, instance=new_poll)
        if form.is_valid():

            form.save()
            return redirect('/app_six/addpoll')
    else:
        form = forms.PollForm()

    username = request.user.username
    user = User.objects.get(username=username)
    polls = models.Poll.objects.filter(user=user)
    template = get_template('app_six/addpoll.html')
    request_context = RequestContext(request, {})
    request_context.push(locals())
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


@login_required
def poll(request, pollid):
    try:
        poll = models.Poll.objects.get(id=pollid)
    except:
        poll = None
    if poll is not None:
        pollitems = models.PollItem.objects.filter(poll=poll).order_by('-vote')
    template = get_template('app_six/poll.html')
    request_context = RequestContext(request, {})
    request_context.push(locals())
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


@login_required
def vote(request, pollid, pollitemid):
    target_url = '/app_six/poll/' + pollid
    if models.VoteCheck.objects.filter(userid=request.user.id, pollid=pollid,
                                    vote_date=datetime.date.today()):
        messages.add_message(request, messages.WARNING, '您已經投過票了！')
        return redirect(target_url)
    else:
        vote_rec = models.VoteCheck(userid=request.user.id, pollid=pollid,
                                    vote_date=datetime.date.today())
        vote_rec.save()
        messages.add_message(request, messages.WARNING, '投票成功！')
    try:
        pollitem = models.PollItem.objects.get(id=pollitemid)
    except:
        pollitem = None
    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()
    return redirect(target_url)


@login_required
def govote(request):
    if request.method == "GET" and request.is_ajax():
        pollitemid = request.GET.get('pollitemid')
        pollid = request.GET.get('pollid')
        bypass = False
        if models.VoteCheck.objects.filter(userid=request.user.id, pollid=pollid,
                                        vote_date=datetime.date.today()):
            bypass = True
        else:
            vote_rec = models.VoteCheck(userid=request.user.id, pollid=pollid,
                                        vote_date=datetime.date.today())
            vote_rec.save()

        try:
            pollitem = models.PollItem.objects.get(id=pollitemid)
            if not bypass:
                pollitem.vote = pollitem.vote + 1
                pollitem.save()
            votes = pollitem.vote
        except:
            votes = 0
    else:
        votes = 0
    return HttpResponse(votes)


@login_required
def delpoll(request, pollid):
    try:
        poll = models.Poll.objects.get(id=pollid)
    except:
        pass
    if poll is not None:
        poll.delete()
    target_url = '/app_six/addpoll/'
    return redirect(target_url)


@login_required
def delpollitem(request, pollid, pollitemid):
    try:
        pollitem = models.PollItem.objects.get(id=pollitemid)
    except:
        pass
    if pollitem is not None:
        pollitem.delete()
    target_url = '/app_six/addpollitem/' + pollid
    return redirect(target_url)
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from fdp.models import Message


@login_required
def index(request):
    quantity = Message.objects.count()
    last_ten_messages_index = 0 if quantity < 10 else quantity - 10
    last_ten_messages = reversed(Message.objects.all()[last_ten_messages_index:])
    context = {'messages_list': last_ten_messages}
    return render(request, 'index.html', context)


@login_required
def message_sent(request):
    text = request.GET['text']
    sender = request.GET['sender']
    m = Message(text=text, sender=sender)
    m.save()
    return HttpResponse('message received', content_type='application/text')


@login_required
def history(request):
    quantity = Message.objects.count()
    i = 0 if quantity < 50 else quantity - 50
    last_messages = Message.objects.all()[i:]
    messages = '\n'.join([str(m) for m in last_messages])
    return HttpResponse(messages, content_type='application/text')


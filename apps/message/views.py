# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import UserMessage

# Create your views here.


def getform(request):
    # all_message = UserMeåssage.objects.all() # 将数据库中的所有变量返回给我们
    # for message in all_message:
    #     print message.name

    # all_messages = UserMessage.objects.filter(name="bobby", address="北京")
    # # all_messages.delete()
    # for message in all_messages:
    #     message.delete()

    message = None
    all_messages = UserMessage.objects.filter(name="bobby")
    if all_messages:
        message = all_messages[0]

    # if request.method == "POST":
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworld3"
    #     user_message.save()

    return render(request, 'message_form.html', {
        "my_message": message
    })

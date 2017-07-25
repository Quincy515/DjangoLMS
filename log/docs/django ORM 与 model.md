```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserMessage(models.Model):
    # djangohui会自动生成ID作为主键  
    # object_id = models.CharField(max_length=50, default="", primary_key=True, verbose_name=u"主键")
    name = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    models.ForeignKey
    models.DateField
    models.DateTimeField
    models.IntegerField
    models.IPAddressField
    models.FileField
    models.ImageField

    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name
        db_table = "user_message"
        ordering = "-object_id"

```

Model 的增删改查

```python
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

```
from django.shortcuts import HttpResponse
from django.shortcuts import render
from cmdb import models

# Create your views here.

#创建了一个用户信息列表，预定义了两个数据，它将被返回给浏览器展示给用户
# user_list=[
#     {"user":"jack","pwd":"abc"},
#     {"user":"tom","pwd":"ABC"},
# ]

def index(request):
    #request参数必须有，名字是类似self的默认规则，可以改。它封装了用户请求的所有内容。
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()

    return render(request,"index.html",{"data":user_list})

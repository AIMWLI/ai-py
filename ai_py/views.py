from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")


from django.shortcuts import render


def hello2(request):
    context = {}
    context['iamcontext'] = 'Hello World!'
    return render(request, 'helloworld2.html', context)


def hello3(request):
    # view：｛"HTML变量名": "views变量名"｝
    # HTML：｛｛变量名｝｝
    views_name = "菜鸟教程"
    return render(request, "helloworld3.html", {"name": views_name})


def hello4(request):
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "helloworld4.html", {"views_list": views_list})


def hello5(request):
    views_dict = {"name": "菜鸟教程"}
    return render(request, "helloworld5.html", {"views_dict": views_dict})

def hello6(request):
    import datetime
    now = datetime.datetime.now()
    # return render(request, "helloworld6.html", {"time": now})
    # views_str = "<a href='https://www.baidu.com/'>点击跳转</a>"
    # return render(request, "helloworld6.html", {"views_str": views_str})
    # views_num = 40
    # return render(request, "helloworld6.html", {"num": views_num})
    # views_list = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3",]
    # return render(request, "helloworld6.html", {"views_list": views_list})
    views_dict = {"name": "sj", "age": 18}
    return render(request, "helloworld6.html", {"views_dict": views_dict})


def mycal(request):
    if request.method == "GET":
        return render(request, "mycal.html")
    elif request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op == 'add':
            result = x + y
        if op == 'sub':
            result = x - y
        if op == 'mul':
            result = x * y
        if op == 'div':
            result = x / y
        return render(request, "mycal.html", locals())
    return None
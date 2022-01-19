from django.http import HttpResponse

from ai_py import models
from ai_py.models import Test


def test(request):
    dto = Test(name="asdf")
    dto.save()
    objs = [Test(name="1"),
            Test(name="2"),
            Test(name="2"),
            Test(name="2"),
            Test(name="3")]
    models.Test.objects.bulk_create(objs, 10)
    return HttpResponse("ok")

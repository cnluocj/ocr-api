# coding:utf-8


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import StringIO


def index(request):
    HttpResponse('hello world !')
#     return render_to_response('index.html', {}, context_instance=RequestContext(request))


def upload(request):
    img = request.FILES['image']

    if img:
        img_buf = StringIO.StringIO(img.read())
        result = pytesseract.image_to_string(Image.open(img_buf), 'chi_sim')
        data = {'is_success': 1, 'result': result}
        return HttpResponse(json.dump(data), content_type='application/json')

    else:
        data = {'is_success': 0}
        return HttpResponse(json.dump(data), content_type='application/json')

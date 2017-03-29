# coding:utf-8


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.views.decorators.csrf import csrf_exempt


try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import StringIO


def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def hello(request):
    return HttpResponse('hello world !')

@csrf_exempt
def upload(request):
    img = request.FILES['image']

    if img:
        img_buf = StringIO.StringIO(img.read())
        result = pytesseract.image_to_string(Image.open(img_buf), 'chi_sim')
        data = {'is_success': 1, 'result': result}
        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        data = {'is_success': 0}
        return HttpResponse(json.dumps(data), content_type='application/json')

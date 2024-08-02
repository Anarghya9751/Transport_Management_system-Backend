from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import json


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return result

def my_view(request):
    data = {
        "title": "Sample PDF",
        "items": [{"name": "Item 1", "price": 10}, {"name": "Item 2", "price": 20}]
    }
    # Convert JSON data to Python dictionary
    context = json.loads(json.dumps(data))
    return render_to_pdf('pdf/welcome.html', context)

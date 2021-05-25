from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# Create your views here.
def test(request):
    context = {
        'firstname': _('first name')
    }
    return render(request, 'test/index.html', context)


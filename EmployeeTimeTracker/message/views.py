from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm
from .models import message
# Create your views here.


def home(request):
    form = MessageForm()
    message_list = message.objects.all().filter(user_id=request.user.id).order_by('-date_created')
    context = {'form': form, 'message_list': message_list}

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'message/index.html', context)


from .forms import FilterForm


def name_of_the_page(request):
    form = FilterForm(request.POST or None)
    answer = ''
    if form.is_valid():
        answer = form.cleaned_data.get('filter_by')
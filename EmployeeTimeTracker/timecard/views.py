from django.shortcuts import render, redirect
import csv
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime, timedelta, time
from .forms import DailyLogForm, MessageForm
from .models import DailyLog, MessageObject
from loginmanager.models import *
from .filters import ReportFilter
from django.utils.translation import gettext as _
from django.utils.timesince import timeuntil
from .decorators import allowed_users, admin_only


# Create your views here.


def timecard(request):
    global data
    checkin_check = DailyLog.objects.filter(user_id=request.user.id).last()
    if checkin_check == None:
        checkin_status = 0
        checkin_time = 'You have not checked In'
    else:
        data = DailyLog.objects.filter(user_id=request.user.id).last()
        pk_id = data.id
        checkin_status = data.status
        checkin_time = data.checkin_time
        checkin = DailyLog.objects.get(id=pk_id)

    name = request.user
    message_list = MessageObject.objects.all().order_by('-date_created_object')
    context = {'name': name,
               'checkin_status': checkin_status,
               'checkin_time': checkin_time,
               'message_list': message_list, }

    if request.method == 'POST':
        if 'checkin' in request.POST:
            form = DailyLogForm(request.POST)
            message_object = request.POST.get('select_object')
            print(message_object)
            if form.is_valid():
                form.save()
                chekin_last = DailyLog.objects.last()
                if message_object is not None:
                    chekin_last.message_object = message_object
                    chekin_last.save()
                return redirect('checkin')
                # return render(request, 'timecard/index.html', context)

        elif 'checkout' in request.POST:
            checkin.status = 0
            checkin.checkout_time = datetime.now()
            checkin.save()
            # form = DailyLogForm(instance=checkin)
            # form = DailyLogForm(request.POST, instance=checkin)
            # if form.is_valid():
            #     form.save(["checkout_message"])
            return redirect('checkin')
    # context['message_object'] = set_message_object(request)
    # print(context)

    return render(request, 'timecard/index.html', context)

    # return render(request, 'timecard/index.html')


@admin_only
def record(request):
    pk_id = request.user.id
    records = DailyLog.objects.all().filter(user_id=pk_id)
    time_work = timedelta(0)
    for record in records:
        time_work += record.checkout_time - record.checkin_time
    time_work_employee = []
    seconds = time_work.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    time_work_employee.append(hours)
    time_work_employee.append(minutes)
    context = {'records': records, 'time_work': time_work_employee}
    return render(request, 'timecard/record.html', context)


@admin_only
def allrecord(request):
    pk_id = request.user.id
    records = DailyLog.objects.all()
    time_work = timedelta(0)
    for record in records:
        time_work += record.checkout_time - record.checkin_time
    time_work_employee = []
    seconds = time_work.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    time_work_employee.append(hours)
    time_work_employee.append(minutes)
    context = {'records': records, 'time_work': time_work_employee}
    return render(request, 'timecard/allrecord.html', context)


@admin_only
def report(request):
    records = DailyLog.objects.all()
    myFilter = ReportFilter(request.GET, queryset=records)
    records = myFilter.qs
    context = {'records': records, 'myFilter': myFilter}
    return render(request, 'timecard/report.html', context)


@admin_only
def getreport(request):
    records = DailyLog.objects.all()
    myFilter = ReportFilter(request.GET, queryset=records)
    records = myFilter.qs
    time_work = timedelta(0)
    for record in records:
        time_work += record.checkout_time - record.checkin_time
    time_work_employee = []
    seconds = time_work.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    time_work_employee.append(hours)
    time_work_employee.append(minutes)
    context = {'records': records, 'myFilter': myFilter, 'time_work': time_work_employee}
    if request.method == 'GET':
        if 'download' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="file.csv"'
            writer = csv.writer(response)
            writer.writerow([_('Username'), _('CheckIn Time'), _('CheckOut Time'), _('Duration'), _('Payment')])
            writer.writerow([''])
            total = 0
            rate = 0
            for r in records:
                try:
                    rates = Profile.objects.get(user_id=r.user_id)
                    if rates.rate_per_hour == None:
                        rate = 0
                    else:
                        rate = rates.rate_per_hour
                except:
                    pass

                duration = r.checkout_time - r.checkin_time
                # payment = duration
                days, seconds = duration.days, duration.seconds
                hours = days * 24 + seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = seconds % 60
                payment = (hours * rate) + (minutes * rate / 60) + (seconds * rate / 3600)
                total = total + payment
                writer.writerow(
                    [r.user.username, r.checkin_time, r.checkout_time, r.message_object, duration,
                     payment])
                # writer.writerow([days, hours, minutes, seconds])
            writer.writerow([''])
            writer.writerow([_('Total'), time_work_employee[0], "hour", time_work_employee[1], "minutes."])
            return response
    return render(request, 'timecard/getreport.html', context)


@admin_only
def add_object(request):
    form = MessageForm()
    message_list = MessageObject.objects.all().order_by('-date_created_object')
    context = {'form': form, 'message_list': message_list}

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'timecard/add_object.html', context)

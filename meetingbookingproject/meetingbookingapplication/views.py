from django.shortcuts import render
from .models import meeting, staff, booking
from .forms import meetingform, staffform, bookingform
from django.http.response import HttpResponse


# def input(request):
# return render(request,'templates\meeting.html')


def meetingview(request):
    if request.method == 'POST':
        mform = meetingform(request.POST)
        if mform.is_valid():
            meetingid = request.post.get('meetingid', '')
            meetingroom = request.post.get('meetingroom', '')
            meetingdescription = request.post.get('meetingdescription', '')
            data = meeting(
                meetingid=meetingid,
                meetingroom=meetingroom,
                meetingdescription=meetingdescription)
            data.save()
            data1 = meeting.objects.filter(meetingid=meetingid)

            if data1:
                info = "room already was booked with this meeting id ,try with another meeting id"
                mform = meetingform()
                return render(request,'meeting.html',{'mform':mform,'info':info})
        info ="room was booked with this meeting id,please fill another u want to book another one"
        mform = meetingform()
        return render(request, 'meeting.html', {'mform': mform,'info':info})

    else:
        mform = meetingform()
        return render(request, 'meeting.html', {'mform': mform})


def staffview(request):
    if request.method == 'POST':
        sform = staffform(request.POST)
        if sform.is_valid():
            staffid = request.post.get('staffid', '')
            staffname = request.post.get('meetingroom', '')
            staffmail = request.post.get('meetingdescription', '')

        data = staff(
            staffid=staffid,
            staffname=staffname,
            staffmail=staffmail,
        )
        data.save()
        sform = staffform()
        return render(request, 'meeting.html', {'sform': sform})

    else:
        sform = staffform()
        return render(request, 'meeting.html', {'sform': sform})


def bookingview(request):
    if request.method == 'POST':
        bform = bookingform(request.POST)
        if bform.is_valid():
            meetingid = request.post.get('meetingid', '')
            staffid = request.post.get('staffid', '')
            bookindstartdate = request.post.get('bookingstartdate', '')
            bookingenddate = request.post.get('bookingenddate', '')
            data = meeting(meetingid=meetingid,staffid=staffid,bookingstartdate=bookindstartdate,bookingenddate=bookingenddate,)
            data.save()
        bform = bookingform()
        return render(request, 'meeting.html', {'bform': bform})

    else:
        bform = bookingform()
        return render(request, 'meeting.html', {'bform': bform})

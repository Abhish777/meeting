from django.db import models

class meeting(models.Model):
    meetingid=models.IntegerField()
    meetingroom=models.CharField(max_length=50)
    meetingdescription=models.TextField()


class staff(models.Model):
    staffid = models.IntegerField()
    staffname = models.CharField(max_length=50)
    staffmail = models.EmailField(max_length=50)


class booking(models.Model):
    mid = models.IntegerField()
    staffid = models.IntegerField()
    startdate=models.DateField()
    enddate=models.DateField()






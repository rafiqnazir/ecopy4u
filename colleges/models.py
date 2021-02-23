from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class colleges(models.Model):
    college_name = models.CharField(max_length=50,default="NIT Srinagar")
    branch = models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    year = models.CharField(max_length=20,default="2017")
    
    pdf = models.FileField(upload_to='colleges')
    contributor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    valid=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True,auto_now=False,null=True)

    class Meta:
        unique_together=['college_name','branch','subject','year']

    #when new board paper is created , where to redirect
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.college_name + ' - ' + str(self.branch) + ' - ' + str(self.subject) + '-'+ str(self.year) + ' - ' + '-' + str(self.valid) + ' ' + str(self.date)

    def save(self, *args, **kwargs):
        self.college_name = self.college_name.lower()
        self.branch = self.branch.lower()
        return super(colleges, self).save(*args, **kwargs)



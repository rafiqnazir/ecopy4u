from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class colleges(models.Model):
    type= [("minor", "Minor"), ("major", "Major")] 
    # Branch=[ 
    # ("Chemical Engineering" , "Chemical Engineering") ,
    # ("Civil Engineering" , "Civil Engineering") , 
    # ("Computer Science Engineering" , "Computer Science Engineering"),
    # ("Electrical Engineering" , "Electrical Engineering") ,
    # ("Electronics Engineering" , "Electronics Engineering"),
    # ("Mechanical Engineering" , "Mechanical Engineering"),
    # ("Metallurgical Engineering" , "Metallurgical Engineering"),
    # ("Information & Technology" , "Information & Technology")]
    college_name = models.CharField(max_length=50,default="NIT Srinagar")
    branch = models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    year = models.IntegerField(default=2020)
    exam=models.CharField(max_length=20,choices=type,default="major")
    # minor / major
    pdf = models.FileField(upload_to='colleges')
    contributor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    valid=models.BooleanField(default=False)

    class Meta:
        unique_together=['college_name','branch','subject','year','exam']

    #when new board paper is created , where to redirect
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.college_name + ' - ' + str(self.branch) + ' - ' + str(self.subject) + '-'+ str(self.year) + ' - ' + self.exam + '-' + str(self.valid)

    def save(self, *args, **kwargs):
        self.college_name = self.college_name.lower()
        self.branch = self.branch.lower()
        return super(colleges, self).save(*args, **kwargs)



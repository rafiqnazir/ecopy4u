from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class boards(models.Model):
    #choices=objects.value('board_name')
    
    board_name = models.CharField(max_length=50,default="JKBOSE")
    class_number=models.IntegerField()
    subject = models.CharField(max_length=50)
    year = models.IntegerField(default=2020)
    series= models.CharField(max_length=10)
    pdf = models.FileField(upload_to='pdf')
    contributor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    valid=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True,auto_now=False,null=True)

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=["board_name", "class_number","subject", "year","series"], name='unique board')]
    #when new board paper is created , where to redirect
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return  self.board_name + ' - ' + str(self.class_number) + ' - ' + self.subject + ' - ' + str(self.year) + ' - ' + str(self.valid) + ' ' + str(self.date)

    def save(self, *args, **kwargs):
        self.board_name = self.board_name.lower()
        self.subject = self.subject.lower()
        return super(boards, self).save(*args, **kwargs)



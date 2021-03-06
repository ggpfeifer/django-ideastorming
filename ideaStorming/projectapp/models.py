from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from authapp.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=30)
   
    def __str__(self):
        return self.tag

class Project(models.Model):
    INVESTMENT_OPTIONS = (
        ('< $100 USD', '< $100 USD'),
        ('$100 - $300 USD', '$100 - $300 USD'),
        ('$301 - $500 USD', '$301 - $500 USD'),
        ('$501 - $800 USD', '$501 - $800 USD'),
        ('$801 - $1000 USD', '$801 - $1000 USD'),
        ('> $1000 USD', '> $1000 USD'),
    )
    
    title = models.CharField(max_length=30) 
    summary = models.TextField()
    advantages = models.TextField()
    investment = models.CharField(max_length=100, choices=INVESTMENT_OPTIONS)
    date_creation =  models.DateTimeField(auto_now_add=True, blank=True) 
    date_last_modification =  models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    mark = models.DecimalField(max_digits=4, decimal_places=3,null=True)

    def __str__(self):
        return '%s' % self.title

    def get_url(self):
        url_title = self.title.replace(" ", "_").replace(".", "").replace(",", "")
        url_user = self.user.username.split('@')[0]
        return '%s/%s/%s'% (url_title,str(self.id),url_user)
     

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    comment = models.TextField()
    added_to_project = models.BooleanField(default=False)
    publication_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment
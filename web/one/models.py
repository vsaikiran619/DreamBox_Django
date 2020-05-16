from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class Categoryposts(models.Model):
    title           = models.CharField(max_length=200)
    img             = models.ImageField(upload_to = 'pics')
    category        = models.CharField(max_length=50,default="Technology")
    interview_procedure= models.TextField()
    about           = models.TextField(default="About Company")
    eligibility     = models.TextField(default="Eligibility criteria of company")
    skills          = models.TextField(default="skills required")
    questions       = models.TextField(default="frequently asked questions in the interview")
    date            = models.DateTimeField(auto_now_add=True)
    #comments_count = models.IntegerField()
    homepost        = models.BooleanField(default=False)
    blogpost        = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id':self.id
        })
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def get_interview(self):
        return self.interview.all()


class Comment(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)
    comment     = models.TextField()
    post        = models.ForeignKey(Categoryposts,related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Interview(models.Model):

    name                = models.CharField(max_length=50)
    company_name        = models.CharField(max_length=100)
    role                = models.CharField(max_length=100)
    qualification       = models.CharField(max_length=200)
    skills              = models.CharField(max_length=200)
    rounds              = models.TextField()
    interview_Experience= models.TextField()
    questions           = models.TextField()
    suggestions         = models.TextField()
    timestamp           = models.DateTimeField(auto_now_add=True)
    selected_year       = models.CharField(max_length=100, default="")
    package             = models.CharField(max_length=100, default="")
    select              = models.BooleanField(default=True)

    def get_original_url(self):
        return reverse('interviews-detail', kwargs={
            'id':self.id
        })
    
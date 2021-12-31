from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    head = models.CharField(max_length=500, default="")
    content = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    Banner_image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title


class Blog_image(models.Model):
    post = models.ForeignKey(Blogpost,default=None, on_delete=models.CASCADE)
    images =models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.post.title



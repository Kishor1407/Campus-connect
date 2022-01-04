from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content=RichTextUploadingField()
    title = models.CharField(max_length=50)
    pub_date = models.DateField(null=True)
    Banner_image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title



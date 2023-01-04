from django.db import models
from django.dispatch import receiver
from api.utils import thumbnail_image,large_image,medium_image,grayScale_image
from django.db.models.signals import post_save,pre_save
# Create your models here.



class ImagesPro(models.Model):
    image = models.ImageField(upload_to="images")
    thumbnial = models.ImageField(upload_to="images",blank=True)
    medium = models.ImageField(upload_to="images",blank=True)
    large = models.ImageField(upload_to="images",blank=True)
    grayscale = models.ImageField(upload_to="images",blank=True)







@receiver(pre_save, sender=ImagesPro)
def trying(sender,instance,**kwargs):
    tb = str(instance.image).split('.')
    t = thumbnail_image(instance.image)
    t.save(f'media/images/{tb[0]}_thumbnial.{tb[-1]}')
    m = medium_image(instance.image)
    m.save(f'media/images/{tb[0]}_medium.{tb[-1]}')
    l = large_image(instance.image)
    l.save(f'media/images/{tb[0]}_large.{tb[-1]}')
    gray  = grayScale_image(instance.image)
    gray.save(f'media/images/{tb[0]}_grayscale.{tb[-1]}')
    instance.large = f'images/{tb[0]}_large.{tb[-1]}'
    instance.medium = f'images/{tb[0]}_medium.{tb[-1]}'
    instance.thumbnial = f'images/{tb[0]}_thumbnial.{tb[-1]}'
    instance.grayscale = f'images/{tb[0]}_grayscale.{tb[-1]}'
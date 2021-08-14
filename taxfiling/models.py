from django.db import models
from django.utils.text import slugify

# Create your models here.

class TaxFiling(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=500,default='')
    tag_content = models.TextField(null=True,blank=True)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TaxFiling, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

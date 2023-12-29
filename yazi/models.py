from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from kategori.models import kategori

# Create your models here.

class Yazi(models.Model):
    başlık = models.CharField(max_length=120)
    metin = RichTextField()
    yayinTarihi = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE, related_name="yazilar")
    begeniSayisi = models.IntegerField(default=0)
    goruntulenmeSayisi = models.IntegerField(default=0)

    def __str__(self):
        return self.başlık

    def get_unique_slug(self):
        slug = slugify(self.başlık)
        unique_slug = slug
        counter = 1

        while Yazi.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()

        return super(Yazi, self).save(*args, **kwargs)

class Yorum(models.Model):
    yazi = models.ForeignKey(Yazi, on_delete=models.CASCADE, related_name="yorumlar")
    metin = models.TextField()
    yayinTarihi = models.DateTimeField(auto_now_add=True)

from django.db import models


class Type(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi


class Portfolio(models.Model):
    nomi = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    date = models.DateField()
    url = models.URLField()
    malumot = models.TextField()

    tur = models.ForeignKey(Type, on_delete=models.CASCADE)

    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media', null=True, blank=True)
    rasm3 = models.ImageField(upload_to='media', null=True, blank=True)

def __str__(self):
        return self.nomi


# Yangi: Xizmatlar (Services) modeli — sizning uslubingizda
class Service(models.Model):
    nomi = models.CharField(max_length=100)
    malumot = models.TextField()
    ikonka = models.CharField(max_length=100, default="bi bi-briefcase") # Bootstrap ikonkalar klassi uchun

    def __str__(self):
        return self.nomi


# Yangi: Xodimlar (Workers/Team) modeli — sizning uslubingizda
class Worker(models.Model):
    ism_familiya = models.CharField(max_length=100)
    lavozimi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='media')
    
    # Ijtimoiy tarmoqlar havolalari
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.ism_familiya
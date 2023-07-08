from django.db import models

class News(models.Model):
    immagine=models.ImageField()
    titolo=models.CharField(max_length=20, default=None)
    descrizione=models.TextField()
    firma= models.CharField(max_length=30, default=None)
    
    
    def __str__(self):
        return self.titolo
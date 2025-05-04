from django.db import models

class Strom(models.Model):
    jmeno = models.CharField(max_length=100)
    listy = models.TextField()
    plody = models.TextField()
    kura = models.TextField()
    tvar_koruny = models.TextField()
    drevo = models.TextField()
    rozpoznavaci_znaky = models.TextField()

    def __str__(self):
        return self.jmeno
    
class StromObrazek(models.Model):
    strom = models.ForeignKey(Strom, on_delete=models.CASCADE, related_name='obrazky')
    obrazek = models.ImageField(upload_to='stromy_obrazky/')

    def __str__(self):
        return f"Obrázek pro {self.strom.jmeno}"

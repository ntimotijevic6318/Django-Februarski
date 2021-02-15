from django.db import models

class Telefoni(models.Model):
    markaTelefona = models.TextField()
    modelTelefona = models.TextField()
    slikaTelefona = models.TextField()
    opisModela= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.markaTelefona



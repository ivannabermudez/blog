from django.db import models

#object oriented programming
# models are python classes that manages a underline database table

class Post(models.Model):   # example of inheritance by extending the models class
    title = models.CharField(max_length=128)     #multiple examples of composition-when u rely on aditional classes to build
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
#models class lives inside the models nodule

    def __str__(self):
        return self.title
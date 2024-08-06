from django.db import models



class Division(models.Model):
    #id = models.I(primary_key=True)
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=250)

    def __str__(self):
        return self.director


class User(models.Model):
    #id = models.IntField(primary_key=True)
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    login = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    division = models.ForeignKey(Division, on_delete=models.PROTECT)


    def __str__(self):
        return self.name
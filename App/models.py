from django.db import models

# Table with fk (foreign key)
class Career(models.Model):
    career = models.CharField(max_length=100)
    def __str__(self):
        return self.career

#table candidate
GENDER = (
    ('F','F'),
    ('M','M'),
    ('Others','Others')
)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,null=True,choices=GENDER)
    career = models.ForeignKey(Career,on_delete=models.CASCADE)
from django.db import models


class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default ="")
    date_of_birth = models.DateField()
    location = models.CharField(max_length=60)
    phone = models.CharField(max_length=14)
    place_of_work = models.CharField(max_length=60)
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=10)
    life_connect = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    specific_life_objective = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(f"{self.first_name}{self.last_name}")
        

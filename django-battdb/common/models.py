from django.db import models
from django.contrib.auth import get_user_model

# any model can inherit this one to add these columns
class BaseModel(models.Model):
   name =  models.CharField(max_length=100, unique=True)
   owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
   created_on = models.DateField(auto_now_add=True)
   accepted = models.BooleanField(default=False)
   class Meta:
      abstract=True  # this tells Django not to create a table for this model - it's an abstract base class
   def __str__(self):
      return self.name

from django.contrib.auth import get_user_model
from djongo import models
#from django-mongo-storage import GridFSStorage
import time

#grid_fs_storage = GridFSStorage(collection='myfiles')

NAME_LENGTH=64

# Create your models here.

#class User(models.Model):
#    name = models.CharField(max_length=30)
#    email = models.EmailField()
#    def __str__(self):
#       return self.name


class HasAttributes(models.Model):
    name = models.CharField(max_length=32)
    attributes = models.JSONField(null=True)
    def __str__(self):
       return self.name
    class Meta:
        abstract = True

# may need to set each as Abstract
class TestProtocol(HasAttributes):
    steps = models.JSONField()
    class Meta:
        abstract = True

class Equipment(HasAttributes):
    serialNo = models.CharField(max_length=64)

class TestEquipment(Equipment):
    pass

class EquipmentUnderTest(Equipment):
    pass

class CellSeparator(models.Model):
    thickness_um = models.FloatField()
    porosity_pct = models.FloatField()
    substrate = models.CharField(max_length=32)
    class Meta:
        abstract = True


class CellBatch(models.Model):
    separator = models.EmbeddedField(model_container=CellSeparator,null=True)
    class Meta:
        abstract = True

class Experiment(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True)
    date = models.DateField()
    testEquipment = models.ManyToManyField(TestEquipment)
    equipmentUnderTest = models.ManyToManyField(EquipmentUnderTest)
    protocol = models.EmbeddedField(
        model_container=TestProtocol,
        null=True
    )
    results = models.JSONField(null=True)
    parameters = models.JSONField(null=True)
    analysis = models.JSONField(null=True)
    objects = models.DjongoManager()



#e = Experiment.objects.create(
#    name="bork",
#    date=time.time(),
#    equipment={},
#    protocol={
#        'name': 'foo',
#        'owner': None,
#        'steps': {}
#    },
#    results = {},
#    parameters = {},
#    analysis = {}
#)

#g = Entry.objects.get(headline='bork')
#assert e == g
#
#e = Experiment()
#e.protocol = {
#    'name': 'b2'
#    'owner': None,
#    'steps': {}
#}
#e.save()

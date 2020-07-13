from django.contrib.auth import get_user_model
from djongo import models
from django-mongo-storage import GridFSStorage
import time

grid_fs_storage = GridFSStorage(collection='myfiles')

# Create your models here.

#class User(models.Model):
#    name = models.CharField(max_length=30)
#    email = models.EmailField()
#    def __str__(self):
#       return self.name

class TestProtocol(models.Model):
    name = models.CharField(max_length=30)
    steps = models.JSONField()
    def __str__(self):
       return self.name
    class Meta:
        abstract = True

class Equipment(models.Model):
    type = models.CharField(max_length=32)
    serialNo = models.CharField(max_length=64)
    metadata = models.JSONField(null=True)

class TestEquipment(Equipment):
    pass

class EquipmentUnderTest(Equipment):
    pass

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

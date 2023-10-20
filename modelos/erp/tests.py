from Proyecto.wsgi import *
from modelos.erp.models import Type

#listar

#Select * from tabla
query = Type.objects.all()
print(query)

t = Type()
t.name = 'Pureksl'
t.save()
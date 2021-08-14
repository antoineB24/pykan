import sys
sys.path.append('/Users/antoine/Documents/pyforum/pyforum')
from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields.related_descriptors import ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor
from django.db.models.query_utils import DeferredAttribute
import pandas as pd

def to_pandas(db, field=None, list_field_object=None):
    list_= []
    field_copy = field
    list_field_object_copy = list_field_object
    if field == None or type(field) != list:
        field_copy = []
        for p in dir(db):
            
            if type(getattr(db, p)) in [DeferredAttribute,  ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor]:
                field_copy.append(p)
    if type(list_field_object_copy) != list:
        list_field_object_copy = []
    for i in range(len(db.objects.all())):
        list_.append([])
        for n in field_copy:
            
            if type(getattr(db.objects.all()[i], str(n) )) in list_field_object_copy:
                list_[i].append(getattr(db.objects.all()[i], str(n) ))
            else: 
                list_[i].append(getattr(db.objects.all()[i], n) )

    return pd.DataFrame(list_, columns=field_copy)

class Command(BaseCommand):
	help = "voir la base de donné en format pandas (lib pandas required)"

	def add_arguments(self, parser):
		parser.add_argument('app',  type=str)
		parser.add_argument('bdd', type=str)
	def handle(self, *args, **options):
		app = __import__(options['app'])
		n = getattr(app.models, options['bdd'])
		return str(to_pandas(n))

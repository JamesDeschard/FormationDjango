from django.core.management.base import BaseCommand
from django.conf import settings
import os
import csv

from first.models import Movie


MODEL = Movie
FILE = 'movies.csv'

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'static', FILE), 'r') as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            header, movies = csv_reader[0], csv_reader[1:]
            for movie in movies:
                attributes = dict(zip(header, movie))
                new_model_entry = MODEL.objects.create(**attributes)
                self.stdout.write(self.style.SUCCESS(f'New Movie entry created: {new_model_entry.original_title}'))
            
        self.stdout.write(self.style.SUCCESS('Successfully created all items'))
from django.core.management.base import BaseCommand
from first.models import Movie


class Command(BaseCommand):

    def query_all_movies(self):
        return Movie.objects.all()
    
    def query_by_title(self, title):
        return Movie.objects.filter(original_title=title)
    
    def query_by_year(self, year):
        return Movie.objects.filter(year=year)
    
    def query_duration(self, length):
        return Movie.objects.filter(duration__gt=length)

    def query_by_director(self, letter, exclude=False):
        if exclude:
            return Movie.objects.filter(director__contains=letter).exclude(director__contains=exclude)
        return Movie.objects.filter(director__icontains=letter)
    
    def query_by_actors(self, actors):
        def get_one_actor(actor):
            return Movie.objects.filter(actors__contains=actor, original_title__icontains='star wars')
        return set().union(*map(get_one_actor, actors))
    
    def query_by_startswith(self, startswith):
        return Movie.objects.filter(original_title__startswith=startswith)
    
    def query_by_endswith(self, endswith):
        return Movie.objects.filter(original_title__endswith=endswith)
    
    def average_vote(self):
        items = self.query_all_movies()
        return sum(item.avg_vote for item in items) / len(items)
    
    def query_raw_all(self):
        return Movie.objects.raw('SELECT * FROM first_movie')

    def handle(self, *args, **options):
        # 1. Query all movies
        print(self.query_all_movies())
        # 2. Query the Dark Knight
        print(self.query_by_title('The Dark Knight'))
        # 3.Query movies from 2012
        print(self.query_by_year(2012))
        # 4. Query movies longer than 200 minutes
        print(self.query_duration(200))
        # 5. Query movie titles starting wight a
        print(self.query_by_startswith('a'))
        # 6. Query movie titles ending with a
        print(self.query_by_endswith('a'))
        # 7. Query movie with director name containing b
        print(self.query_by_director('b', exclude=False))
        # 8. Query movie with director name containing b and not containing a
        print(self.query_by_director('b', exclude='a'))
        # 9. Query movie by ascending order
        print(self.query_all_movies().order_by('original_title'))
        # 10. Get star wars movies by actors
        print(self.query_by_actors(['Harrison Ford', 'Mark Hamill', 'Carrie Fisher']))
        # 11. Get movies by average vote
        print(self.average_vote())
        # 12 Raw query
        print([movie for movie in self.query_raw_all()])
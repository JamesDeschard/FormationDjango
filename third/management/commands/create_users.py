from django.core.management.base import BaseCommand

from django.contrib.auth.models import User


class Command(BaseCommand):

    def create_new_user(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        user.save()
    
    def see_users(self):
        users = User.objects.all()
        for user in users:
            print(user.username)
    
    def see_user_dir(self):
        bobby = User.objects.get(username='Boby')
        # print(dir(bobby))
        print(bobby.is_superuser)
        print(bobby.is_staff)
        print(bobby.is_active)
    
    def change_user_password(self):
        user = User.objects.get(username='Boby')
        user.set_password('james12341')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print('password was successfully changed')

    def handle(self, *args, **options):
        # self.create_new_user('Bobyyy', 'bobby.bobby@gmail.com', 'bobby1234!')
        self.change_user_password()
        print('user was successfully created')
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workouts = [
            Workout(name='Push Ups', description='Upper body strength'),
            Workout(name='Running', description='Cardio endurance'),
        ]
        for workout in workouts:
            workout.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, points=10, date=timezone.now())
        Activity.objects.create(user=users[1], type='Push Ups', duration=15, points=8, date=timezone.now())
        Activity.objects.create(user=users[2], type='Running', duration=25, points=9, date=timezone.now())
        Activity.objects.create(user=users[3], type='Push Ups', duration=20, points=7, date=timezone.now())

        # Create Leaderboard
        for i, user in enumerate(users):
            Leaderboard.objects.create(user=user, total_points=(i+1)*10, rank=i+1)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))

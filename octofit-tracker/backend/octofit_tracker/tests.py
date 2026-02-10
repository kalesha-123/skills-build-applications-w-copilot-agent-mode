from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team2', description='A test team2')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team3', description='A test team3')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, points=10, date='2024-01-01')
        self.assertEqual(str(activity), 'Test User2 - Running (2024-01-01)')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='A test workout')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team4', description='A test team4')
        user = User.objects.create(name='Test User3', email='test3@example.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, total_points=100, rank=1)
        self.assertEqual(str(leaderboard), 'Test User3 - 100 pts')

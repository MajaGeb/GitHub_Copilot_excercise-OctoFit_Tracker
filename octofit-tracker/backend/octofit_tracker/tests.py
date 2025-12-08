from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(email='a@b.com', username='hero', team=team, is_superhero=True)
        self.assertEqual(str(user), 'hero')

    def test_activity_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(email='a@b.com', username='hero', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Run', duration=10, date='2025-12-08')
        self.assertEqual(activity.type, 'Run')

    def test_workout_create(self):
        team = Team.objects.create(name='T', description='d')
        workout = Workout.objects.create(name='W', description='desc')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'W')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='T', description='d')
        leaderboard = Leaderboard.objects.create(team=team, total_points=42)
        self.assertEqual(leaderboard.total_points, 42)

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data robustly
        for model in [Activity, User, Team, Workout, Leaderboard]:
            try:
                model.objects.all().delete()
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Could not clear {model.__name__}: {e}"))

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', username='Iron Man', team=marvel, is_superhero=True),
            User(email='steve@rogers.com', username='Captain America', team=marvel, is_superhero=True),
            User(email='bruce@wayne.com', username='Batman', team=dc, is_superhero=True),
            User(email='clark@kent.com', username='Superman', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flyers')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100)
        Leaderboard.objects.create(team=dc, total_points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))

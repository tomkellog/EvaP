from django.core.management.base import BaseCommand
from django.core.cache import cache

from evap.evaluation.models import Course
from evap.evaluation.tools import calculate_results


class Command(BaseCommand):
    args = ''
    help = 'Clears the cache and pre-warms it with the results of all courses'

    def handle(self, *args, **options):
        self.stdout.write("Clearing cache...")
        cache.clear()

        self.stdout.write("Calculating results for all courses...")
        for course in Course.objects.all():
            calculate_results(course)

        self.stdout.write("Done with updating cache.")

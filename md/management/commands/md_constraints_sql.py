from django.core.management.base import BaseCommand

from django.db import connections
from tsdata.sql import get_add_constraints_and_indexes


class Command(BaseCommand):
    """Inspect and print current MD database constraints and indexes"""

    def handle(self, *args, **options):
        cursor = connections['traffic_stops_md'].cursor()
        print(get_add_constraints_and_indexes(cursor))

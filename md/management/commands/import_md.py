from django.core.management.base import BaseCommand

from md.data import DEFAULT_URL, importer


class Command(BaseCommand):
    """Helper command to kickoff MD data import"""

    def add_arguments(self, parser):
        parser.add_argument('--dest', default=None)
        parser.add_argument('--url', default=DEFAULT_URL)

    def handle(self, *args, **options):
        importer.run(options['url'], options['dest'])

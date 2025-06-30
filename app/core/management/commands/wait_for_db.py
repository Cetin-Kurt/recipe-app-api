"""
Wait for db
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Handle the command"""

        pass
    """
      self.stdout.write('Waiting for database...')
        self.stdout.flush()

        from django.db import connections
        from django.db.utils import OperationalError

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                db_conn.cursor()
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                self.stdout.flush()
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
    """
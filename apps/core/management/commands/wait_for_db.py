"""
Django Command to wait for DB to be available
"""
import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_is_up = False
        db_connection = connections["default"]
        while not db_is_up:
            try:
                # try to connect with db
                db_connection.cursor()
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING(
                        "Database is still not ready. will try in 1 second"
                    )
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available"))

"""
Django Command to wait for DB to be available
"""
import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError as DjangoDbUtilsOperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_is_up = False
        while not db_is_up:
            try:
                # try to connect with db
                self.check(databases=["default"])
                db_is_up = True
                self.stdout.write(self.style.SUCCESS("Database is available"))
            except (Psycopg2OperationalError, DjangoDbUtilsOperationalError):
                self.stdout.write(
                    self.style.WARNING(
                        "Database is still not ready. will try in 1 second"
                    )
                )
                time.sleep(1)

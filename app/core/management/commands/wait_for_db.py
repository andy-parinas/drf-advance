"""
Django command to wait for the database to be avaialble
"""
import time
from psycopg import OperationalError as PsycopgError
from django.db.utils import OperationalError
from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to wait for database """

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Waiting for database")
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True

            except (PsycopgError, OperationalError):
                self.stdout.write("Database unavailable. Waiting for 1sec...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

    # def check(self, databases):
    #     pass

"""
Django Command to wait for DB to be available
"""
import time

from django.conf import settings
from django.core.management import BaseCommand
from elasticsearch import Elasticsearch


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for ElasticSearch...")
        elk_is_up = False
        host = settings.ELK_HOST
        port = settings.ELK_PORT
        while not elk_is_up:
            try:
                # try to connect with db
                self.stdout.write(
                    self.style.WARNING(
                        "trying to connect with elk at {}:{}".format(host, port)
                    )
                )
                es = Elasticsearch([{"host": host, "port": port}])
                es.cluster.health(wait_for_status="yellow", request_timeout=1)
                self.stdout.write(self.style.SUCCESS("✅ ElasticSearch is available"))
                elk_is_up = True
            except Exception:
                self.stdout.write(
                    self.style.WARNING(
                        "❌ ElasticSearch is still not ready. will try in 5 second"
                    )
                )
                time.sleep(5)

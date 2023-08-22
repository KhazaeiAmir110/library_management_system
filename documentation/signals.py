from django.db.models.signals import post_save
from django.dispatch import receiver
import core.redis_services as redis_services

from documentation.models import Documentation


@receiver(post_save, sender=Documentation)
def delete_documentation_from_redis(sender, instance, created, **kwargs):
    data = redis_services.get('documentation_list')
    if created and data:
        redis_services.delete('documentation_list')

from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            students = Group.objects.get(name='estudiante')
        except Group.DoesNotExist:
            students = Group.objects.create(name='estudiante')
            students = Group.objects.create(name='profesor')
            students = Group.objects.create(name='preceptor')
            students = Group.objects.create(name='administrativo')
        instance.user.groups.add(students)
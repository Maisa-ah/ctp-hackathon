from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    YEAR_CHOICES = (
        (0, "Undefined"),
        (1, "Freshman"),
        (2, "Sophomore"),
        (3, "Junior"),
        (4, "Senior")
    )

    email = models.EmailField(max_length=255, unique=True, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    current_year = models.IntegerField(choices=YEAR_CHOICES, default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(null=True)

    school = models.ForeignKey('ServicesMajorsApp.School', on_delete=models.SET_NULL, null=True)
    major = models.ForeignKey('ServicesMajorsApp.Major', on_delete=models.SET_NULL, null=True, default=0)
    classes = models.ManyToManyField('ServicesMajorsApp.Class')
    services = models.ManyToManyField('ServicesMajorsApp.Service')

    def __repr__(self):
        return self.user

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

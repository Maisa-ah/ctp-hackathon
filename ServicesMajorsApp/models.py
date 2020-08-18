from django.db import models
# import models from user to reference here: from user import models


class Class(models.Model):
    class_code = models.CharField(primary_key=True, max_length=8)
    # class_users = models.ManyToManyField(ClassUser)


class Major(models.Model):
    major_code = models.CharField(primary_key=True, max_length=50)
    full_title = models.CharField(max_length=50)
    # students_with_major = models.ForeignKey(User)


class Service(models.Model):
    service_type = models.CharField(max_length=50, primary_key=True)
    # service_mentors = models.ManyToManyField(ServiceMentor)


class School(models.Model):
    school_code = models.CharField(primary_key=True, max_length=8)
    school_name = models.CharField(max_length=50)
    # students = models.ForeignKey(User)

from django.db import models
# import models from user to reference here: from user import models

<<<<<<< HEAD
=======

>>>>>>> f1e3fa4ee279f79306b1d5c3ef728a04f8dc1413
class Major(models.Model):
    major_code = models.CharField(primary_key=True, max_length=50)
    major_title = models.CharField(max_length=50)

    def __str__(self):
        return self.major_title


class Service(models.Model):
    service_type = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.service_type


class School(models.Model):
    school_code = models.CharField(primary_key=True, max_length=8)
    school_name = models.CharField(max_length=50)

    def __str__(self):
        return self.school_name


class Class(models.Model):
    school = models.ForeignKey(
        School, related_name="school", default="CUNY", on_delete=models.CASCADE)
    class_code = models.CharField(primary_key=True, max_length=8)
    class_name = models.CharField(max_length=50)
    # class_users = models.ManyToManyField(ClassUser)

    def __str__(self):
        return self.class_name

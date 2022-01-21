from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)


class Contact(models.Model):
    code = models.CharField("code", max_length=255, blank=True, null=True)
    name = models.CharField("name", max_length=255, blank=True, null=True)
    # phone = models.CharField(max_length=20, blank = True, null = True)
    # address = models.TextField(blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    # createdAt = models.DateTimeField("Created At", auto_now_add=True)


# https://blog.csdn.net/qq_37049050/article/details/82108056
# ORM的一些高级操作
class Student(models.Model):
    """学生表"""
    name = models.CharField(max_length=100)
    gender = models.SmallIntegerField()

    class Meta:
        db_table = 'student'


class Course(models.Model):
    """课程表"""
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'course'


class Score(models.Model):
    """分数表"""
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    number = models.FloatField()

    class Meta:
        db_table = 'score'


class Teacher(models.Model):
    """老师表"""
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher'

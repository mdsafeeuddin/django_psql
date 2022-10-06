from django.db import models

# Create your models here.

class Department(models.Model):
  department = models.CharField(max_length=200, primary_key=True)
  division = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.department, self.division

  class Meta:
    db_table = 'departments'

class Region(models.Model):
  region_id = models.IntegerField(primary_key=True)
  region = models.CharField(max_length=200)
  country = models.CharField(max_length=200)

  class Meta:
    db_table = 'regions'

class Employee(models.Model):
  employee_id = models.IntegerField(primary_key=True)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.CharField(max_length=200, null=True)
  hire_date = models.DateField()
  department = models.CharField(max_length=200)
  gender = models.CharField(max_length=200)
  salary = models.IntegerField()
  region_id = models.IntegerField()

  class Meta:
    db_table = 'employees'

class Student(models.Model):
  student_no = models.IntegerField(primary_key=True)
  student_name = models.CharField(max_length=200)
  age = models.IntegerField()

  class Meta:
    db_table = 'students'

class Course(models.Model):
  course_no = models.CharField(max_length=200, primary_key = True)
  course_title = models.CharField(max_length=200)
  credits = models.IntegerField()

  class Meta:
    db_table = 'courses'

class StudentEnrollment(models.Model):
  student_no = models.IntegerField(primary_key = True, unique=False)
  course_no = models.CharField(max_length=200)

  class Meta:
    db_table = 'student_enrollment'

class Professor(models.Model):
  last_name = models.CharField(max_length=200, primary_key=True)
  department = models.CharField(max_length=200)
  salary = models.IntegerField()
  hire_date = models.DateField('hire_date')

  class Meta:
    db_table = 'professors'

class Teach(models.Model):
  last_name = models.CharField(max_length=200, primary_key=True, unique=False)
  course_no = models.CharField(max_length=200)

  class Meta:
    db_table = 'teach'

class Section(models.Model):
  section_title = models.CharField(max_length=200)
  created = models.DateTimeField('date created')
  updated = models.DateTimeField('date updated')

  def __str__(self) -> str:
    return self.section_title

  class Meta:
    db_table = 'sections'
  
class Topic(models.Model):
  section = models.ForeignKey(Section, on_delete = models.CASCADE)
  topic = models.CharField(max_length=200)
  duration = models.IntegerField(default=0)
  created = models.DateTimeField('date created')
  updated = models.DateTimeField('date updated')

  def __str__(self) -> str:
    return self.topic

  class Meta:
    db_table = 'topics'

class Query(models.Model):
  topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
  query_text = models.TextField()
  query_desc = models.TextField()
  created = models.DateTimeField('date created')
  updated = models.DateTimeField('date updated')

  class Meta:
    db_table = 'queries'

  def __str__(self) -> str:
    return self.query_text
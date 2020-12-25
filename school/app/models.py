from django.db import models
'''
# Create your models here.
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50, blank=False, null=False)
    subject_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.subject_name} {self.subject_description}'

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50, blank=False, null=True)
    teacher_DOB = models.DateField()
    teacher_email = models.EmailField(max_length=50)
    teacher_phone = models.CharField(max_length=20)
    teacher_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.teacher_name} {self.teacher_DOB} {self.teacher_phone} {self.teacher_address}'

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50, blank=False, null=False)
    student_DOB = models.DateField()
    student_email = models.EmailField(max_length=50)
    student_phone = models.CharField(max_length=20)
    student_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.student_name} {self.student_DOB} {self.student_phone} {self.student_address}'
'''
'''
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50, blank=False, null=False)
    subject_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.subject_name} {self.subject_description}'

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50, blank=False, null=False)
    teacher_DOB = models.DateField()
    teacher_email = models.EmailField(max_length=50)
    teacher_phone = models.CharField(max_length=20)
    teacher_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.teacher_name} {self.teacher_DOB} {self.teacher_email} {self.teacher_phone} {self.teacher_address}'

class SubjectTeacher(models.Model):
    class Meta:
        unique_together = (('subject_id', 'teacher_id'),)

    subject_id = models.ManyToManyField(Subject)
    teacher_id = models.ManyToManyField(Teacher)

    def __str__(self):
        return f'{self.subject_id} {self.teacher_id}'


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50, blank=False, null=False)
    class_batch = models.CharField(max_length=5, blank=False, null=False)
    class_advisor = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.class_name} {self.class_batch} {self.class_advisor}'

class ClassSubject(models.Model):
    class Meta:
        unique_together = (('class_id', 'subject_id'),)
    
    class_id = models.ManyToManyField(Class)
    subject_id = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.class_id} {self.subject_id}'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50, blank=False, null=False)
    student_DOB = models.DateField()
    student_email = models.EmailField(max_length=50)
    student_phone = models.CharField(max_length=20)
    student_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.student_name} {self.student_DOB} {self.student_email} {self.student_phone} {self.student_address}'

class ClassStudent(models.Model):
    class Meta:
        unique_together = (('class_id', 'student_id'),)
    
    class_id = models.ManyToManyField(Class)
    student_id = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.class_id} {self.student_id}'



class Extracurricular(models.Model):
    extracurricular_id = models.AutoField(primary_key=True)
    extracurricular_name = models.CharField(max_length=50, blank=False, null=False)
    extracurricular_advisor = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    extracurricular_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.extracurricular_name} {self.extracurricular_advisor} {self.extracurricular_description}'

class ExtracurricularStudent(models.Model):
    class Meta:
        unique_together = (('extracurricular_id', 'student_id'),)
    
    extracurricular_id = models.ManyToManyField(Extracurricular)
    student_id = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.extracurricular_id} {self.student_id}'
'''

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50, blank=False, null=False)
    subject_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.subject_name} {self.subject_description}'

class Employement(models.Model):
    employment_id = models.AutoField(primary_key=True)
    employment_name = models.CharField(max_length=50, blank=False, null=False)
    employment_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.employment_name} {self.employment_description}'

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50, blank=False, null=False)
    employee_DOB = models.DateField()
    employee_email = models.EmailField(max_length=50)
    employee_phone = models.CharField(max_length=20)
    employee_address = models.TextField(blank=True, null=True)
    employee_position = models.ManyToManyField(Employement)

    def __str__(self):
        return f'{self.employee_name} {self.employee_DOB} {self.employee_email} {self.employee_phone} {self.employee_address} {self.employee_position}'

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50, blank=False, null=False)
    class_batch = models.CharField(max_length=5, blank=False, null=False)
    class_advisor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    class_subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.class_name} {self.class_batch} {self.class_advisor} {self.class_subject}'

class Extracurricular(models.Model):
    extracurricular_id = models.AutoField(primary_key=True)
    extracurricular_name = models.CharField(max_length=50, blank=False, null=False)
    extracurricular_advisor = models.OneToOneField(Employee, on_delete=models.CASCADE)
    extracurricular_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.extracurricular_name} {self.extracurricular_advisor} {self.extracurricular_description}'

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50, blank=False, null=False)
    student_DOB = models.DateField()
    student_email = models.EmailField(max_length=50)
    student_phone = models.CharField(max_length=20)
    student_address = models.TextField(blank=True, null=True)
    student_class = models.ManyToManyField(Class)
    student_extracurricular = models.ManyToManyField(Extracurricular)

    def __str__(self):
        return f'{self.student_name} {self.student_DOB} {self.student_email} {self.student_phone} {self.student_address} {self.student_class} {self.student_extracurricular}'
from django import forms
from .models import Subject, Employee, Student, Class, Extracurricular, Employment

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

        widgets = {
            'subject_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'subject_description' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5','style': 'width: 600px;'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

        widgets = {
            'class_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'class_advisor' : forms.Select(attrs={'class': 'form-control'}),
            'class_subject' : forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
            'class_batch' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'yyyy'}),
        }

class ExtracurricularForm(forms.ModelForm):
    class Meta:
        model = Extracurricular
        fields = '__all__'

        widgets = {
            'extracurricular_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'extracurricular_advisor' : forms.Select(attrs={'class': 'form-control'}),
            'extracurricular_description' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5','style': 'width: 600px;'}),
            
        }

class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = '__all__'

        widgets = {
            'employment_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'employment_description' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5','style': 'width: 600px;'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'employee_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'employee_DOB' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'employee_email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'name@example.com'}),
            'employee_phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'employee_address' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5','style': 'width: 600px;'}),
            'employee_position' : forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'student_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'student_DOB' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'student_email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'name@example.com'}),
            'student_phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'student_address' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5','style': 'width: 600px;'}),
            'student_class' : forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
            'student_extracurricular' : forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
        }
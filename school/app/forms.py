from django import forms
from .models import Subject, Employee, Student

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

        widgets = {
            'subject_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'subject_description' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5','style': 'width: 600px;'}),
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
        }
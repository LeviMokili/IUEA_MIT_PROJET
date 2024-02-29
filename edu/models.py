from django.db import models
#create ur class here
   
class Staff(models.Model):
    Staff_name= models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)
    GENDER_CHOICES= [
        ('Male','Male'),
        ('Female','Female'),
    ]
    Gender = models.CharField(choices= GENDER_CHOICES,default='Male', max_length=20)
    Date_Employed= models.DateField(auto_now=True)
    
class Department(models.Model):
    Dept_name = models.CharField(max_length = 25)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
 

class Courses(models.Model):
    course_Name = models.CharField(max_length=10)
    course_code = models.CharField(max_length=10)
    Dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)

class Course_unit(models.Model):
    Unit_Name =models.CharField(max_length=25)
    Unit_Code=models.CharField(max_length=20)
    courses= models.ForeignKey(Courses,on_delete=models.CASCADE)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE)


class Student(models.Model):
    Name = models.CharField(max_length=25)
    Student_RegNo = models.CharField(max_length=25, unique=True)
    Student_Email = models.EmailField(max_length=25)
    Student_Phone = models.CharField(max_length=25)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    Reg_Date = models.DateTimeField()
    
    
    
class slider(models.Model):
 image_name = models.CharField(max_length=25)
 slide = models.ImageField(upload_to='movie')
 
    
class movies(models.Model):
 movie_name = models.FileField(max_length=25)
 movie = models.FileField(max_length=25)

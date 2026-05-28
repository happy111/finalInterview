from django.db import models

# Create your models here.


from django.db import models


class College(models.Model):
	college_name = models.CharField(max_length=100)
	college_address = models.CharField(max_length=100)

class Student(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'))
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=gender_choices, default="Male")
    age = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField()
    profile_image = models.ImageField(null=True, blank=True, upload_to="student")
    created_at = models.DateTimeField(auto_now_add=True)  # Corrected field for creation time
    updated_at = models.DateTimeField(auto_now=True)  # auto_now for updates, not auto_now_add
    file = models.FileField(upload_to="files/")

class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Added on_delete argument
    book_name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    published_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.book_name

class Brand(models.Model):
	brand_name = models.CharField(max_length=100)



class Products(models.Model):
	brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
	product_name = models.CharField(max_length=233)


class skills(models.Model):
	skill_name = models.CharField(max_length=100)



class Person(models.Model):
	skill = models.ManyToManyField(skills)
	person_name = models.CharField(max_length=233)


class Emp(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    dept = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.dept} | {self.salary} | {self.age}"
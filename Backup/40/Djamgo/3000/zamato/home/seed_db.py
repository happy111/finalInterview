from home.models import *
from faker import Faker
import random
fake = Faker('en_IN')


# def dbSeeder(records = 10)->None:
# 	college_names = ['IIT','KNIT sULTANPUR','IGNOU','VIIT cHEnnai','orissa','delhi']
# 	for i  in college_names:
# 		address = fake.address()
# 		College.objects.create(
# 				college_name=i,
# 			    college_address = address
# 			)



# def dbSeeder(records = 10)->None:
# 	colleges = College.objects.all()
# 	for i  in range(records):
# 		college_index = random.randint(0,colleges.count())
# 		college = Colleges[college_index]
# 		name = fake.name()
# 		mobile = fake.phone_number()
# 		email = fake.email()
# 		gender = random.choice(['Male','Female'])
# 		age = random.randint(18,40)
# 		student = Student.objects.create(
# 				name=i,
# 			    mobile = address,
# 			    email = email,
# 			    gender=gender,
# 			    age=age
# 			)
# 		print(student)




fake = Faker()
departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']

# Create 10 fake employees
def dbSeeder(records = 10)->None:
	for _ in range(50):
	    Emp.objects.create(
	        name=fake.name(),
	        salary=round(random.uniform(30000, 120000), 2),
	        dept=random.choice(departments),
	        age=random.randint(21, 60)
	    )
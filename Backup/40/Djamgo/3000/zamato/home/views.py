from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.db.models import *
from .models import *
from django.db.models import OuterRef, Subquery

def index(request):
	#return HttpResponse("Hello client")
	names = ["ram","sita"]

	items ={

	 "pen" : 4,
	 "pensic" : 12

	}

	context = {
	"names" : names,
	"items" : items 
	 }

	emp = Emp.objects.all()
	#  Aggregate
	# max_salary = emp.aggregate(Max('salary'))
	# print(max_salary)

	#  Annotate
	# data = emp.values('dept').annotate(avg_salary=(Avg('salary')))
	# print(data)
	# for d in data:
	# 	print(d['dept'])
	# 	print(d['avg_salary'])

	print("***********************************")

	book = Book.objects.filter().order_by('-published_date')[:1]
	print(type(book))


	print("***********************************")

	# book = Book.objects.filter(
	# 	author = OuterRef('id')).order_by('-published_date').values('book_name')[:1]

	# authors = Author.objects.annotate(books=Subquery(book))
	# for author in authors:
	# 	print(authors)

	print("***********************************")

	book = Book.objects.filter(
		author = OuterRef('id'),published_date__year=2023)\
	.values('author').annotate(total_price = Sum('price')).values('total_price')

	authors = Author.objects.annotate(total_price_for_book=Subquery(book))
	for author in authors:
		print(authors)



	return render(request,"index.html",context)


def contact(request):
	#return HttpResponse("hello contract")
		return render(request,"contact.html")



def dynamic_route(request, number):
	return HttpResponse(f"Response by dynamic route you entered {number}")



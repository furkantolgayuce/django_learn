from django.shortcuts import render, HttpResponse
from .models import DataStore

# Sayfalama yapmak için.
from django.core.paginator import Paginator

# Create your views here.

def index(request):
	keyword = request.GET.get("keyword")

	if keyword:
		all_data = DataStore.objects.filter(title__contains = keyword)
		paginator = Paginator(all_data, 5) # Show x contacts per page

		page = request.GET.get('page')
		contacts = paginator.get_page(page)

		context = {
			'contacts': contacts,
			"keyword" : keyword
		}

		return render(request,"all_data.html",context)

	last_datas = DataStore.objects.all().order_by('-id')[:5]

	context = {
		"last_datas" : last_datas
	}
	return render(request,"index.html",context)

def about(request):
	return render(request,"about.html")

def data_detail(request,id):
	data = DataStore.objects.filter(id = id).first()

	context = {
		"data" : data
	}
	return render(request, "data_detail.html", context)

def all_data(request):

	keyword = request.GET.get("keyword")

	if keyword:
		all_data = DataStore.objects.filter(title__contains = keyword)
	else:
		all_data = DataStore.objects.all()
	paginator = Paginator(all_data, 5) # Show x contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	context = {
		'contacts': contacts,
		"keyword" : keyword
	}

	return render(request,"all_data.html",context)



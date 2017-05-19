#coding utf-8
from django.http import HttpResponse

def index(req):
	return HttpResponse('<h1>Hello world!</h1>')

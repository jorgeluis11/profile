from django.shortcuts import render_to_response, HttpResponse, render, redirect, get_list_or_404
from django.template import RequestContext
import json, httplib, urllib
from project.models import Projects

def index(request):
    data = {
    	"projects" : get_list_or_404(Projects.objects.all().order_by("submit_date"))
    	}
    return render(request,"index.html",data);

from django.shortcuts import render_to_response, HttpResponse, render, redirect
from django.template import RequestContext
import json, httplib, urllib

def index(request):
    return render(request,"index.html",{});
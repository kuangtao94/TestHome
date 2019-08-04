from django.shortcuts import render
from django.http import HttpResponse
# created by tools/tclZIC.tcl - do not edit
#if {![info exists TZDa

def index(request):
    return HttpResponse("Hello Teacher")
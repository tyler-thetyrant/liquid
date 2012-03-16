from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def main(request):
  return render_to_response('intranet/main.html',{"page":'main'})
  
def faq(request):
  return render_to_response('intranet/faq.html',{"page":'faq'})
  
def treasure_chest(request):
  return render_to_response('intranet/treasure_chest.html',{"page":'treasure_chest'})
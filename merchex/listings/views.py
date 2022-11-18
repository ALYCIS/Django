from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello Django world!</h1>')

def about(request):
    return HttpResponse('<h1> Ceci est pour About us </h1>')

def helloBand(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html')
    

def AfficheTitres(request):
    titres = Title.objects.all()
    return HttpResponse(f"""
        <h1> Les titres sont :</h1>

        <ol>
            <li>{titres[0].title} </li>
            <li>{titres[1].title} </li>
            <li>{titres[2].title} </li>
            <li>{titres[3].title} </li>
            <li>{titres[4].title} </li>

        </ol>

    """)

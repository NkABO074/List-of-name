from django.shortcuts import render, redirect,get_object_or_404
from .forms import DudesForm, DudesSearchForm
from django.views.decorators.http import require_POST

# Create your views here.
from .models import Dudes


def index(request):
    latest_Dudes_list = Dudes.objects.all()
    return render(request, "mainApp/index.html", {"latest_Dudes_list": latest_Dudes_list})

def inscriptionView(request):
    return render(request, "mainApp/inscription.html")

@require_POST
def delete_dude(request,dude_id):
    dude = get_object_or_404(Dudes, id=dude_id)
    dude.delete()
    return redirect('index')

def update_dude(request,dude_id):
    dude = get_object_or_404(Dudes, id=dude_id)
    form = DudesForm(request.POST, instance=dude)        

    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = DudesForm(request.POST, instance=dude)

    return render(request,"mainApp/update.html",{'form':form,'dudes': dude})

def search_dude(request):
    query = request.GET.get('name', '')
    results = Dudes.objects.filter(name__contains=query)
    form = DudesSearchForm(request.GET, instance=results)
    if form.is_valid():
        query = form.cleaned_data['query']
    return render(request, 'research.html', {'form': form, 'results': results})

# handle the form submition
def submit_form(request):
    if request.method == 'POST':
        form = DudesForm(request.POST)
    if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            telephone = form.cleaned_data['telephone']
            city = form.cleaned_data['city']
            postal_address = form.cleaned_data['postal_address']
            dude = form.save(commit=True)
            dude.save()

            return redirect('index')
    else:
        form = DudesForm()
    return render(request, 'mainApp/inscription.html', {"form": form})

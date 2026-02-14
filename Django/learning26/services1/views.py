from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm
# Create your views here.
def serviceList(request):
    services = Service.objects.all().order_by('id').values()
    return render(request, 'services1/serviceList.html',{'services':services})

def createServicesForm(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save()
        # return HttpResponse("EMPLOYEE CRATED...")
        return redirect("serviceList")

    else:
        form = ServiceForm()
        return render(request, "services1/createServicesForm.html",{"form":form})

def updateService(request,id):
    services = Service.objects.get(id=id)

    if request.method == 'POST':
        form = ServiceForm(request.POST,instance=services)
        form.save()
        return redirect("serviceList")
    else:
        form = ServiceForm(instance=services)
        return render(request,"services1/updateService.html",{'form':form})

def deleteService(request, id):
    Service.objects.filter(id=id).delete()
    return redirect("serviceList")

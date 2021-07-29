from django.shortcuts import render,HttpResponseRedirect
from .forms import onlineform
from .models import online
from django.contrib import messages


# Create your views here.
#['Firstname','Lastname','Email','Contact','Address','Gender','Password','Confirm_password','Software_courses']
def onlineco(request):
    if request.method == 'POST':
        fm = onlineform(request.POST)
        if fm.is_valid():
            firstnm = fm.cleaned_data['Firstname']
            lastnm = fm.cleaned_data['Lastname']
            ema = fm.cleaned_data['Email']
            con = fm.cleaned_data['Contact']
            addr = fm.cleaned_data['Address']
            gen = fm.cleaned_data['Gender']
            pa = fm.cleaned_data['Password']
            conp = fm.cleaned_data['Confirm_password']
            soco = fm.cleaned_data['Software_courses']
            onlinestore = online(Firstname=firstnm,Lastname=lastnm, Email=ema, Contact=con,Address=addr,Gender=gen,Password=pa,Confirm_password=conp,Software_courses=soco)
            onlinestore.save()
            messages.success(request, 'You have register successfully')
            fm=onlineform()
    else:
        fm = onlineform()
    data = online.objects.all()
    return render(request, 'oncoursehtml.html', {'form': fm, 'dataa': data})

def update_data(request,id):
    if request.method == "POST":
        pi=online.objects.get(pk=id)
        fm=onlineform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You have update successfully')
    else:
        pi=online.objects.get(pk=id)
        fm=onlineform(instance=pi)

    return render(request,'updateonline.html', {'form': fm})


def delete_data(request,id):
    if request.method == "POST":
        row = online.objects.get(pk=id)
        row.delete()
        return HttpResponseRedirect('/oncourse')







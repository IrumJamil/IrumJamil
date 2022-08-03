from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import Stu

# Create your views here.
def base(request):
    if request.method == 'POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            n=fm.cleaned_data['name']
            e=fm.cleaned_data['email']
            p=fm.cleaned_data['password']
            reg=Stu(name=n,email=e,password=p)
            reg.save()
            return HttpResponseRedirect('/')
            fm=StudentForm()
    else:
        fm=StudentForm()
        stud=Stu.objects.all()
        return render(request, 'base.html',{'form': fm,'data':stud})
def update(request,id):
    if request.method == 'POST':
        p=Stu.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=p)
        if fm.is_valid():
            fm.save()
    else:
        p=Stu.objects.get(pk=id)
        fm=StudentForm(instance=p)
    return render(request, 'update.html',{'form':fm})

def delete(request,id):
    if request.method == 'POST':
        p=Stu.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect('/')
        
    
        
        
    
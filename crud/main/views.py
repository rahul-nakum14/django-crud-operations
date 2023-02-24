from django.shortcuts import render,redirect
from . forms import userdataform
from django.contrib import messages
from . models import userdata

'''Method via instance to save data'''
# def add_data(request):
#     if request.method=="POST":
#         form = userdataform(request.POST)
#         if form.is_valid():
#             fn = form.cleaned_data['first_name']
#             ln = form.cleaned_data['last_name']
#             en = form.cleaned_data['email']
#             mo = form.cleaned_data['mob_no']

#             reg = userdata(first_name=fn,last_name=ln,email=en,mob_no=mo)
#             reg.save()

#             messages.success(request,'Account Is Created')
#             return redirect('home')
#     else:
#         form  = userdataform()
#     return render(request,'main/home.html',{'form':form})


def add_data(request):
    if request.method=="POST":
        form = userdataform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Is Created')
            return redirect('home')
    else:
        form  = userdataform()
        data= userdata.objects.all()
    return render(request,'main/home.html',{'form':form,'data':data})

def edit(request, id):
    post = userdata.objects.get(id=id)
    if request.method == "POST":
        form = userdataform(request.POST, instance=post) 
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        post = userdata.objects.get(id=id)
        form = userdataform(instance=post)
    return render(request, 'main/update.html', {'form': form})
    

def delete(request, id):  
    obj = userdata.objects.get(id=id)  
    obj.delete()  
    return redirect('home')  
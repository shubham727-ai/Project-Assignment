from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
   ## return httpResponse('this is homepage')

   if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age =request.POST.get('age')
        skills =request.POST.get('skill')
       desc = request.POST.get('desc')
       index = Index(name=name,surname=surname,age=age,skills=skill,desc=desc)
    index.save()
return render(request,"index.html")
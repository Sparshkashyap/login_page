from django.shortcuts import render


def username(request):
    if request.method == "POST":
        username=request.POST.get("user")
        password=request.POST.get("pass")
        
        print(username)
        print(password)
    return render(request, 'username.html')
        

from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        # 입력받은 내용을 이용해 회원 객체 생성
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(username, password, password2)
        # 회원객체 생성
        user = User()
        user.username = username
        user.set_password(password)
        user.save()

        return render(request, 'accounts/signup_complete.html')
        
    else:
        # form 객체를 만들어서 전달
        context_values = {'form':'this is form'}
        return render(request, 'accounts/signup.html', context_values)

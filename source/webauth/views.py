from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout


def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s' % reverse('webauth:login'))
    return super().dispatch(request, *args, **kwargs)


def login_view(request):

    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webapp:order_list')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:order_list')

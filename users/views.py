from django.shortcuts import render


# Create your views here.
def profile(request):
    context = {}
    template = 'accounts/profile.html'

    return render(request, template, context)

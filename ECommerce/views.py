from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product
from accounts.models import UserProfile, Account

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, "home.html", context)


def socialActivate(request):
    current_user = request.user

    profile = UserProfile.objects.filter(user_id=current_user.id).exists()

    if profile:
        return redirect('cart')
    else:
        new_profile = UserProfile()
        new_profile.user_id = current_user.id
        new_profile.profile_picture = 'default/default-user.png'
        new_profile.save()
        return redirect('dashboard')
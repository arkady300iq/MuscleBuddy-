from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def profile_view(request,pk):
    user_profile = get_object_or_404(User, pk=pk)
    return render(request, 'user_profile/profile.html', {'user_profile': user_profile})
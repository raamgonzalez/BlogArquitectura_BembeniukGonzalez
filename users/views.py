from django.shortcuts import render
from django.urls import reverse
from users.models import User_profile
from django.views.generic import UpdateView,DetailView


class Detail_user_profile(DetailView):
    model = User_profile
    template_name= 'users/detail_user_profile.html'

class Update_user_profile(UpdateView):
    model = User_profile
    template_name = 'users/update_user_profile.html'
    fields = ['phone', 'profile_image']

    def get_success_url(self):
        return reverse('detail_user_profile', kwargs = {'pk':self.object.pk})


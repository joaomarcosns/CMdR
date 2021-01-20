from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Nationality, About, Homeless

from django.urls import reverse_lazy


# Create your views here.

######################################################### CreateView #########################################################
class NationalityCreate(CreateView):
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')


class AboutCreate(CreateView):
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')

class HomelessCreate(CreateView):
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')



######################################################### UpdateView  #########################################################

class NationalityUpdate(UpdateView):
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')

class AboutUpdate(UpdateView):
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')

class HomelessUpdate(UpdateView):
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')



######################################################### DeleteView  #########################################################

class NationalityDelete(DeleteView):
    model = Nationality
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('home-home')

class AboutDelete(DeleteView):
    model = About
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('home-home')


class HomelessDelete(DeleteView):
    model = Homeless
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('home-home')
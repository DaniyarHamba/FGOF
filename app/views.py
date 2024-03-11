from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin
from .models import Courses, Useres
from django.urls import reverse_lazy
# Create your views here.


class CourseList(UserPassesTestMixin, ListView):
    model = Courses
    context_object_name = 'course'
    template_name = 'app/course_list.html'

    def test_func(self):

        if self.request.user.Useres.choice == 't':
            return True
        else:
            return False


class CourseDetail(UserPassesTestMixin, DetailView):
    model = Courses
    context_object_name = 'courses'
    template_name = 'app/course_detail.html'


class CourseCreate(UserPassesTestMixin, CreateView):
    model = Courses
    success_url = reverse_lazy('course_list')
    template_name = 'app/form.html'
    fields = '__all__'


class CourseUpdate(UserPassesTestMixin, UpdateView):
    model = Courses
    success_url = reverse_lazy('course_list')
    template_name = 'app/form.html'
    fields = '__all__'


class CourseDelete(UserPassesTestMixin, DeleteView):
    model = Courses
    success_url = reverse_lazy('course_list')
    template_name = 'app/form.html'


class UserLogoutView(LogoutView):
    pass


class UserLoginView(LoginView):
    template_name = 'app/login.html'
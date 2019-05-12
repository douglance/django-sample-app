from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .models import Mentor
from .forms import CreateMentorForm, FindMentorForm


def index(request):
    return render(request, 'mentorfinder/index.html')


class CreateMentor(FormView):
    form_class = CreateMentorForm
    template_name = 'mentorfinder/create.html'

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            name = f'{form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]}'
            messages.add_message(request, messages.SUCCESS,
                                 f'Successfully added {name}')
            return HttpResponseRedirect(reverse('create'))

        messages.add_message(request, messages.ERROR,
                             f'An error occurred while attempting to add mentor')
        return render(request, self.template_name, {'form': form})


class FindMentor(FormView):
    form_class = FindMentorForm
    template_name = 'mentorfinder/find.html'

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            mentor = form.cleaned_data["mentor"]
            name = f'{form.cleaned_data["mentor"]}'
            messages.add_message(request, messages.SUCCESS,
                                 f'Successfully found {name}')
            return HttpResponseRedirect(reverse('detail', args=(mentor.id,)))

        messages.add_message(request, messages.ERROR,
                             f'An error occurred while attempting to find mentor')
        return render(request, self.template_name, {'form': form})


def load_mentors(request):
    available = request.GET.get('available')
    mentors = Mentor.objects.filter(
        available=available).order_by('last_name')
    return render(request, 'mentorfinder/mentor-list-options.html', {'mentors': mentors})


class MentorDetail(TemplateView):
    template_name = 'mentorfinder/mentor-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mentor = Mentor.objects.get(id=kwargs['id'])
        mentor.phone = "(%c%c%c) %c%c%c-%c%c%c%c" % tuple(str(mentor.phone))
        context["mentor"] = mentor
        return context

# -*- coding: utf-8 -*-
import os
from .models import Projects, AwardsAndAchievements, Notes,\
    Summary, Experience
from django.utils import timezone
from django.views import generic
from .forms import ContactForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from htmlmin.decorators import minified_response
from django.views.generic import TemplateView


class IndexListView(generic.ListView):
    """
    Index view for the portfolio.
    """
    context_object_name = 'project_list'
    template_name = 'portfolio/index.html'
    queryset = Projects.objects.order_by('-pub_date')[:3]

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['award_list'] = AwardsAndAchievements.objects.order_by('-received')
        context['summary_list'] = Summary.objects.all()
        return context


class ProjectListView(generic.ListView):
    context_object_name = 'project_list'
    template_name = 'portfolio/project_list.html'

    def get_queryset(self):
        """Return the projects"""
        return Projects.objects.order_by('-pub_date')


class NoteListView(generic.ListView):
    context_object_name = 'note_list'
    template_name = 'portfolio/note.html'

    def get_queryset(self):
        """Return the Notes"""
        return Notes.objects.all()


class ProjectDetailView(generic.DetailView):
    model = Projects
    template_name = 'portfolio/project_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['now'] = timezone.now()
        return context


class ExperienceListView(generic.ListView):
    context_object_name = 'experience_list'
    template_name = 'portfolio/experience.html'

    def get_queryset(self):
        """Return the experience"""
        return Experience.objects.order_by('-start_date')


@minified_response
@csrf_exempt
def contact_view(request):
    message = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sub = form.cleaned_data["subject"][:min(len(form.cleaned_data["subject"]),20)] + '...'
            email_subject = f'YUYU: {form.cleaned_data["email"]}: {sub}'
            email_message = form.cleaned_data['message']
            message = Mail(
                from_email=settings.CONTACT_EMAIL,
                to_emails=settings.ADMIN_EMAIL + form.cleaned_data["email"].split(' '),
                subject=email_subject,
                html_content=email_message)
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                sg.send(message)
                # send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)    
                print('Email sent')
                message = 'Your message has been sent. Thank you!'
            except Exception as e:
                print(e.message)         
                message = 'Your message could not be sent. Please try again later.'
    form = ContactForm()
    context = {'form': form, 'message': message}
    return render(request, 'portfolio/contact.html', context)



class Error404(TemplateView):
    template_name = "portfolio/404.html"
    
    @classmethod
    def get_rendered_view(cls):
        as_view_fn = cls.as_view()

        def view_fn(request, exception):
            response = as_view_fn(request)
            # this is what was missing before
            response.render()
            return response
        return view_fn

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.status_code = 404
        return self.render_to_response({'status_code': response.status_code})

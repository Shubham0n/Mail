from django.shortcuts import render, HttpResponse
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
        
        '''
        this for view
        '''
        # name = form.cleaned_data.get("name").strip()
        # from_email = form.cleaned_data.get("email")
        # subject = form.cleaned_data.get("inquiry")
        # msg = f"{name} with email {from_email} said:"
        # msg += f'\n"{subject}"\n\n'
        # msg += form.cleaned_data.get("message")

        # send_mail(
        #         subject=subject,
        #         message=msg,
        #         from_email=settings.EMAIL_HOST_USER,
        #         recipient_list=[from_email]
        #     )
        # return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'success.html'
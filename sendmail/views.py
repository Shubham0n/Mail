from django.shortcuts import render, HttpResponse
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

        """
        this for view
        """
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
    template_name = "success.html"



# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import get_template

# def customer_selections_sent(request):
#     # make=request.POST['makeselection']
#     if request.method == "GET":

#         current_site = get_current_site(request)
#         emailto = request.user.email_user
#         user = request.user.username

#         # call session values from SearchInventory function
#         modelvalue = request.session.get("modelvalue")
#         makevalue = request.session.get("makevalue")
#         subject = "ShowVroom Selections"

#         # create variables to be used in the email template
#         Email_Vars = {
#             "user": user,
#             "make": makevalue,
#             "model": modelvalue,
#             "domain": current_site.domain,
#         }

#         # create the email msg
#         message = get_template("customer_selections_email.html").render(Email_Vars)
#         html_message = get_template("customer_selections_email.html").render(Email_Vars)
#         message.content_subtype = "html"  # Main content is now text/html


#         # send email
#         request.user.email_user(subject, message)
#         # request.user.email_user(subject, html_message)
#         # return redirect('customer_selections_sent')
#         return render(
#             request,
#             "customer_selections_sent.html",
#             {
#                 "title": "Deals are on the way",
#                 "body": "We will email you shortly with more detail on your choices, you can respond to the dealers via the app until you agree to a viewing, test or purchase ",
#                 "year": datetime.now().year,
#             },
#         )
        
#         send_mail(
#             subject,
#             message,
#             "Abc@xyz.org",
#             emailto,
#             fail_silently=False,
#             html_message=html_message,
#         )
#         sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
#         response = sg.send(message)
#         # log respon
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
        
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from .models import About, Project, Setting, Contact, Homepage
from django.shortcuts import redirect 
from django.conf import settings
from django.utils.translation import gettext as _

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Abouts'] = About.objects.first()
        context['Projects'] = Project.objects.all().order_by('-id')
        context['setting'] = Setting.objects.first()
        context['Homepage'] = Homepage.objects.first()

        return context

    def post(self, request, *args, **kwargs):
        fullName = request.POST.get('fullName', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not all([fullName, email, message]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('index')

        Contact.objects.create(
            full_name=fullName,
            email=email,
            message=message
        )

        try:
            send_mail(
                subject=f"New Message: {fullName}",
                message=f"""

                Full Name: {fullName}
                E-mail: {email}

                Message:
                {message}

                Admin panel: {request.build_absolute_uri('/admin/')}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['berkaykahraman27@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, _('Thank you! Your message has been sent successfully. I will get back to you shortly.'))
        except Exception as e:
            
            print(f"[MAIL ERROR] {e}")
            messages.error(request, _('An error occurred while sending the message. Please try again later.'))

        return redirect('index')  
from tzac_notifications.forms import NotificationForm
from tzac_notifications.models import Notification
from django.http import HttpRequest

def confirm_notice(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Notification.objects.create(
                subject = cd['subject'],
                body = cd['body'])
    return redirect("/admin")

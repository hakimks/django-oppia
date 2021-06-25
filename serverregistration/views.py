
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views.generic import FormView

from helpers.mixins.TitleViewMixin import TitleViewMixin

from settings import constants
from settings.models import SettingProperties
from serverregistration.forms import RegisterServerForm


class RegisterServerView(FormView, TitleViewMixin):

    template_name = 'serverregistration/register.html'
    form_class = RegisterServerForm
    success_url = 'thanks/'
    title = _(u'Register Server')

    def get_initial(self):
        initial = {'server_url': SettingProperties.get_property(
            constants.OPPIA_HOSTNAME, ''),
            'include_no_courses': SettingProperties.get_bool(
            constants.OPPIA_SERVER_REGISTER_NO_COURSES, False),
            'include_no_users': SettingProperties.get_bool(
            constants.OPPIA_SERVER_REGISTER_NO_USERS, False),
            'email_notifications': SettingProperties.get_bool(
            constants.OPPIA_SERVER_REGISTER_EMAIL_NOTIF, False),
            'notif_email_address': SettingProperties.get_string(
            constants.OPPIA_SERVER_REGISTER_NOTIF_EMAIL_ADDRESS, '')
        }

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        SettingProperties.set_bool(
            constants.OPPIA_SERVER_REGISTERED, True)

        server_url = form.cleaned_data.get("server_url")
        SettingProperties.set_string(
            constants.OPPIA_HOSTNAME, server_url)

        include_no_courses = form.cleaned_data.get("include_no_courses")
        SettingProperties.set_bool(
            constants.OPPIA_SERVER_REGISTER_NO_COURSES, include_no_courses)

        include_no_users = form.cleaned_data.get("include_no_users")
        SettingProperties.set_bool(
            constants.OPPIA_SERVER_REGISTER_NO_USERS, include_no_users)

        email_notifications = form.cleaned_data.get("email_notifications")
        SettingProperties.set_bool(
            constants.OPPIA_SERVER_REGISTER_EMAIL_NOTIF, email_notifications)

        notif_email_address = form.cleaned_data.get("notif_email_address")
        SettingProperties.set_string(
            constants.OPPIA_SERVER_REGISTER_NOTIF_EMAIL_ADDRESS,
            notif_email_address)
        
        
        return response

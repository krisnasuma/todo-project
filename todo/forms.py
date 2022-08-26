#this file was created manually, 
# because we need to use django-widget-tweaks for the forms only

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


#import class Task from todo\models.py
from .models import Task

#create class TaskForm for create task
class TaskForm(ModelForm):
    class Meta:
        #realize form model with the Task model
        model = Task
        #set fields for the form, what fields will be displayed on the form
        fields = ('title','description','status')
        #set labels for the fields
        labels = {
            'title': _('Judul'),
            'description': _('Deskripsi'),
            'status': _('Status'),
        }
        #set error messages text for fields validation
        error_messages = {
            'title': {
                'required': _("Judul Tidak Boleh Kosong."),
            },
            'description': {
                'required': _("Deskripsi Tidak Boleh Kosong"),
            },
        }
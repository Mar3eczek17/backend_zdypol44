from django.contrib import admin

from form_app6.models import Task  #klasa siedzi w modelach

# Register your models here.
admin.site.register(Task)  # aby cos sie pojawilo w modelu administratora trzeba to zarejestrowac

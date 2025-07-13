from django.contrib import admin # type: ignore
from .models import Project, Client, Contact, Subscriber

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Subscriber)

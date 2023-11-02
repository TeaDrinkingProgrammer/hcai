from django.contrib import admin

from hcai.app.models import BadAppInput, Feedback, GoodAppInput

admin.site.register(Feedback)
admin.site.register(GoodAppInput)
admin.site.register(BadAppInput)
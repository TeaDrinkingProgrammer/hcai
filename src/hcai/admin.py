from django.contrib import admin

from hcai.app.models import BadAppFeedback, BadAppInput, GoodAppFeedback, GoodAppInput

admin.site.register(GoodAppFeedback)
admin.site.register(BadAppFeedback)
admin.site.register(GoodAppInput)
admin.site.register(BadAppInput)
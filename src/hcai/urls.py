"""
URL configuration for hcai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin

from .app import home
from .app.good_app import home as ga_home
from .app.good_app import questionaire as ga_questionaire
from .app.good_app import result as ga_result
from .app.good_app import explanation as ga_explanation
from .app.good_app import privacy as ga_privacy

from .app.test_app import test_app, test_form

from .app.bad_app import home as ba_home
from .app.bad_app import questionaire as ba_questionaire
from .app.bad_app import result as ba_result

good_app_patterns = [
    path("", ga_home.index),
    path("questionaire/", ga_questionaire.index),
    path("result/", ga_result.index),
    path("explanation/", ga_explanation.index),
    path("privacy/", ga_privacy.index),
]

bad_app_patterns = [
    path("", ba_home.index),
    path("questionaire/", ba_questionaire.index),
    path("result/", ba_result.index),
]

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", home.index),
    path("good_app/", include(good_app_patterns)),
    path("bad_app/", include(bad_app_patterns)),
    path("test/", test_app.index),
    path("your-name/", test_form.index),
]
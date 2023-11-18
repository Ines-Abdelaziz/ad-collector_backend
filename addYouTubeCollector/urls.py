"""addYouTubeCollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from StoreToDB import views
from youtube_dashboard import views as v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    url(r'^admin/', admin.site.urls),
    url(r'^store_Data_To_DataBase', views.store_Data_To_DataBase,name='store_Data_To_DataBase'),
    url(r'getStatistiqueFromDB', views.getStatistiqueFromDB,name='getStatistiqueFromDB'),
    url(r'get_general_statistics', v.get_general_statistics,name='get_general_statistics'),
    url(r'get_all_ads', v.get_all_ads,name='get_all_ads'),
    url(r'youtubeAdCollector', v.get_site,name='get_site'),
    url(r'getConsent', views.isConsent,name='isConsent'),
    url(r'registerConsent', views.acceptConsent,name='acceptConsent'),
    url(r'removeConsent', views.removeConsent,name='removeConsent')
]

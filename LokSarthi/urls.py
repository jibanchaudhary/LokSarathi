"""
URL configuration for LokSarthi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from catalog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('catalog/',include('catalog.urls')),
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('base/',views.base,name="base"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('syllabus/',views.syllabus_list,name="syllabus"),
    path('MCQ/',views.MCQ,name="MCQ"),
    path('addQuestion/',views.addQuestion,name="AddQuestion"),
    path('officer/',views.Officer,name="officerlevel"),
    path('section_officer/',views.Section_officer,name="Sectionofficer"),
    path('constition/',views.constition,name="constitution"),
    path('books/',views.books,name="books")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
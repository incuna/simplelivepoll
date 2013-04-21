from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

from .views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),

    url('^$', HomeView.as_view(), name='home'),
    url('^questions/$', NextQuestion.as_view(), name='nextquestion'),
    url('^questions/(?P<question_pk>[0-9]+)/$', QuestionView.as_view(), name='question'),
    url('^results/(?P<question_pk>[0-9]+)/$', ResultView.as_view(), name='results'),

    # Used to serve specific static media such as tiny_mce
    url(r'^direct-static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATICFILES_DIR,
    }),
)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eis.views.home', name='home'),
    # url(r'^eis/', include('eis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    (r'^hello/(\d{1,3})/$', 'eis.views.hello'),
    (r'^hello2/\d{1,3}/$', 'eis.views.hello2'),
    (r'^accounts/login/$', 'staff.views.login_view'),
    (r'^accounts/logout/$', 'staff.views.logout_view'),
    (r'^main/$', 'staff.views.main'),
    (r'^ajax_staff_list/$', 'staff.views.ajax_staff_list'),
    (r'^ajax_staff_add/$', 'staff.views.ajax_staff_add'),
    (r'^ajax_staff_del/$', 'staff.views.ajax_staff_del'),
)

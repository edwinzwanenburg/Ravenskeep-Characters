from django.conf.urls import patterns, include, url

urlpatterns = patterns('chars.views',
    url(r'^$', 'home'),
    url(r'^char/(?P<char_id>\d+)/$', 'char'),

    # Logout
    (r'^logout/$', 'logout_user'),

)

urlpatterns += patterns('',
    # Login
    (r'^login/$', 'django.contrib.auth.views.login'),
)

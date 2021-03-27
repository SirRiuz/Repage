

# Django-hosts
from django_hosts import patterns, host


host_patterns  = patterns(
    '',
    host(r'www','core.urls',name='www'),
    host(r'api','core.apiurls',name='api'),
    host(r'(\w+)','pages.urls',name='page')
)
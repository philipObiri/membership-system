from django.contrib import admin
from .models import Record

admin.site.register(Record)
admin.site.site_header = "Christ Commonwealth Community (Membership System)"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Membership System"

from django.contrib import admin
from jobseeker.models import Contact
from jobseeker.models import JobForm
from jobseeker.models import signin
# Register your models here.
admin.site.register(Contact)
admin.site.register(JobForm)
admin.site.register(signin)
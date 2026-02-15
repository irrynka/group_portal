from django.contrib import admin
from users.models import Poll, Portfolio, Vote

admin.site.register(Poll)
admin.site.register(Portfolio)
admin.site.register(Vote)

# Register your models here.

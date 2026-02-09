from django.contrib import admin
from users.models import Poll, User, Portfolio, Vote

admin.site.register(User)
admin.site.register(Poll)
admin.site.register(Portfolio)
admin.site.register(Vote)

# Register your models here.

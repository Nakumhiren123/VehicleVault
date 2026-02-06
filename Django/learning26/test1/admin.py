from django.contrib import admin
from .models import Accessory,Car, User,CarAccessoryMapping,SearchHistory, Review, Comparison, Admin, UserInteraction, UserPreference
# Register your models here.

admin.site.register(Accessory)
admin.site.register(Car)
admin.site.register(User)
admin.site.register(CarAccessoryMapping)
admin.site.register(SearchHistory)
admin.site.register(Review)
admin.site.register(Comparison)
admin.site.register(Admin)
admin.site.register(UserInteraction)
admin.site.register(UserPreference)
from django.contrib import admin
from .models import Profile, Pet, Diseases, RequestPhoto, RequestPoll

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(Diseases)
class DiseasesAdmin(admin.ModelAdmin):
    pass

@admin.register(RequestPhoto)
class RequestPhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(RequestPoll)
class RequestPollAdmin(admin.ModelAdmin):
    pass

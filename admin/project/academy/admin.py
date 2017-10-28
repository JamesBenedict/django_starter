# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
	list_display = ("name", "branch", "gender", "data_of_birth", "race")
	list_filter = ("branch", "gender", "race")
	search_fields = ("name",)
admin.site.register(Invite, InviteAdmin)

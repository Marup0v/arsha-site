from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Portfolio, Type, Service, Worker

@admin.register(Type)
class TypeAdmin(ModelAdmin):
    list_display = ["nomi"]


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    list_display = ["nomi", "company_name", "date"]
    search_fields = ["nomi", "company_name"]


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ["nomi", "ikonka"]
    search_fields = ["nomi"]


@admin.register(Worker)
class WorkerAdmin(ModelAdmin):
    list_display = ["ism_familiya", "lavozimi"]
    search_fields = ["ism_familiya", "lavozimi"]
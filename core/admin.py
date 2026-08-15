from django.contrib import admin
from .models import Matricula, Mensalidade, Modalidade, Plano, Professor

admin.site.register(Plano)
admin.site.register(Professor)
admin.site.register(Modalidade)
admin.site.register(Matricula)
admin.site.register(Mensalidade)

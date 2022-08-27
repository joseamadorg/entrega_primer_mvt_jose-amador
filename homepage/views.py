from django.shortcuts import render

# Create your views here.
from .models import Familiar


def index(request):
  familiars_list = Familiar.objects.all()
  context = {'familiars_list': familiars_list}
  return render(request, 'homepage/index.html', context=context)
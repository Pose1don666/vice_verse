
from django.shortcuts import render


def reverse_text(request):
    return render(request, 'text_area.html')
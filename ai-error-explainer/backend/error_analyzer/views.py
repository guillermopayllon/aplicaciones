from django.shortcuts import render
from .openai_client import analizar_error

def home(request):
    resultado = None
    if request.method == 'POST':
        error_text = request.POST.get('error_text')
        resultado = analizar_error(error_text)
    return render(request, 'index.html', {'resultado': resultado})

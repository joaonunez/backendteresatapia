from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    return render(request, 'templatefirstapp/template1.html')
def rendertemplateData(request):
    data = {"nombre": "Kike Morande"}
    return render(request, 'templatefirstapp/template2.html', data)

def infoUsuario(request):
    data = { "id" : "1001", "nombre": "Lopez", "email": "lopez@jls.es"}
    return render(request, 'templatefirstapp/userInfoTemplate.html', data)

def infoUsuarioImagen(request):
    data = {"id": "123", "nombre": "Jelle", "email": "mraggle@gmail.com"}
    return render(request, 'templatefirstapp/userInfoTemplateImagen.html', data)


from django.shortcuts import render

# Create your views here.

def api_view(request):

    return render(request, 'api/principal.html')



def convertir_a_hexadecimal(x):    
    numero = int(x)    
    hexadecimal = hex(numero)
    if len(hexadecimal) > 5:
        return -1
    else:
        return hexadecimal

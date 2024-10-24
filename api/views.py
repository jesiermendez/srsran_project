from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
import subprocess
from .serializers import *
from.forms import *
from .models import *

# Create your views here.

class EjecutarScriptsView(APIView):
    def post(self, request):
        parametros = request.data.get('parametros', '')

        try:
            resultado = subprocess.run(
                ["./mi_srsran_script.sh"] + parametros.split(),
                capture_output=True,
                text=True,
                check=True
            )
            if resultado.returncode == 0:
                return Response({"output": resultado.stdout}), status.HTTP_200_OK
            else:
                return Response({"error": resultado.stderr}), status.HTTP_400_BAD_REQUEST
        except Exception as e:
            return Response({"error": str}), status.HTTP_500_INTERNAL_SERVER_ERROR

class srsranModelViewSet(viewsets.ModelViewSet):
    queryset = enodeb.objects.all()
    serializer_class = enodeb_serializer

@login_required
def api_view(request):
    mensaje1 = ''
    mensaje2 = ''
    mensaje4 = ''
    mensaje5 = ''
    mensaje6 = ''
    mensaje7 = ''
    mensaje8 = ''
    mensaje9 = ''
    mensaje10 = ''
    mensaje11 = ''
    mensaje12 = ''

    error1 = ''

    try:
        last_enb_files = enb_files.objects.latest('id')
        initial_data_enb_files = {'sib_config': last_enb_files.sib_config,'rr_config': last_enb_files.rr_config,
                               'rb_config':last_enb_files.rb_config,                               
                               }
    except enb_files.DoesNotExist:
        last_enb_files = None
        initial_data_enb_files = {}

    try:
        last_enodeb = enodeb.objects.latest('id')
        initial_data_enodeb = {'enb_id': last_enodeb.get_enb_id,'mcc': last_enodeb.mcc, 'mnc':last_enodeb.mnc, 
                               'mme_addr': last_enodeb.mme_addr, 'gtp_bind_addr':last_enodeb.gtp_bind_addr, 
                               'gtp_advertise_addr':last_enodeb.gtp_advertise_addr, 's1c_bind_addr':last_enodeb.s1c_bind_addr,
                                's1c_bind_port': last_enodeb.s1c_bind_port, 'n_prb':last_enodeb.n_prb, 'tm':last_enodeb.tm,
                                'nof_ports':last_enodeb.nof_ports,
                               }
    except enodeb.DoesNotExist:
        last_enodeb = None
        initial_data_enodeb = {}

    form1 = enodeb_form(initial=initial_data_enodeb)
    form2 = enb_files_form(initial=initial_data_enb_files)

    if request.method == 'POST':
        if 'submit_form1' in request.POST:
            form1 = enodeb_form(request.POST)
            if form1.is_valid():                
                form_unsaved = form1.save(commit=False)
                id_enb = form_unsaved.enb_id
                ex = convertir_a_hexadecimal(id_enb)
                if ex != -1:
                    enodeb.objects.all().delete()
                    form_unsaved.enb_id = ex
                    form_unsaved.save()                
                    mensaje1 = 'Ajustes corregidos exitosamente'
                else:
                    error1 = 'El id excede los 20 bits'
              
        elif 'submit_form2' in request.POST:
            form2 = enb_files_form(request.POST)
            if form2.is_valid():
                enb_files.objects.all().delete()
                form2.save()
                mensaje2 = 'Ajustes corregidos exitosamente'
                
        
        elif 'submit_form3' in request.POST:
            pass

                
        
    return render(request, 'api/principal.html', {
        'form1':form1, 'form2':form2,
        'error':error1, 'mensaje1':mensaje1, 'mensaje2':mensaje2
    } )





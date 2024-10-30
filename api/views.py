from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
import subprocess
from .serializers import *
from.forms import *
from .models import *
from .scripts import *

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
    mensaje3 = ''
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
    error2 = ''
    error3 = ''
    error4 = ''
    error5 = ''
    error6 = ''
    error7 = ''
    error8 = ''
    error9 = ''
    error10 = ''
    error11 = ''
    error12 = ''

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
        initial_data_enodeb = {'enb_id': last_enodeb.get_enb_id, 'name': last_enodeb.name,'mcc': last_enodeb.mcc, 'mnc':last_enodeb.mnc, 
                               'mme_addr': last_enodeb.mme_addr, 'gtp_bind_addr':last_enodeb.gtp_bind_addr, 
                               'gtp_advertise_addr':last_enodeb.gtp_advertise_addr, 's1c_bind_addr':last_enodeb.s1c_bind_addr,
                                's1c_bind_port': last_enodeb.s1c_bind_port, 'n_prb':last_enodeb.n_prb, 'tm':last_enodeb.tm,
                                'nof_ports':last_enodeb.nof_ports, 'p_a':last_enodeb.p_a
                               }
    except enodeb.DoesNotExist:
        last_enodeb = None
        initial_data_enodeb = {}

    try:
        last_rf = rf.objects.latest('id')
        initial_data_rf = {'dl_earfcn':last_rf.dl_earfcn, 'tx_gain': last_rf.tx_gain , 'rx_gain': last_rf.rx_gain,
                           'dl_freq': last_rf.dl_freq, 'ul_freq':last_rf.ul_freq, 'device_name':last_rf.device_name,
                           'device_args':last_rf.device_args, 'time_adv_nsamples':last_rf.time_adv_nsamples}

    except rf.DoesNotExist:
        last_rf = None
        initial_data_rf = {}

    try:
        last_pcap = pcap.objects.latest('id')
        initial_data_pcap = {'enable':last_pcap.enable,'filename':last_pcap.filename,'nr_filename':last_pcap.nr_filename,
                             's1ap_enable':last_pcap.s1ap_enable,'s1ap_filename':last_pcap.s1ap_filename,'mac_net_enable':last_pcap.mac_net_enable,
                             'bind_ip':last_pcap.bind_ip,'bind_port':last_pcap.bind_port,'client_ip':last_pcap.client_ip,'client_port':last_pcap.client_port}

    except pcap.DoesNotExist:
        last_pcap = None
        initial_data_pcap = {}

    try:
        last_log = log.objects.latest('id')
        initial_data_log = {'all_level':last_log.all_level,'all_hex_limit':last_log.all_hex_limit,'filename':last_log.filename,
                            'file_max_size':last_log.file_max_size,'gui_enable':last_log.gui_enable}

    except log.DoesNotExist:
        last_log = None
        initial_data_log = {}

    try:
        last_scheduler = scheduler.objects.latest('id')
        initial_data_scheduler = {'policy':last_scheduler.policy,'policy_args':last_scheduler.policy_args,'min_aggr_level':last_scheduler.min_aggr_level,
                                  'max_aggr_level':last_scheduler.max_aggr_level,'adaptive_aggr_level':last_scheduler.adaptive_aggr_level,'pdsch_mcs':last_scheduler.pdsch_mcs,
                                  'pdsch_max_mcs':last_scheduler.pdsch_max_mcs,'pusch_mcs':last_scheduler.pusch_mcs,'pusch_max_mcs':last_scheduler.pusch_max_mcs,
                                  'min_nof_ctrl_symbols':last_scheduler.min_nof_ctrl_symbols,'max_nof_ctrl_symbols':last_scheduler.max_nof_ctrl_symbols,'pucch_multiplex_enable':last_scheduler.pucch_multiplex_enable,
                                  'pucch_harq_max_rb':last_scheduler.pucch_harq_max_rb,'target_bler':last_scheduler.target_bler,'max_delta_dl_cqi':last_scheduler.max_delta_dl_cqi,
                                  'max_delta_ul_snr':last_scheduler.max_delta_ul_snr,'adaptive_dl_mcs_step_size':last_scheduler.adaptive_dl_mcs_step_size,'adaptive_ul_mcs_step_size':last_scheduler.adaptive_ul_mcs_step_size,
                                  'min_tpc_tti_interval':last_scheduler.min_tpc_tti_interval,'ul_snr_avg_alpha':last_scheduler.ul_snr_avg_alpha,'init_ul_snr_value':last_scheduler.init_ul_snr_value,
                                  'init_dl_cqi':last_scheduler.init_dl_cqi,'max_sib_coderate':last_scheduler.max_sib_coderate,'pdcch_cqi_offset':last_scheduler.pdcch_cqi_offset,
                                  'nr_pdsch_mcs':last_scheduler.nr_pdsch_mcs,'nr_pusch_mcs':last_scheduler.nr_pusch_mcs}

    except scheduler.DoesNotExist:
        last_scheduler = None
        initial_data_scheduler = {}

    try:
        last_slicin = slicin.objects.latest('id')
        initial_data_slicin = {'enable_eMBB':last_slicin.enable_eMBB,'enable_URLLC':last_slicin.enable_URLLC,'enable_MIoT':last_slicin.enable_MIoT,
                               'eMBB_sd':last_slicin.eMBB_sd,'URLLC_sd':last_slicin.URLLC_sd,'MIoT_sd':last_slicin.MIoT_sd}

    except slicin.DoesNotExist:
        last_slicin = None
        initial_data_slicin = {}

    try:
        last_embms = embms.objects.latest('id')
        initial_data_embms = {'enable':last_embms.enable,'m1u_multiaddr':last_embms.m1u_multiaddr,
                              'm1u_if_addr':last_embms.m1u_if_addr,'mcs':last_embms.mcs}

    except embms.DoesNotExist:
        last_embms = None
        initial_data_embms = {}

    try:
        last_channel_dl = channel_dl.objects.latest('id')
        initial_data_channel_dl = {}

    except channel_dl.DoesNotExist:
        last_channel_dl = None
        initial_data_channel_dl = {}

    try:
        last_cfr = cfr.objects.latest('id')
        initial_data_cfr = {'enable':last_cfr.enable,'mode':last_cfr.mode,'manual_thres':last_cfr.manual_thres,
                            'strength':last_cfr.strength,'auto_target_papr':last_cfr.auto_target_papr,'ema_alpha':last_cfr.ema_alpha}

    except cfr.DoesNotExist:
        last_cfr = None
        initial_data_cfr = {}

    try:
        last_e2_agent = e2_agent.objects.latest('id')
        initial_data_e2_agent = {'enable':last_e2_agent.enable, 'ric_ip':last_e2_agent.ric_ip,'ric_port': last_e2_agent.ric_port,
            'ric_bind_ip': last_e2_agent.ric_bind_ip,'ric_bind_port': last_e2_agent.ric_bind_port,
            'max_ric_setup_retries':last_e2_agent.max_ric_setup_retries,'ric_connect_timer': last_e2_agent.ric_connect_timer}

    except e2_agent.DoesNotExist:
        last_e2_agent = None
        initial_data_e2_agent = {}

    try:
        last_expert = expert.objects.latest('id')
        initial_data_expert = {'pusch_max_its':last_expert.pusch_max_its,'nr_pusch_max_its':last_expert.nr_pusch_max_its,'pusch_8bit_decoder':last_expert.pusch_8bit_decoder,
                               'nof_phy_threads':last_expert.nof_phy_threads,'metrics_period_secs':last_expert.metrics_period_secs,'metrics_csv_enable':last_expert.metrics_csv_enable,
                               'metrics_csv_filename':last_expert.metrics_csv_filename,'report_json_enable':last_expert.report_json_enable,'report_json_filename':last_expert.report_json_filename,
                               'report_json_asn1_oct':last_expert.report_json_asn1_oct,'alarms_log_enable':last_expert.alarms_log_enable,'alarms_filename':last_expert.alarms_filename,
                               'tracing_enable':last_expert.tracing_enable,'tracing_filename':last_expert.tracing_filename,'tracing_buffcapacity':last_expert.tracing_buffcapacity,
                               'stdout_ts_enable':last_expert.stdout_ts_enable,'tx_amplitude':last_expert.tx_amplitude,'rrc_inactivity_timer':last_expert.rrc_inactivity_timer,
                               'max_mac_dl_kos':last_expert.max_mac_dl_kos,'max_mac_ul_kos':last_expert.max_mac_ul_kos,'max_prach_offset_us':last_expert.max_prach_offset_us,
                               'nof_prealloc_ues':last_expert.nof_prealloc_ues,'rlf_release_timer_ms':last_expert.rlf_release_timer_ms,'lcid_padding':last_expert.lcid_padding,
                               'eea_pref_list':last_expert.eea_pref_list,'eia_pref_list':last_expert.eia_pref_list,'gtpu_tunnel_timeout':last_expert.gtpu_tunnel_timeout,
                               'extended_cp':last_expert.extended_cp,'ts1_reloc_prep_timeout':last_expert.ts1_reloc_prep_timeout,'ts1_reloc_overall_timeout':last_expert.ts1_reloc_overall_timeout,
                               'rlf_min_ul_snr_estim':last_expert.rlf_min_ul_snr_estim,'s1_setup_max_retries':last_expert.s1_setup_max_retries,'s1_connect_timer':last_expert.s1_connect_timer,
                               'rx_gain_offset':last_expert.rx_gain_offset,'mac_prach_bi':last_expert.mac_prach_bi,'use_cedron_f_est_alg':last_expert.use_cedron_f_est_alg}

    except expert.DoesNotExist:
        last_expert = None
        initial_data_expert = {}

    form1 = enodeb_form(initial=initial_data_enodeb)
    form2 = enb_files_form(initial=initial_data_enb_files)
    form3 = rf_form(initial=initial_data_rf)
    form4 = pcap_form(initial=initial_data_pcap)
    form5 = log_form(initial=initial_data_log)
    form6 = scheduler_form(initial=initial_data_scheduler)
    form7 = slicin_form(initial=initial_data_slicin)
    form8 = embms_form(initial=initial_data_embms)
    #form9 = channel_dl_form(initial=initial_data_channel_dl)
    form10 = cfr_form(initial=initial_data_cfr)
    form11 = e2_agent_form(initial=initial_data_e2_agent)
    form12 = expert_form(initial=initial_data_expert)

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

                    results = modificar_enodeb(enb_id=ex, name= form_unsaved.name, mcc= form_unsaved.mcc, mnc=form_unsaved.mnc,
                                               mme_addr=form_unsaved.mme_addr,gtp_bind_addr=form_unsaved.gtp_bind_addr,
                                               gtp_advertise_addr=form_unsaved.gtp_advertise_addr, s1c_bind_addr=form_unsaved.s1c_bind_addr, s1c_bind_port=form_unsaved.s1c_bind_port,n_prb=form_unsaved.n_prb,
                                               nof_ports=form_unsaved.nof_ports,tm=form_unsaved.tm, p_a=form_unsaved.p_a)

                    form_unsaved.save()
                    print(results)              
                    mensaje1 = 'Ajustes corregidos exitosamente'
                else:
                    error1 = 'El id excede los 20 bits'
                
              
        elif 'submit_form2' in request.POST:
            form2 = enb_files_form(request.POST)
            if form2.is_valid():
                enb_files.objects.all().delete()

                form2.save()
                mensaje2 = 'Ajustes corregidos exitosamente'
            else:
                error2 = 'Error al guardar formulario'
        
        elif 'submit_form3' in request.POST:
            form3 = rf_form()
            if form3.is_valid():
                rf.objects.all().delete()

                form3.save()
                mensaje3 = 'Ajustes corregidos exitosamente'
            else:
                error3 = 'Error al guardar formulario'

        elif 'submit_form4' in request.POST:
            form4 = pcap_form()
            if form4.is_valid():
                pcap.objects.all().delete()

                form4.save()
                mensaje4 = 'Ajustes corregidos exitosamente'
            else:
                error4 = 'Error al guardar formulario'

        elif 'submit_form5' in request.POST:
            form5 = log_form()
            if form5.is_valid():
                log.objects.all().delete()

                form5.save()
                mensaje5 = 'Ajustes corregidos exitosamente'
            else:
                error5 = 'Error al guardar formulario'

        elif 'submit_form6' in request.POST:
            form6 = scheduler_form()
            if form6.is_valid():
                scheduler.objects.all().delete()

                form6.save()
                mensaje6 = 'Ajustes corregidos exitosamente'
            else:
                error6 = 'Error al guardar formulario'

        elif 'submit_form7' in request.POST:
            form7 = slicin_form()
            if form7.is_valid():
                slicin.objects.all().delete()

                form7.save()
                mensaje7 = 'Ajustes corregidos exitosamente'
            else:
                error7 = 'Error al guardar formulario'

        elif 'submit_form8' in request.POST:
            form8 = embms_form()
            if form8.is_valid():
                embms.objects.all().delete()

                form8.save()
                mensaje8 = 'Ajustes corregidos exitosamente'
            else:
                error8 = 'Error al guardar formulario'

        #elif 'submit_form9' in request.POST:
            #form9 = channel_dl_form()
            #if form9.is_valid():
                #channel_dl.objects.all().delete()

                #form9.save()
                #mensaje9 = 'Ajustes corregidos exitosamente'
            #else:
                #error9 = 'Error al guardar formulario'

        elif 'submit_form10' in request.POST:
            form10 = cfr_form()
            if form10.is_valid():
                cfr.objects.all().delete()

                form10.save()
                mensaje10 = 'Ajustes corregidos exitosamente'
            else:
                error10 = 'Error al guardar formulario'

        elif 'submit_form11' in request.POST:
            form11 = e2_agent_form()
            if form11.is_valid():
                e2_agent.objects.all().delete()

                form11.save()
                mensaje11 = 'Ajustes corregidos exitosamente'
            else:
                error11 = 'Error al guardar formulario'

        elif 'submit_form12' in request.POST:
            form12 = expert_form()
            if form12.is_valid():
                expert.objects.all().delete()

                form12.save()
                mensaje12 = 'Ajustes corregidos exitosamente' 
            else:
                error12 = 'Error al guardar formulario'               
        
        elif 'submit_form13' in request.POST:
            form12 = expert_form()
            if form12.is_valid():
                expert.objects.all().delete()

                form12.save()
                mensaje12 = 'Ajustes corregidos exitosamente' 
            else:
                error12 = 'Error al guardar formulario'
    return render(request, 'api/principal.html', {
        'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4,'form5':form5,'form6':form6,'form7':form7,
        'form8':form8,'form10':form10,'form11':form11,'form12':form12,#'form9':form9,
        'error1':error1, 'error2':error2, 'error3':error3,'error4':error4,'error5':error5,'error6':error6,'error7':error7,
        'error8':error8,'error9':error9,'error10':error10,'error11':error11,'error12':error12,
        'mensaje1':mensaje1, 'mensaje2':mensaje2, 'mensaje3':mensaje3 , 'mensaje4': mensaje4,'mensaje5': mensaje5,
        'mensaje6': mensaje6,'mensaje7': mensaje7,'mensaje8': mensaje8,'mensaje9': mensaje9,'mensaje10': mensaje10,'mensaje11': mensaje11,'mensaje12': mensaje12,
    } )

from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import re

# Create yours forms here
def convertir_a_hexadecimal(x):    
        numero = int(x)    
        hexadecimal = hex(numero)
        if len(hexadecimal) > 5:
            return -1
        else:
            return hexadecimal

class enodeb_form(forms.ModelForm):  
    country_code = [
        ('1', '+1 EE.UU'),
        ('52', '+52 Mexico'),
        ('34', '+34 España'),
        ('44', '+44 UK'),
        ('49', '+49 Alemania'),
        ('33', '+33 Francia'),
        ('39', '+39 Italia'),
        ('55', '+55 Brasil'),
    ]
    mobile_network_code = [
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
    ]
    physical_resource_blocks = [
        ('6', '6'),
        ('15', '15'),
        ('25', '25'),
        ('50', '50'),
        ('75', '75'),
        ('100', '100'),
    ]
    nof_ports_op = [
        ('1', '1'),
        ('2', '2'),
    ]
    tm_op = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    s1c_bind_port_op = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]

    enb_id = forms.IntegerField(label='Id del enodeb')
    mcc = forms.ChoiceField(choices=country_code, label='Código de pais')
    mnc = forms.ChoiceField(choices=mobile_network_code, label='Código de red')
    n_prb = forms.ChoiceField(choices=physical_resource_blocks, label='Número de bloques de recursos físicos')
    nof_ports = forms.ChoiceField(choices=nof_ports_op, label='Número de puertos Tx (Puerto predeterminado 1)')
    tm = forms.ChoiceField(choices=tm_op, label='Modo de transmision 1-4 (Predeterminado TM1)')
    s1c_bind_port = forms.ChoiceField(choices=s1c_bind_port_op, label='Puerto de origen para conección S1AP (0 significa cualquiera)')

    mme_addr = forms.GenericIPAddressField(protocol='both', unpack_ipv4=False, label = 'Dirección IP de MME para conección S1')
    gtp_bind_addr = forms.GenericIPAddressField(protocol='both', unpack_ipv4=False, label = 'Dirección IP local para vincular conección GTP')
    gtp_advertise_addr = forms.GenericIPAddressField(protocol='both', unpack_ipv4=False, label = 'Dirección IP de eNB para anunciar el tráfico DL GTP-U')
    s1c_bind_addr = forms.GenericIPAddressField(protocol='both', unpack_ipv4=False, label = 'Direccion IP local para vincular conección S1AP')

    class Meta:
        model = enodeb
        fields = ['enb_id', 'mcc', 'mnc', 'mme_addr', 'gtp_bind_addr', 'gtp_advertise_addr', 's1c_bind_addr',
                  's1c_bind_port', 'n_prb', 'tm', 'nof_ports']
        
        def __init__(self, *args, **kwargs):
            super(enodeb_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class enb_files_form(forms.ModelForm):
    
    class Meta:
        model = enb_files
        fields = ['sib_config', 'rr_config', 'rb_config']        
        labels = {
            'sib_config': 'Ruta al archivo de configuración SIB1, SIB2 y SIB3',
            'rr_config': 'Ruta al archivo de configuracion de recursos de radio',
            'rb_config': 'Ruta al archivo de configuración SRB/DRB',
        }

        def clean_sib(self):
            sib_config = self.cleaned_data['sib_config']
                        
            regex = re.compile(r'^[A-Za-z]:[\\/](?:[^\\/:*?"<>|\r\n]+[\\/])*[^\\/:*?"<>|\r\n]*$')

            if not regex.match(sib_config):
                raise forms.ValidationError('Introduce una ruta válida')
            return sib_config
        
        def clean_rr(self):            
            rr_config = self.cleaned_data['rr_config']
                        
            regex = re.compile(r'^[A-Za-z]:[\\/](?:[^\\/:*?"<>|\r\n]+[\\/])*[^\\/:*?"<>|\r\n]*$')

            if not regex.match(rr_config):
                raise forms.ValidationError('Introduce una ruta válida')
            return rr_config
        
        def clean_rb(self):
            rb_config = self.cleaned_data['rb_config']
            
            regex = re.compile(r'^[A-Za-z]:[\\/](?:[^\\/:*?"<>|\r\n]+[\\/])*[^\\/:*?"<>|\r\n]*$')

            if not regex.match(rb_config):
                raise forms.ValidationError('Introduce una ruta válida')
            return rb_config
                
        def __init__(self, *args, **kwargs):
            super(enb_files_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))      
               
class rf_form(forms.ModelForm):
    class Meta:
        model = rf
        fields = ['dl_earfcn', 'tx_gain', 'rx_gain', 'dl_freq', 'ul_freq', 'device_name', 'device_args', 'time_adv_nsamples']        
        labels = {
            'dl_earfcn': 'Código EARFCN para DL (Solo válido si hay una sola celda)',
            'tx_gain': 'Ganancia de transmisión (dB)',
            'rx_gain': 'Ganancia de recepción (dB)',
            'dl_freq': 'Frecuencia DL correspondiente a EARFCN',
            'ul_freq': 'Frecuencia UL correspondiente a EARFCN',
            'device_name': 'Nombre del controlador de dispositivo',
            'device_args': 'Argumentos del controlador de dispositivo',
            'time_adv_nsamples': 'Avance de tiempo de transmisión (En número de muestras)',
        }
                
        def __init__(self, *args, **kwargs):
            super(rf_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class pcap_form(forms.ModelForm):
    class Meta:
        model = pcap
        fields = ['enable', 'filename', 'nr_filename', 's1ap_enable', 's1ap_filename',
                  'mac_net_enable', 'bind_ip', 'bind_port', 'client_ip', 'client_port']        
        labels = {
            'enable': 'Habilitar capturas de paquetes MAC',
            'filename': 'Ruta del archivo para capturas de paquetes MAC LTE',
            'nr_filename': 'Ruta del archivo para capturas de paquetes MAC NR',
            's1ap_enable': 'Habilitar/Deshabilitar la captura de S1AP',
            's1ap_filename': 'Nombre del archivo para guardar las capturas de S1AP',
            'mac_net_enable': 'Habilitar capturas de paquete MAC',
            'bind_ip': 'Dirección IP de enlace para rastreo de red MAC',
            'bind_port': 'Puerto de enlace para rastreo de red MAC',
            'client_ip': 'Dirección IP del cliente para rastreo de red MAC',
            'client_port': 'Puerto del cliente para rastreo de red MAC',
        }
        def __init__(self, *args, **kwargs):
            super(pcap_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class log_form(forms.ModelForm):
    class Meta:
        model = log
        fields = ['all_level', 'all_hex_limit', 'filename', 'file_max_size', 'gui_enable',]        
        labels = {
            'all_level': 'Nivel de registro para todas las capas',
            'all_hex_limit': 'Limite de volcado para todas las capas',
            'filename': 'Ruta del archivo para la salida del registro',
            'file_max_size': 'Tamaño máximo del archivo de registro (kilobytes)',
            'gui_enable': 'Habilitar deshabilitar interfáz gráfica (GUI)',            
        }
        def __init__(self, *args, **kwargs):
            super(log_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class scheduler_form(forms.ModelForm):
    class Meta:
        model = scheduler
        fields = ['policy', 'policy_args', 'min_aggr_level', 'max_aggr_level', 'adaptive_aggr_level',
                  'pdsch_mcs', 'pdsch_max_mcs', 'pusch_mcs', 'pusch_max_mcs', 'min_nof_ctrl_symbols',
                  'max_nof_ctrl_symbols', 'pucch_multiplex_enable', 'pucch_harq_max_rb',
                  'target_bler','max_delta_dl_cqi', 'max_delta_ul_snr', 'adaptive_dl_mcs_step_size',
                  'adaptive_ul_mcs_step_size', 'min_tpc_tti_interval',
                  'ul_snr_avg_alpha', 'init_ul_snr_value',
                  'init_dl_cqi', 'max_sib_coderate', 'pdcch_cqi_offset', 'nr_pdsch_mcs', 'nr_pusch_mcs',]        
        labels = {
            'policy': 'Politica de programación',
            'policy_args': 'Cantidad de argumentos de Politica de programación',
            'min_aggr_level': 'Nivel mínimo de agragación',
            'max_aggr_level': 'Nivel máximo de agragación',
            'adaptive_aggr_level': 'Habilitar nivel de agragación adaptativo',
            'pdsch_mcs': 'Índice de MCS PDSCH',
            'pdsch_max_mcs': 'Límite máximo de MCS PDSCH',
            'pusch_mcs': 'Índice de MCS PUSCH',
            'pusch_max_mcs': 'Límite máximo de MCS PUSCH',
            'min_nof_ctrl_symbols': 'Número mínimo de símbolos de control',
            'max_nof_ctrl_symbols': 'Número máximo de símbolos de control',
            'pucch_multiplex_enable': 'Permitir que HARQ PUCCH colisione con PUSCH y PDCCH',
            'pucch_harq_max_rb': 'Máximo número de RB para HARQ PUCCH',
            'target_bler': 'BLER objetivo',
            'max_delta_dl_cqi': 'Cambio máximo en CQI para DL',
            'max_delta_ul_snr': 'Cambio máximo en SNR para UL',
            'adaptive_dl_mcs_step_size': 'Tamaño de paso para DL MCS adaptativo',
            'adaptive_ul_mcs_step_size': 'Tamaño de paso para UL MCS adaptativo',
            'min_tpc_tti_interval': 'Intervalo mínimo de TTI para actualizaciones de TCP',
            'ul_snr_avg_alpha': 'Coeficiente alfa promedio para SNR UL',
            'init_ul_snr_value': 'Valor inicial de SNR UL',
            'init_dl_cqi': 'Valor inicial de CQI',
            'max_sib_coderate': 'Límie superior de SIB y RAR',
            'pdcch_cqi_offset': 'Desplazamiento de CQI para SINR',
            'nr_pdsch_mcs': 'Índice de MCS PDSCH NR',
            'nr_pusch_mcs': 'Índice de MCS PUSCH NR',            
        }
        def __init__(self, *args, **kwargs):
            super(scheduler_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class slicin_form(forms.ModelForm):
    class Meta:
        model = slicin
        fields = ['enable_eMBB', 'enable_URLLC', 'enable_MIoT', 'eMBB_sd', 'URLLC_sd', 'MIoT_sd',]        
        labels = {
            'enable_eMBB': 'Habilitar banda ancha móvil mejorada',
            'enable_URLLC': 'Habilitar comunicaciones ultraconfiables y de baja latencia',
            'enable_MIoT': 'Habilitar internet de las cosas masivo',
            'eMBB_sd': 'Diferenciador de slice para banda ancha móvil mejorada',
            'URLLC_sd': 'Diferenciador de slice para comunicaciones ultra confiables y de baja latencia',
            'MIoT_sd': 'Diferenciador de slice para Internet de las cosas masivo',            
        }
        def __init__(self, *args, **kwargs):
            super(slicin_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class embms_form(forms.ModelForm):
    class Meta:
        model = embms
        fields = ['enable', 'm1u_multiaddr', 'm1u_if_addr', 'mcs',]        
        labels = {
            'enable': 'Habilitar transmisión MBMS en el eNB',
            'm1u_multiaddr': 'Dirección multicast a la que se registrará el socket M1-U',
            'm1u_if_addr': 'Dirección de interfaz que escuchará el M1-U para multicast',
            'mcs': 'Esquema de modulación y codificación para el tráfico MBMS',          
        }
        def __init__(self, *args, **kwargs):
            super(embms_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))
'''
class channel_dl_form(forms.ModelForm): #Falta por crear este y utiliza JSonFields
    class Meta:
        model = channel_dl
        fields = ['', '', '', '', '',]        
        labels = {
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',            
        }
        def __init__(self, *args, **kwargs):
            super(channel_dl_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))
'''
class cfr_form(forms.ModelForm):
    class Meta:
        model = cfr
        fields = ['enable', 'mode', 'manual_thres', 'strength', 'auto_target_papr', 'ema_alpha',]        
        labels = {
            'enable': 'Habilitar/Deshabilitar el CFR',
            'mode': 'Modo de operación del CFR (manual/auto_ema/auto_cma)',
            'manual_thres': 'Umbral de recorte manual fijo para modo CFR manual',
            'strength': 'Relacion entre la señal limitada en amplitud y la señal no procesada (0-1)',
            'auto_target_papr': 'Objetivo de PAPR de la señal en modos de CFR automáticos',
            'ema_alpha': 'Coeficiente alfa para el promedio de potencia en modo auto_ema',            
        }
        def __init__(self, *args, **kwargs):
            super(cfr_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class e2_agent_form(forms.ModelForm):
    class Meta:
        model = e2_agent
        fields = ['enable', 'ric_ip', 'ric_port', 'ric_bind_ip', 'ric_bind_port', 'max_ric_setup_retries',
                  'ric_connect_timer',]        
        labels = {
            'enable': 'Habilitar/deshabilitar e2_agent',
            'ric_ip': 'Dirección IP del controlador RIC',
            'ric_port': 'Puerto del controlador RIC',
            'ric_bind_ip': 'Dirección IP local para la conexión RIC',
            'ric_bind_port': 'Puerto local para lo cenexión RIC',
            'max_ric_setup_retries': 'Número máximo de intentos para establecer la conexión RIC',
            'ric_connect_timer': 'Tiempo de reintento de conexión RIC (s)',            
        }
        def __init__(self, *args, **kwargs):
            super(e2_agent_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

class expert_form(forms.ModelForm):
    class Meta:
        model = expert
        fields = ['pusch_max_its', 'nr_pusch_max_its', 'pusch_8bit_decoder', 'nof_phy_threads', 'metrics_period_secs',
                  'metrics_csv_enable', 'metrics_csv_filename', 'report_json_enable', 'report_json_filename', 'report_json_asn1_oct',
                  'alarms_log_enable', 'alarms_filename', 'tracing_enable', 'tracing_filename', 'tracing_buffcapacity',
                  'stdout_ts_enable', 'tx_amplitude', 'rrc_inactivity_timer', 'max_mac_dl_kos', 'max_mac_ul_kos',
                  'max_prach_offset_us', 'nof_prealloc_ues', 'rlf_release_timer_ms', 'lcid_padding', 'eea_pref_list',
                  'eia_pref_list', 'gtpu_tunnel_timeout', 'extended_cp', 'ts1_reloc_prep_timeout', 'ts1_reloc_overall_timeout',
                  'rlf_min_ul_snr_estim', 's1_setup_max_retries', 's1_connect_timer', 'rx_gain_offset', 'mac_prach_bi',
                  'use_cedron_f_est_alg',]        
        labels = {
            'pusch_max_its': 'Número máximo de iteraciones del decodificador turbo',
            'nr_pusch_max_its': 'Número máximo de iteraciones LDPC para NR',
            'pusch_8bit_decoder': 'Representación LLR y cálculo de enrejado del decodificador turbo',
            'nof_phy_threads': 'Seleccionar la cantidad de subprocesos (Experimental)',
            'metrics_period_secs': 'Periodo de solicitud de metrica eNB',
            'metrics_csv_enable': 'Escribir metricas eNB en un archivo CSV',
            'metrics_csv_filename': 'Ruta del archivo que se utilizará para las metricas',
            'report_json_enable': 'Escribir informe eNB en archivo JSON',
            'report_json_filename': 'Ruta del archivo JSON del informe',
            'report_json_asn1_oct': 'Imprimir mensajes ASN1 codificados como una cadena de octetos en archivo de infome JSON',
            'alarms_log_enable': 'Habilitar registro de alarmas',
            'alarms_filename': 'Nombre del archivo de registro de alarmas',
            'tracing_enable': 'Escribir informacion de seguimiento del código fuente',
            'tracing_filename': 'Ruta del archivo de seguimiento del código fuente',
            'tracing_buffcapacity': 'Cápacidad máxima que el marco de seguimiento puede almacenar (bytes)',
            'stdout_ts_enable': 'Imprimir maraca de tiempo en stdout',
            'tx_amplitude': 'Factor de amplitud de transmisión',
            'rrc_inactivity_timer': 'Tiempo de espera de inactividad para eliminar contexto UE de RRC',
            'max_mac_dl_kos': 'Número máximo de KO consecutivos en DL',
            'max_mac_ul_kos': 'Número máximo de KO consecutivos en UL',
            'max_prach_offset_us': 'Desplazamiento máximo permitido de RACH',
            'nof_prealloc_ues': 'Número de recursos de memoria UE',
            'rlf_release_timer_ms': 'Time taken by eNB to release UE context after it detects a RLF',
            'lcid_padding': 'Lcid padding',
            'eea_pref_list': 'Lista de preferencias ordenadas para seleccion de lgoritmos de cifrado EEA',
            'eia_pref_list': 'Lista de preferencias ordenadas para seleccion de lgoritmos de cifrado EIA',
            'gtpu_tunnel_timeout': 'Time that GTPU takes to release indirect forwarding tunnel since the last received GTPU PDU (0 for no timer)',
            'extended_cp': 'Extended cp',
            'ts1_reloc_prep_timeout': 'S1AP TS 36.413 TS1RelocPrep Expiry Timeout value in milliseconds',
            'ts1_reloc_overall_timeout': 'S1AP TS 36.413 TS1RelocOverall Expiry Timeout value in milliseconds',
            'rlf_min_ul_snr_estim': 'SNR threshold in dB below which the enb is notified with RLF ko',
            's1_setup_max_retries': 'Maximum amount of retries to setup the S1AP connection.',
            's1_connect_timer': 'Connection Retry Timer for S1 connection (seconds)',
            'rx_gain_offset': 'Desplazamiento de ganancia RX',
            'mac_prach_bi': 'MAC prach bi',
            'use_cedron_f_est_alg': 'Utilizar o no algoritmo cedron para la estimacion de TA',           
        }
        def __init__(self, *args, **kwargs):
            super(expert_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))

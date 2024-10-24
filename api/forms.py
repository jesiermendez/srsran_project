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
            'dl_earfcn': '3350 EARFCN code for DL (only valid if a single cell is configured in rr.conf)',
            'tx_gain': '80 Transmit gain (dB).',
            'rx_gain': '40',
            'dl_freq': 'Override DL frequency corresponding to dl_earfcn',
            'ul_freq': 'Override UL frequency corresponding to dl_earfcn (must be set if dl_freq is set)',
            'device_name': 'Device driver family Supported options: "auto" (uses first driver found)',
            'device_args': 'Arguments for the device driver. Options are "auto" or any string.',
            'time_adv_nsamples': 'Transmission time advance (in number of samples) to compensate for RF delay',
        }
                
        def __init__(self, *args, **kwargs):
            super(rf_form, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'form-vertical'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.add_input(Submit('submit', 'Guardar'))




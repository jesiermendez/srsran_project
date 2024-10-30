import subprocess

#Aqui comienza a trabajar en linux

def modificar_enodeb(enb_id, name, mcc, mnc, mme_addr, gtp_bind_addr, gtp_advertise_addr, s1c_bind_addr,
                     s1c_bind_port, n_prb, nof_ports, tm, p_a):
    scripts = [f'srsenb --enb.enb_id arg={enb_id}', f'srsenb --enb.name arg={name}',f'srsenb --enb.mcc arg={mcc}',
               f'srsenb --enb.mnc arg={mnc}',f'srsenb --enb.mme_addr arg={mme_addr}',f'srsenb --enb.gtp_bind_addr arg={gtp_bind_addr}',
               f'srsenb --enb.gtp_advertise_addr arg={gtp_advertise_addr}',f'srsenb --enb.s1c_bind_addr arg={s1c_bind_addr}',
               f'srsenb --enb.s1c_bind_port arg={s1c_bind_port}',f'srsenb --enb.n_prb arg={n_prb}',f'srsenb --enb.nof_ports arg={nof_ports}',
               f'srsenb --enb.tm arg={tm}',f'srsenb --enb.p_a arg={p_a}']
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_enb_files(sib_config, rr_config, rb_config):
    scripts = [f'srsenb --enb_files.sib_config arg={sib_config}',f'srsenb --enb_files.rr_config arg={rr_config}',
               f'srsenb --enb_files.rb_config arg={rb_config}']
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_rf(dl_earfcn, srate, rx_gain, tx_gain, tx_gain0, tx_gain1, tx_gain2, tx_gain3, tx_gain4,
                 dl_freq, ul_freq, device_name, device_args, time_adv_nsamples):
    scripts = [f'srsenb --rf.dl_earfcn arg={dl_earfcn}',f'srsenb --rf.srate arg={srate}',f'srsenb --rf.rx_gain arg={rx_gain}',
               f'srsenb --rf.tx_gain arg={tx_gain}',f'srsenb --rf.tx_gain[0] arg={tx_gain0}',f'srsenb --rf.tx_gain[1] arg={tx_gain1}',
               f'srsenb --rf.tx_gain[2] arg={tx_gain2}',f'srsenb --rf.tx_gain[3] arg={tx_gain3}',f'srsenb --rf.tx_gain[4] arg={tx_gain4}',
               f'srsenb --rf.dl_freq arg={dl_freq}',f'srsenb --rf.ul_freq arg={ul_freq}',f'srsenb --rf.device_name arg={device_name}',
               f'srsenb --rf.device_args arg={device_args}',f'srsenb --rf.time_adv_nsamples arg={time_adv_nsamples}']
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_gui(enable):
    script = f'srsenb --gui.enable arg={enable}'
    result = subprocess.run(script, capture_output=True, text=True)
    return result

def modificar_pcap(filename, nr_filename, s1ap_enable, s1ap_filename, ngap_enable, ngap_filename, mac_net_enable,
                   bind_ip, bind_port, client_ip, client_port, enable):
    scripts = [f'srsenb --pcap.filename arg={filename}',f'srsenb --pcap.nr_filename arg={nr_filename}',f'srsenb --pcap.s1ap_enable arg={s1ap_enable}',
               f'srsenb --pcap.s1ap_filename arg={s1ap_filename}',f'srsenb --pcap.ngap_enable arg={ngap_enable}',f'srsenb --pcap.ngap_filename arg={ngap_filename}',
               f'srsenb --pcap.mac_net_enable arg={mac_net_enable}',f'srsenb --pcap.bind_ip arg={bind_ip}',f'srsenb --pcap.bind_port arg={bind_port}',
               f'srsenb --pcap.client_ip arg={client_ip}',f'srsenb --pcap.client_port arg={client_port}',f'srsenb --pcap.enable arg={enable}']
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_log(rf_level, phy_level, phy_hex_limit, phy_lib_level, mac_level, mac_hex_limit, rlc_level, rlc_hex_limit, pdcp_level,
                  pdcp_hex_limit, rrc_level, rrc_hex_limit, gtpu_level, gtpu_hex_limit, s1ap_level, s1ap_hex_limit, stack_level,
                  stack_hex_limit, all_level, all_hex_limit, filename, file_max_size):
    scripts = [f'srsenb --log.rf_level arg={rf_level}',f'srsenb --log.phy_level arg={phy_level}',f'srsenb --log.phy_hex_limit arg={phy_hex_limit}',
               f'srsenb --log.phy_lib_level arg={phy_lib_level}',f'srsenb --log.mac_level arg={mac_level}',f'srsenb --log.mac_hex_limit arg={mac_hex_limit}',
               f'srsenb --log.rlc_level arg={rlc_level}',f'srsenb --log.rlc_hex_limit arg={rlc_hex_limit}',f'srsenb --log.pdcp_level arg={pdcp_level}',
               f'srsenb --log.pdcp_hex_limit arg={pdcp_hex_limit}',f'srsenb --log.rrc_level arg={rrc_level}',f'srsenb --log.rrc_hex_limit arg={rrc_hex_limit}',
               f'srsenb --log.gtpu_level arg={gtpu_level}',f'srsenb --log.gtpu_hex_limit arg={gtpu_hex_limit}',f'srsenb --log.s1ap_level arg={s1ap_level}',
               f'srsenb --log.s1ap_hex_limit arg={s1ap_hex_limit}',f'srsenb --log.stack_level arg={stack_level}',f'srsenb --log.stack_hex_limit arg={stack_hex_limit}',
               f'srsenb --log.all_level arg={all_level}',f'srsenb --log.all_hex_limit arg={all_hex_limit}',f'srsenb --log.filename arg={filename}',
               f'srsenb --log.file_max_size arg={file_max_size}']
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_scheduler(nr_pdsch_mcs, policy, policy_args, pdsch_mcs, pdsch_max_mcs, pusch_mcs, pusch_max_mcs, min_aggr_level, max_aggr_level, adaptive_aggr_level, max_nof_ctrl_symbols, min_nof_ctrl_symbols,
                        pucch_multiplex_enable, pucch_harq_max_rb, target_bler, max_delta_dl_cqi, max_delta_ul_snr, adaptive_dl_mcs_step_size, adaptive_ul_mcs_step_size, min_tpc_tti_interval, ul_snr_avg_alpha,
                        init_ul_snr_value, init_dl_cqi, max_sib_coderate, pdcch_cqi_offset, nr_pusch_mcs):
    scripts = [f'srsenb --scheduler.nr_pdsch_mcs arg={nr_pdsch_mcs}',f'srsenb --scheduler.policy arg={policy}',f'srsenb --scheduler.policy_args arg={policy_args}',
               f'srsenb --scheduler.pdsch_mcs arg={pdsch_mcs}',f'srsenb --scheduler.pdsch_max_mcs arg={pdsch_max_mcs}',f'srsenb --scheduler.pusch_mcs arg={pusch_mcs}',
               f'srsenb --scheduler.pusch_max_mcs arg={pusch_max_mcs}',f'srsenb --scheduler.min_aggr_level arg={min_aggr_level}',f'srsenb --scheduler.max_aggr_level arg={max_aggr_level}',
               f'srsenb --scheduler.adaptive_aggr_level arg={adaptive_aggr_level}',f'srsenb --scheduler.max_nof_ctrl_symbols arg={max_nof_ctrl_symbols}',f'srsenb --scheduler.min_nof_ctrl_symbols arg={min_nof_ctrl_symbols}',
               f'srsenb --scheduler.pucch_multiplex_enable arg={pucch_multiplex_enable}',f'srsenb --scheduler.pucch_harq_max_rb arg={pucch_harq_max_rb}',f'srsenb --scheduler.target_bler arg={target_bler}',
               f'srsenb --scheduler.max_delta_dl_cqi arg={max_delta_dl_cqi}',f'srsenb --scheduler.max_delta_ul_snr arg={max_delta_ul_snr}',f'srsenb --scheduler.adaptive_dl_mcs_step_size arg={adaptive_dl_mcs_step_size}',
               f'srsenb --scheduler.adaptive_ul_mcs_step_size arg={adaptive_ul_mcs_step_size}',f'srsenb --scheduler.min_tpc_tti_interval arg={min_tpc_tti_interval}',f'--scheduler.ul_snr_avg_alpha arg={ul_snr_avg_alpha}',
               f'srsenb --scheduler.init_ul_snr_value arg={init_ul_snr_value}',f'srsenb --scheduler.init_dl_cqi arg={init_dl_cqi}',f'srsenb --scheduler.max_sib_coderate arg={max_sib_coderate}',
               f'srsenb --scheduler.pdcch_cqi_offset arg={pdcch_cqi_offset}',f'srsenb --scheduler.nr_pusch_mcs arg={nr_pusch_mcs}']
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_slicin(enable_eMBB, enable_URLLC, enable_MIoT, eMBB_sd, URLLC_sd, MIoT_sd):
    scripts = [f'srsenb --slicing.enable_eMBB arg={enable_eMBB}',f'srsenb --slicing.enable_URLLC arg={enable_URLLC}',f'srsenb --slicing.enable_MIoT arg={enable_MIoT}',
               f'srsenb --slicing.eMBB_sd arg={eMBB_sd}',f'srsenb --slicing.URLLC_sd arg={URLLC_sd}',f'srsenb --slicing.MIoT_sd arg={MIoT_sd}']
    
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_embms(enable, m1u_multiaddr, m1u_if_addr, mcs):
    scripts = [f'srsenb --embms.enable arg={enable}',f'srsenb --embms.m1u_multiaddr arg={m1u_multiaddr}',
               f'srsenb --embms.m1u_if_addr arg={m1u_if_addr}',f'srsenb --embms.mcs arg={mcs}']
    
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_channel_dl(dl_enable, dl_awgn_enable, dl_awgn_snr, dl_fading_enable, dl_fading_model, dl_delay_enable, dl_delay_period_s, dl_delay_init_time_s,
                         dl_delay_maximum_us, dl_delay_minimum_us, dl_rlf_enable, dl_rlf_t_on_ms, dl_rlf_t_off_ms, dl_hst_enable, dl_hst_period_s,
                         dl_hst_fd_hz, dl_hst_init_time_s):
    scripts = [f'srsenb --channel.dl.enable arg={dl_enable}',f'srsenb --channel.dl.awgn.enable arg={dl_awgn_enable}',
               f'srsenb --channel.dl.awgn.snr arg={dl_awgn_snr}',f'srsenb --channel.dl.fading.enable arg={dl_fading_enable}',f'srsenb --channel.dl.fading.model arg={dl_fading_model}', 
               f'srsenb --channel.dl.delay.enable arg={dl_delay_enable}',f'srsenb --channel.dl.delay.period_s arg={dl_delay_period_s}',f'srsenb --channel.dl.delay.init_time_s arg={dl_delay_init_time_s}',
               f'srsenb --channel.dl.delay.maximum_us arg={dl_delay_maximum_us}',f'srsenb --channel.dl.delay.minimum_us arg={dl_delay_minimum_us}',f'srsenb --channel.dl.rlf.enable arg={dl_rlf_enable}',
               f'srsenb --channel.dl.rlf.t_on_ms arg={dl_rlf_t_on_ms}',f'srsenb --channel.dl.rlf.t_off_ms arg={dl_rlf_t_off_ms}',f'srsenb --channel.dl.hst.enable arg={dl_hst_enable}',
               f'srsenb --channel.dl.hst.period_s arg={dl_hst_period_s}',f'srsenb --channel.dl.hst.fd_hz arg={dl_hst_fd_hz}',f'srsenb --channel.dl.hst.init_time_s arg={dl_hst_init_time_s}']
    
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_chanel_ul(ul_enable, ul_awgn_enable, ul_awgn_signal_power, ul_awgn_snr, ul_fading_enable, ul_fading_model, ul_delay_enable, ul_delay_period_s, ul_delay_init_time_s,
                        ul_delay_maximum_us, ul_delay_minimum_us, ul_rlf_enable, ul_rlf_t_on_ms, ul_rlf_t_off_ms, ul_hst_enable, ul_hst_period_s, ul_hst_fd_hz, ul_hst_init_time_s):
    scripts = [f'srsenb --channel.ul.enable arg={ul_enable}',f'srsenb --channel.ul.awgn.enable arg={ul_awgn_enable}',f'srsenb --channel.ul.awgn.signal_power arg={ul_awgn_signal_power}',
               f'srsenb --channel.ul.awgn.snr arg={ul_awgn_snr}',f'srsenb --channel.ul.fading.enable arg={ul_fading_enable}',f'srsenb --channel.ul.fading.model arg={ul_fading_model}',
               f'srsenb --channel.ul.delay.enable arg={ul_delay_enable}',f'srsenb --channel.ul.delay.period_s arg={ul_delay_period_s}',f'srsenb --channel.ul.delay.init_time_s arg={ul_delay_init_time_s}',
               f'srsenb --channel.ul.delay.maximum_us arg={ul_delay_maximum_us}',f'srsenb --channel.ul.delay.minimum_us arg={ul_delay_minimum_us}',f'srsenb --channel.ul.rlf.enable arg={ul_rlf_enable}',
               f'srsenb --channel.ul.rlf.t_on_ms arg={ul_rlf_t_on_ms}',f'srsenb --channel.ul.rlf.t_off_ms arg={ul_rlf_t_off_ms}',f'srsenb --channel.ul.hst.enable arg={ul_hst_enable}',
               f'srsenb --channel.ul.hst.period_s arg={ul_hst_period_s}',f'srsenb --channel.ul.hst.fd_hz arg={ul_hst_fd_hz}',f'srsenb --channel.ul.hst.init_time_s arg={ul_hst_init_time_s}']
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_cfr(enable, mode, manual_thres, strength, auto_target_papr, ema_alpha):
    scripts = [f'srsenb --cfr.enable arg={enable}',f'srsenb --cfr.mode arg={mode}',f'srsenb --cfr.manual_thres arg={manual_thres}',
               f'srsenb --cfr.strength arg={strength}',f'srsenb --cfr.auto_target_papr arg={auto_target_papr}',f'srsenb --cfr.ema_alpha arg={ema_alpha}']
    
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_e2_agent(enable, ric_ip, ric_port, ric_bind_ip, ric_bind_port, max_ric_setup_retries, ric_connect_timer):
    scripts = [f'srsenb --e2_agent.enable arg={enable}',f'srsenb --e2_agent.ric_ip arg={ric_ip}',f'srsenb --e2_agent.ric_port arg={ric_port}',
               f'srsenb --e2_agent.ric_bind_ip arg={ric_bind_ip}',f'srsenb --e2_agent.ric_bind_port arg={ric_bind_port}',
               f'srsenb --e2_agent.max_ric_setup_retries arg={max_ric_setup_retries}',f'srsenb --e2_agent.ric_connect_timer arg={ric_connect_timer}']
    
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

def modificar_expert(nr_pusch_max_its, metrics_csv_enable, metrics_csv_filename, pusch_max_its, pusch_8bit_decoder, pusch_meas_evm, tx_amplitude, nof_phy_threads,
                     nof_prach_threads, max_prach_offset_us, equalizer_mode, estimator_fil_w, lte_sample_rates, report_json_enable, report_json_filename, report_json_asn1_oct,
                     alarms_filename, tracing_enable, tracing_filename, tracing_buffcapacity, stdout_ts_enable, rrc_inactivity_timer, print_buffer_state, eea_pref_list,
                     eia_pref_list, nof_prealloc_ues, lcid_padding, max_mac_dl_kos, max_mac_ul_kos, gtpu_tunnel_timeout, rlf_release_timer_ms, extended_cp, ts1_reloc_prep_timeout,
                     ts1_reloc_overall_timeout, rlf_min_ul_snr_estim, max_s1_setup_retries, s1_connect_timer, sctp_reuse_addr, sctp_rto_max, sctp_init_max_attempts, sctp_max_init_timeo,
                     rx_gain_offset, mac_prach_bi, use_cedron_f_est_alg, metrics_period_secs, alarms_log_enable):
    scripts = [f'srsenb --expert.nr_pusch_max_its arg={nr_pusch_max_its}',f'srsenb --expert.metrics_csv_enable arg={metrics_csv_enable}',
               f'srsenb --expert.metrics_csv_filename arg={metrics_csv_filename}',f'srsenb --expert.pusch_max_its arg={pusch_max_its}',f'srsenb --expert.pusch_8bit_decoder arg={pusch_8bit_decoder}',
               f'srsenb --expert.pusch_meas_evm arg={pusch_meas_evm}',f'srsenb --expert.tx_amplitude arg={tx_amplitude}',f'srsenb --expert.nof_phy_threads arg={nof_phy_threads}',
               f'srsenb --expert.nof_prach_threads arg={nof_prach_threads}',f'srsenb --expert.max_prach_offset_us arg={max_prach_offset_us}',f'srsenb --expert.equalizer_mode arg={equalizer_mode}',
               f'srsenb --expert.estimator_fil_w arg={estimator_fil_w}',f'srsenb --expert.lte_sample_rates arg={lte_sample_rates}',f'srsenb --expert.report_json_enable arg={report_json_enable}',
               f'srsenb --expert.report_json_filename arg={report_json_filename}',f'srsenb --expert.report_json_asn1_oct arg={report_json_asn1_oct}',f'srsenb --expert.alarms_log_enable arg={alarms_log_enable}',
               f'srsenb --expert.alarms_filename arg={alarms_filename}',f'srsenb --expert.tracing_enable arg={tracing_enable}',f'srsenb --expert.tracing_filename arg={tracing_filename}',
               f'srsenb --expert.tracing_buffcapacity arg={tracing_buffcapacity}',f'srsenb --expert.stdout_ts_enable arg={stdout_ts_enable}',f'srsenb --expert.rrc_inactivity_timer arg={rrc_inactivity_timer}',               
               f'srsenb --expert.print_buffer_state arg={print_buffer_state}',f'srsenb --expert.eea_pref_list arg={eea_pref_list}',f'srsenb --expert.eia_pref_list arg={eia_pref_list}',
               f'srsenb --expert.nof_prealloc_ues arg={nof_prealloc_ues}',f'srsenb --expert.lcid_padding arg={lcid_padding}',f'srsenb --expert.max_mac_dl_kos arg={max_mac_dl_kos}',
               f'srsenb --expert.max_mac_ul_kos arg={max_mac_ul_kos}',f'srsenb --expert.gtpu_tunnel_timeout arg={gtpu_tunnel_timeout}',f'srsenb --expert.rlf_release_timer_ms arg={rlf_release_timer_ms}',
               f'srsenb --expert.extended_cp arg={extended_cp}',f'srsenb --expert.ts1_reloc_prep_timeout arg={ts1_reloc_prep_timeout}',f'srsenb --expert.ts1_reloc_overall_timeout arg={ts1_reloc_overall_timeout}',
               f'srsenb --expert.rlf_min_ul_snr_estim arg={rlf_min_ul_snr_estim}',f'srsenb --expert.max_s1_setup_retries arg={max_s1_setup_retries}',f'srsenb --expert.s1_connect_timer arg={s1_connect_timer}',
               f'srsenb --expert.sctp_reuse_addr arg={sctp_reuse_addr}',f'srsenb --expert.sctp_rto_max arg={sctp_rto_max}',f'srsenb --expert.sctp_init_max_attempts arg={sctp_init_max_attempts}',
               f'srsenb --expert.sctp_max_init_timeo arg={sctp_max_init_timeo}',f'srsenb --expert.rx_gain_offset arg={rx_gain_offset}',f'srsenb --expert.mac_prach_bi arg={mac_prach_bi}',               
               f'srsenb --expert.use_cedron_f_est_alg arg={use_cedron_f_est_alg}',f'srsenb --expert.metrics_period_secs arg={metrics_period_secs}']
    
    results = []

    for script in scripts:
        command = script.split()
        result = subprocess.run(command, capture_output=True, text=True)
        results.append(result.stdout)

    return results

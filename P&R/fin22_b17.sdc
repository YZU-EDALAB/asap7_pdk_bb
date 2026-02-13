set sdc_version 2.1
create_clock [get_ports {clock}] -name clock -period 8 -waveform {0 4}
set_clock_latency 4 [get_clocks {clock}]
set_input_delay -clock clock 4  [all_inputs]
set_output_delay 4 -clock clock [all_outputs]



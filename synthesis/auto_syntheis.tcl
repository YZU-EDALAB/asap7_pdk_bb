set LIRARY_NAME fin21
set VERILOG_NAME gpu
set CLOCK_PERIOD 25

set_app_var search_path ". /usr/cad/synopsys/synthesis/cur/libraries/syn /usr/cad/synopsys/synthesis/cur/dw/syn_ver /usr/cad/synopsys/synthesis/cur/dw/sim_ver /home1st/s80307330/finFlex/synthesis/" 
set_app_var link_library "/home1st/PUBLIC/synthesis/linkLibrary/75T.db"
read_file -format verilog {/home1st/PUBLIC/synthesis/verilog/gpu.v}
current_design [get_designs ${VERILOG_NAME}]
set_app_var target_library  "${LIRARY_NAME}.db"
create_clock [get_ports {clock}] -name clock -period ${CLOCK_PERIOD}
set_max_fanout 10 ${VERILOG_NAME}
# set_wire_load_model -name verySmall -library ALL_M_75t
ungroup -all -flatten
# set_dont_use { 
# }
compile_ultra

 
# Export timing path report
# ./Log (create folder ) b17_1p9_path.timing(create file name)
redirect -append ./Timing/${LIRARY_NAME}_${VERILOG_NAME}_${CLOCK_PERIOD}.timing { report_timing -path full -delay max -nworst 1 -max_paths 1 -significant_digits 3 -sort_by group }


# Export the cell used
redirect -append ./Cells/${LIRARY_NAME}_${VERILOG_NAME}_${CLOCK_PERIOD}.cell { report_reference -hierarchy }

# Export power
redirect -append ./Power/${LIRARY_NAME}_${VERILOG_NAME}_${CLOCK_PERIOD}.power { report_power }

# Export the .v file
write -format verilog -output ./Verilog/${LIRARY_NAME}_${VERILOG_NAME}_${CLOCK_PERIOD}.v
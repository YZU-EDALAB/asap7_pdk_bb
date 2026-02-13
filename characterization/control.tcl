#Read in template library
source   ALL_modify.tcl
#Setup operation condition
set_operating_condition -voltage 0.8 -temp 25
set_vdd VDD 0.7
set_gnd VSS 0
set_var voltage_map 1
set_var constraint_delay_degrade 0.1
#set_var  constraint_search_bound 0.000001 
set_var extsim_deck_dir "/home1st/s80307330/finFlex/characterization/output/"
set_var extsim_save_failed  all
set_var extsim_save_passed  all
#set_var constraint_glitch_peak_mode 2
#set_var constraint_glitch_peak 0.1
#set_var constraint_glitch_peak_report_inherent 1
#set_var constraint_delay_degrade 0.1
#Read spice files and models
read_spice   {characteristic_all.sp}
#char_library -extsim HSPICE
#char_library -ecsm -css -extsim hspice -client_postproc "hspice -C -K"
set_var extsim_exclusive 1
#set_var mpw_table 1
#char_library -ecsm -ccs -extsim Hspice -thread 15
char_library -thread 25 -extsim hspice 
#char_library -extsim Hspice 
#set_var extsim_exclusive 1
#write out ldb
write_ldb finFlex_simple_fin32.1db
write_library   all.lib

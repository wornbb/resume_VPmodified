#!/usr/bin/zsh
rm -rf trans.gridIR
rm -rf power_grid.test
./voltspot -c pdn.config -f example.flp -p example.ptrace -v trans.vtrace -gridvol_file trans.gridIR
python getCurrent.py


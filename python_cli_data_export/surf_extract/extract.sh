#!/bin/bash

ts=$((10368+144*$1))

ITER="$ts"

echo $ITER

python extract_llc_surf.py --iter ["$ITER"] --variables='["Eta","U","V","W","Theta","Salt"]' --facen='[3]' --out_dir './surf_fields/'


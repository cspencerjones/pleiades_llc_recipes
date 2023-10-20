#!/bin/bash

ts=$((179856+144*$1))

ITER="$ts"

echo $ITER

python extract_wind.py --iter ["$ITER"] --variables='["KPPhbl","PhiBot","oceTAUX","oceTAUY","SIarea"]' --facen='[3]' --out_dir './surf_wind/'


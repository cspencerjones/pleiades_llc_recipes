#!/bin/bash

for i in {0..1}
do
ts=$((390528+144*$i))

ITER="$ts"


#python extract_llc.py --iter ["$ITER"] --out_dir './sub/'
python extract_llc.py --iter ["$ITER"] --variables='["U","V"]' --fdepth='y' --out_dir './not_compressed/'
#python extract_llc.py --iter ["$ITER"] --variables='["PhiBot"]' --out_dir './sub-output/'
#python extract_llc.py --iter ["$ITER"] --variables='["Theta"]' --out_dir './sub-output/' 
#python extract_llc.py --iter ["$ITER"] --variables='["Salt"]' --out_dir './sub-output/'
#python extract_llc.py --iter ["$ITER"] --fdepth='y' --variables='["Salt"]' --out_dir './ts_output/'

done

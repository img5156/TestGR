#!/bin/bash

lalapps_inspinj --output injection.xml --seed 5227 --f-lower 20 \
                --waveform SEOBNRv3pseudoFourPN \
                --gps-start-time 1135136355 --gps-end-time 1135136365 \
                --t-distr uniform --time-step 10 --time-interval 20 \
                --d-distr uniform --l-distr fixed  \
                --min-distance 200000 --max-distance 200000 \
                --i-distr fixed --polarization 0.0 --fixed-inc 30.0 \
                --coa-phase-distr fixed --fixed-coa-phase 0.0 \
                --m-distr fixMasses \
                --fixed-mass1 22 --fixed-mass2 18 \
                --taper-injection startend --enable-spin  --amp-order -1 \
                --min-spin1 0.8 --max-spin1 0.8 \
                --min-spin2 0.8  --max-spin2 0.8 \
                --longitude 0.0 --latitude 0.0 \

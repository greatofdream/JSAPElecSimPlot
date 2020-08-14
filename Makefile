.PHONY: all
all: readout trigger
%.png: test.root 
	python3 plotHittime.py -i $^ -o $@ -c 0 1 2 3 4 5 29 -e $* >$@.log 2>&1
waveform/%: test.root
	mkdir -p $(dir $@)
	python3 plotWaveform.py -i $^ -o $@ -e $* >$@.log 2>&1
spe.png: SPE.mat
	python3 plotSPE.py -i $^ -o $@ >$@.log 2>&1
.DELETE_ON_ERRORS:
.SECONDARY:
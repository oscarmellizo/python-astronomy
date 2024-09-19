from lightkurve import search_targetpixelfile
tpf = search_targetpixelfile('KIC 6922244', author="Kepler", cadence="long", quarter=4).download()
lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)
tpf.plot()
import sys
import scipy
import glob
import ccdproc
import matplotlib.pyplot as plt
from astropy import units as u
import numpy as np
from astropy.nddata import CCDData
from astropy.nddata import NDData
from astropy.nddata import fits_ccddata_reader
from astropy.nddata import fits_ccddata_writer
from astropy.modeling.functional_models import Gaussian2D
from astropy.utils.misc import NumpyRNGContext
from scipy.ndimage import uniform_filter
import astropy.io.fits as fits
from ccdproc import Combiner
from ccdproc import wcs_project
from astropy.io.fits import Header
from astropy import  wcs
from astropy.io import fits 
from astropy.table import Table, Column
from specutils import Spectrum1D
import os
import pandas as pd

dir="spectra\\"

ngc2264_spectra=pd.DataFrame(columns=['#ra','dec','width'])
i=0
for fitsName in glob.glob(dir+'*.fits'):
    
    
    hdul = fits.open(fitsName)
  #  hdul.info()
    
    specdata = hdul[0]
    
#    print(10**specdata.data[1],specdata.data[0])
    
    scidata = specdata.data[0]* u.dimensionless_unscaled

    lamb = specdata.data[2] * u.AA 
 
 
    with open(fitsName+".txt",'w') as f:
        for row in zip(lamb, scidata):
            f.write('{}\t{}\n'.format(row[0], row[1]))
    

# To plot using maptplotlib:

    spec = Spectrum1D(spectral_axis=lamb, flux=scidata) 
    
    from specutils.manipulation import extract_region
    from specutils import SpectralRegion
    cut_spectrum1_HA = extract_region(spec, SpectralRegion(6540.0*u.AA, 6550.0*u.AA))
    cut_spectrum2_HA = extract_region(spec, SpectralRegion(6575.0*u.AA, 6600.0*u.AA))
    cut_spectrumHA = extract_region(spec, SpectralRegion(6540.0*u.AA, 6590.0*u.AA))

    from astropy.modeling import models
    from numpy.polynomial import polynomial as P
    from astropy.modeling import models, fitting
    from scipy import interpolate
    from astropy.modeling.fitting import LevMarLSQFitter

    model_poly = models.Polynomial1D(degree=2)
    fitter_poly = fitting.LinearLSQFitter()
    best_fit_HA = fitter_poly(model_poly, np.concatenate((cut_spectrum1_HA.spectral_axis.value, cut_spectrum2_HA.spectral_axis.value), axis = None), np.concatenate((cut_spectrum1_HA.flux.value, cut_spectrum2_HA.flux.value), axis = None))
    nspec1d_HA = Spectrum1D(flux=cut_spectrumHA.flux.value/best_fit_HA(cut_spectrumHA.spectral_axis.value)*u.dimensionless_unscaled, spectral_axis=cut_spectrumHA.spectral_axis)
    
    from specutils.manipulation import extract_region
    from specutils.fitting import fit_generic_continuum

    from specutils.analysis import equivalent_width, centroid
    from specutils import SpectralRegion
    

    
    anchitoHA=5
# First we compute the centroids:
    cHA = centroid(nspec1d_HA, SpectralRegion(6555*u.AA, 6575*u.AA))
# Thus we configure the width measured fromthe centroid:
    izq1HA=cHA - anchitoHA*u.AA
    der1HA=cHA + anchitoHA*u.AA   
# we use photutils to fit a gaussian and get the equivalent width
    EW_HA = equivalent_width(nspec1d_HA,regions=SpectralRegion(izq1HA,der1HA))
 
    print(hdul[0].header['RA'],hdul[0].header['DEC'],EW_HA)
    ngc2264_spectra.loc[i,'#ra']=hdul[0].header['RA']
    ngc2264_spectra.loc[i,'dec']=hdul[0].header['DEC']
    ngc2264_spectra.loc[i,'width']=EW_HA
    i=i+1
    #plt.plot(nspec1d_HA.spectral_axis, nspec1d_HA.flux)
    #plt.title('SSH (m) ' + str(ecco_ds.time[0].values)[0:7] + '\n tile 2')
    #plt.title(fitsName,fontsize=10)

    #plt.xlabel('Wavelength (\AA)')
    #plt.ylabel('Relative Flux')
    #plt.xlim(6540,6580) #Ha
   # plt.xlim(658,750) #OI
    ttauri=[100.24517, 100.17576, 100.41561, 100.21476, 100.22609, 100.19794, 100.17236]
    for number in ttauri:
        if hdul[0].header['RA'] ==number:
            plt.plot(nspec1d_HA.spectral_axis, nspec1d_HA.flux)
            #plt.title('SSH (m) ' + str(ecco_ds.time[0].values)[0:7] + '\n tile 2')
            plt.title(fitsName,fontsize=10)
            plt.xlabel('Wavelength (\AA)')
            plt.ylabel('Relative Flux')
            plt.xlim(6540,6580) #Ha
            #plt.savefig(str(fitsName)+"para_subir"+".png")
            #plt.show()
        else:
            pass
        plt.savefig(str(fitsName)+"para_subir_F"+".png")
   # plt.xlim(658,750) #OI
            
#plt.ylim(1e-7,1e1);
    #plt.savefig(str(fitsName)+".png")
    
    #plt.show()    
#ngc2264_spectra.to_csv(r"C:\Users\juani\OneDrive\Documentos\TOBS\spectra\ngc2264_spectra.csv",index=False)    
pass
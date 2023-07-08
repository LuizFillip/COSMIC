# Routine for analysis of FormoSat-3 / COSMIC GPS radio occultation data  


# Introduction 

Since the FormoSat-3 / COSMIC (F3/C) satellites fly in non-sun-synchronous 
orbit with an inclination of 70◦, they effectively perform global soundings

How the goal of this code is to run for several days and years with downloading,
unziping, read NetCDF files. Moreover, creating and deleting folders during this 
process, all them automaticaly. I add some progress bars for the main tasks 
(I was think pretty cool)

# Products

## Level 1b
Atmospheric excess phase (atmPhs format) 
Navigation bits used for processing open loop data in the lower troposphere (gpsBit format) 
Ionospheric excess phase (ionPhs format) 
Clock offset values for each LEO satellite (leoClk format) 
LEO orbit specification file (leoOrb format) 
Absolute Total Electron Content and auxiliary data (podTec format)
S4 scintillation index and auxiliary data (scnLv1 format)

## Level 2
Atmospheric profiles without moisture (atmPrf format) 
Low-resolution, atmospheric profile in the BUFR format (bfrPrf format) 
ECMWF profiles (echPrf format) 
ERA-40 Interim reanalysis data (eraPrf format) 
NCEP operational analysis data (gfsPrf format) 
Ionospheric profiles (ionPrf format) 
Atmospheric profiles with moisture (wetPrf format)

These datasets are available from 2006-04-22 to 2014-04-30.

# Scintilation data (S4 parameter)

S4 scintillation index and auxiliary data. Each file contains continuous S4 data 
(one value each second based on 50 Hz internal receiver sampling) from one GPS 
satellite (small data gaps are allowed).

CDAAC also provides “ScnLv1” scintillation datasets which contain offline 
constructed S4 data calculated from 50 Hz that are recorded at 1 Hz (Kepkar et al. 2020).
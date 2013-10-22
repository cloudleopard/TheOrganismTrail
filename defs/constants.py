# A starter environmental resources dictionary.
# All values are mol/L, except Temp and Lux, which are in Kelvin and Lux.
# Based on standard LB medium and standard growth conditions.
# http://en.wikipedia.org/wiki/Lysogeny_broth
ENVR = {'H+'  : 10**-7.4,
        'K+'  : 3.3*10**-3,
        'Na+' : 1.8*10**-1,
        'Cl-' : 1.8*10**-1,
        'CO2' : 3.3*10**-2,
        'O2'  : 3.3*10**-2,
        'Glc' : 3.3*10**-3,
        'Fru' : 0.0,
        'Lac' : 0.0,
        'AAs' : 9.7*10**-2,
        'N'   : 0.0,
        'P'   : 0.0,
        'EtOH': 0.0,
        'Temp': 310.0,
        'Lux' : 1000.0}

RESLIST = ENVR.keys()

# A starter internal cellular concentrations dictionary.
# Based on Escherichia coli.
# Each resource has a dictionary containing min/max/current values.
# All values are in mol/L and are based on the following research article:
# http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2754216/
CELLR = {'H+':  {'current': 10**-7.4,
                 'minLive': 10**-8.0,
                 'minGrow': 10**-7.8,
                 'ideal'  : 10**-7.4,
                 'maxGrow': 10**-7.2,
                 'maxLive': 10**-7.0},
         'K+':  {'current': 2.1*10**-1,
                 'minLive': 10**-1,
                 'minGrow': 1.5*10**-1,
                 'ideal'  : 2*10**-1,
                 'maxGrow': 2.5*10**-1,
                 'maxLive': 3*10**-1},
         'Na+': {'current': 5*10**-3,
                 'minLive': 10**-3,
                 'minGrow': 3*10**-3,
                 'ideal'  : 3.5*10**-3,
                 'maxGrow': 1.4*10**-2,
                 'maxLive': 2*10**-2},
         'Cl-': {'current': 5*10**-3,
                 'minLive': 10**-3,
                 'minGrow': 3*10**-3,
                 'ideal'  : 3.5*10**-3,
                 'maxGrow': 1.4*10**-2,
                 'maxLive': 2*10**-2},
         'ATP': {'current': 8*10**-3,
                 'minLive': 5*10**-4,
                 'minGrow': 2*10**-3,
                 'ideal'  : 9*10**-3,
                 'maxGrow': 10**-2,
                 'maxLive': 2*10**-2},
         'ADP': {'current': 8*10**-3,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**-1,
                 'maxLive': 2*10**-1},
         'CO2': {'current': 3.3*10**-2,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**-1,
                 'maxLive': 10**-1},
         'O2':  {'current': 3.3*10**-2,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**-1,
                 'maxLive': 10**-1},
         'Glc': {'current': 8*10**-3,
                 'minLive': 0.0,
                 'minGrow': 10**-3,
                 'ideal'  : 9*10**-3,
                 'maxGrow': 10**-2,
                 'maxLive': 2*10**-2},
         'Fru': {'current': 0.0,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**-2,
                 'maxLive': 2*10**-2},
         'Lac': {'current': 0.0,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**-2,
                 'maxLive': 2*10**-2},
         'AAs': {'current': 1.5*10**-1,
                 'minLive': 10**-2,
                 'minGrow': 10**-1,
                 'ideal'  : 1.9*10**-1,
                 'maxGrow': 2*10**-1,
                 'maxLive': 3*10**-1},
         'N':   {'current': 8*10**-3,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**-2,
                 'maxLive': 10**-1},
         'P':   {'current': 8*10**-3,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**-2,
                 'maxLive': 10**-1},
         'EtOH':{'current': 0.0,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 1.09,   # These correspond to ~6%...
                 'maxLive': 1.71},  # ...and ~10% ABV
         'Temp':{'current': 310.0,
                 'minLive': 273.0,
                 'minGrow': 281.0,
                 'ideal'  : 310.0,
                 'maxGrow': 318.0,
                 'maxLive': 344.0},
         'Lux' :{'current': 0.0,
                 'minLive': 0.0,
                 'minGrow': 0.0,
                 'ideal'  : 0.0,
                 'maxGrow': 10**5,
                 'maxLive': 1.7*10**5}}

# Some resources diffuse freely across membranes.
DIFFUSES = ['CO2', 'O2', 'EtOH', 'Lux', 'Temp']

# There are several basic functions of operons, passive/active transporters,
# modifiers, and reaction catalysts.
OPTYPES = ['pas', 'act', 'mod', 'rxn', 'misc']
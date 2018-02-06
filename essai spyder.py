from pylab import *
import pandas as pd
close('all')
largeur =5.01
epaisseur =5.02
section=largeur*epaisseur
location = 'C:\Users\Mathias\Documents\Thèse\Traction\eprouvette_D1.csv'
datafile = pd.read_csv(location, sep=';', decimal=',', encoding='latin-1')
temps= datafile['Temps'][1:].str.replace(',','.').astype(float)
dep = datafile['Déplacement'][1:].str.replace(",",".").astype(float)
force = datafile['Charge'][1:].str.replace(",",".").astype(float)
deformation = datafile['Déformation 1'][1:].str.replace(",",".").astype(float)
sigma=force/section
figure(1)
plot(deformation[1:2634],sigma[1:2634])
xplot('Déformation $\epsilon$')
yplot('Contrainte $\sigma$')
grid()
axis([0,0.25,0,1200])

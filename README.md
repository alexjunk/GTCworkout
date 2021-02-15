# GTCworkout

## notations

Text = température extérieure

Tc = température de consigne de l'eau

Tdep = température de départ dans le circuit

pompe = 1 pour pompe en marche, 0 pour pompe arrêtée

V3V = 1 pour vanne 3 voies qui s'ouvre, -1 pour vanne 3 voies qui se ferme, 0 pour statut-quo

## algorithme de fonctionnement d'un circuit de chauffage

situation de distribution | action
-- | --
passage de ON à OFF | V3V = -1 puis pompe = 0
pasage de ON à OFF | pompe = 1 puis V3V = 1

Lorsqu'on distribue de la chaleur, la pompe tourne et la vanne s'ouvre ou se ferme pour réguler la température de départ à +/-1°C autour de la température de consigne de l'eau 
distribution | monitoring | action
-- | -- | --
ON | Tdep < Tc-1 | V3V = 1
ON | Tc-1 <= Tdep <= Tc+1 | V3V = 0
ON | Tdep > Tc+1 | V3V =-1

Lorsqu'on ne chauffe pas, on maintient l'activité de la pompe jusqu'à ce que le circuit ne distribue plus de chaleur 
distribution | monitoring | action
-- | -- | --
OFF | Tdep > 30 | pompe = 1
OFF | Tdep <= 25 | pompe = 0 

Lorsqu'on ne chauffe pas et que le bâtiment n'est pas occupé, et s'il y a une vague de froid, on envoie de l'eau à 20°c pour maintenir le hors-gel
distribution | monitoring | action
-- | -- | -- 
OFF | Text < 4 | pompe = 1
OFF | Tdep < 19 | V3V = 1
OFF | 19 <= Tdep <= 21 | V3V = 0
OFF | Tdep > 21 | V3V =-1


comment sait-on que la vanne est totalement fermée ou totalement ouverte ?

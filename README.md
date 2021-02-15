# GTCworkout

## notations

Text = température extérieure

Tc = température de consigne de l'eau pour la distribution

Tdep = température de départ dans le circuit

pompe = 1 pour pompe en marche, 0 pour pompe arrêtée

V3V = 1 pour vanne 3 voies qui s'ouvre, -1 pour vanne 3 voies qui se ferme, 0 pour rien

## algorithme de fonctionnement d'un circuit de chauffage

distribution | monitoring | action
-- | -- | --
ON | Tdep > 30 | pompe = 1
ON | Tdep <= 30 | pompe = 0 
ON ou OFF | Text < 4 | pompe = 1
ON | Tdep < Tc-1 | V3V = 1
ON | Tc-1 <= Tdep <= Tc+1 | V3V = 0
ON | Tdep > Tc+1 | V3V =-1

situation | action
passage de ON à OFF | V3V = -1 puis pompe = 0
pasage de ON à OFF | pompe = 1 puis V3V = 1

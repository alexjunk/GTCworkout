# GTCworkout

## notations

Text = température extérieure

Tc = température de consigne de l'eau pour la distribution

Tdep = température de départ dans le circuit

pompe = 1 pour pompe en marche, 0 pour pompe arrêtée

V3V = 1 pour vanne 3 voies qui s'ouvre, 2 pour vanne 3 voies qui se ferme

## algorithme de fonctionnement d'un circuit de chauffage

constat après monitoring | action
-- | --
Tdep > 30 | pompe = 1
Tdep <= 30 | pompe = 0 
Text < 4 | pompe = 1
si Tdep < Tc 

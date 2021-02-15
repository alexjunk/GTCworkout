# GTCworkout

## algorithme de fonctionnement d'un circuit de chauffage

Text = température extérieure
Tdep = température de départ dans le circuit
pompe = 1 pour pompe en marche, 0 pour pompe arrêtée
V3V = 1 pour vanne 3 voies qui s'ouvre, 2 pour vanne 3 voies qui se ferme

si Tdep > 30 alors pompe = 1
si Text < 4 alors pompe = 1

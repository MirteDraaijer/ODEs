# ODEs
Paar aantekeningen over de opdracht:
Algemene taken casus B:
- Eigen python module/package met classes/functies die meerdere gangbare tumorgroeimodellen implementeert en dingen voor fitten (alle 10 de formules uit de notebook)
- README met technische specificaties, achtergrondinformatie over modellen/technieken + referenties
- Notebook met een use-case

Specifiekere taken casus B:
- We kunnen voor de modellen al achtergrond info opzoeken, voor de readme
- Paper doorlezen: https://www.jsr.org/hs/index.php/path/article/view/5202/2426
- Alle modellen uit de notebook
- Data vinden of willen we de gegeven data gebruiken?

---

# Achtergrondinformatie:
Wiskundige modellen, waaronder ordinary differential equations (ODEs), worden gebruikt om tumor groei te simuleren en behandeling van kanker te bestuderen (Chan et al., 2023). Er zijn verschillende differentiaal vergelijkingen die hiervoor gebruikt kunnen worden. Verderop volgt een kort overzicht van een aantal verschillende differentiaal vergelijkingen die gebruikt kunnen worden om tumor groei te simuleren.

## Lineaire groei:

## Exponentieel toenemende groei:
De formule voor de exponentieel toenemende groei is:
$$
\frac{\text{d}V}{\text{d}t} = c \cdot V
$$
In het exponentiele model is de groei proportioneel aan de tumor-grootte. Hierbij is $c$ de groeifactor en $V$ is het volume van de tumor op  een gegeven moment. Dit model werkt goed voor het voorspellen van tumorgroei in vroege stadia (Hassan & Al-Saedi, 2024).

## Mendelsohn groei:

## Exponentieel afvlakkende groei:
De formule voor exponentieel afvlakkende groei is:
$$
\frac{\text{d}V}{\text{d}t} = c \,( V_{\max} - V)
$$
Deze formule is een variant op de 'normale' exponentiele groei, deze versie heeft een maximaal volume wat de tumor kan bereiken, dit is iets wat de 'normale' exponentiele formule niet heeft. Hierbij is $c$ de groeifactor, $V_{max}$ is het maximale volume dat de tumor kan krijgen en $V$ is het volume van de tumor op een gegeven moment. 

## Logistische groei:

## Montroll groei:
De formule voor Montroll groei is:
$$
\frac{\text{d}V}{\text{d}t} = c \, V \, \left( V_{\max}^d - V^d \right)
$$
Dit model gaat uit van continue groei, maar in een echt systeem groeit de tumor niet elke dag even snel. Hierbij is $c$ de groeifactor, $V$ is het volume van de tumor op een gegeven moment, $V_{\max}^d$ is de maximale groeiruimte die beschikbaar is, waarbij $d$ bepaalt hoe sterk de remming en $V^d$ is hoeveel van de groeiruimte al is gebruikt (Rodrigues, 2024).

## Allee effect groei:

## Lineair gelimiteerde groei:
De formule voor lineair gelimiteerde groei is:
$$
\frac{\text{d}V}{\text{d}t} = c \cdot \frac{V}{V + d}
$$
Deze formule is een variant op de 'normale' lineaire groei, deze versie heeft een maximum snelheid waarmee de tumor kan groeien, dit is iets wat de 'normale' formule niet heeft. Hierbij is $c$ de groeifactor, $V$ is het huidige volume van de tumor en $V + d$ voegt een constante toe waardoor de snelheid waarmee de tumor kan groeien beperkt wordt.

## Oppervlakte gelimiteerde groei:

## Von Bertalanffy groei:
De formule voor Von Bertalanffy groei is:
$$
\frac{\text{d}V}{\text{d}t} = c \cdot V^\frac{2}{3} - d \cdot V
$$
Dit model impliceert dat het volume van de tumor afneemt met celldood en dat groei toeneemt proportioneel aan het oppervlakte. Hierbij is $c$ de groeifactor, $V^\frac{2}{3}$ beschrijft de starttoestand en $-d \cdot V$ zorgt voor een afname in volume. Als er een populatie wordt beschreven kunnen $V^\frac{2}{3}$ en $-d \cdot V$ ook gezien worden als de geboorte- en sterftecijfers, maar dat is niet hoe tumoren te werk gaan (Hassan & Al-Saedi, 2024).

## Gompertz groei:

# Bronvermelding:
- Chan, K., Kao, C., Gordinier, J., & Ganden, K. (2023). Treatment Optimization for Tumor Growth by Ordinary Differential Equations. Journal Of Student Research, 12(4). https://doi.org/10.47611/jsrhs.v12i4.5202
- Hassan, S. S., & Al-Saedi, H. M. (2024). Comparative Study of Tumor Growth Based on Single Species Models. BIO Web Of Conferences, 97, 00118. https://doi.org/10.1051/bioconf/20249700118
- Rodrigues, J. A. (2024). Using Physics-Informed Neural Networks (PINNs) for Tumor Cell Growth Modeling. Mathematics, 12(8), 1195. https://doi.org/10.3390/math12081195
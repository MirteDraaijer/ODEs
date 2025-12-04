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
## Auteurs:
- Ivar Lottman
- Mirte Draaijer

# Beschrijving:

In dit project zijn 11 verschillende differentiaal vergelijkingen toegepast om de groei van tumoren te modelleren. Het project bestaat uit een python klasse (`ode_solver.py`) met daarin: de verschillende modellen, een functie om de modellen te fitten, een solver op basis van Runge-Kutta om de differentiaal vergelijkingen op te lossen en een plot functie. Verder is er een jupyter notebook (`ode_demo.ipynb`) met daarin 2 uitgebreid uitgewerkte voorbeelden. Achtergrondinformatie, een korte handleiding, en vereisten zijn te vinden in de README

Het bestand `ode_solver.py` bevat een aantal verschillende functies, hier volgt een korte beschrijving van elke functie.

- runge_kutta_solver(): deze functie wordt gebruikt om de differentiaal vergelijkingen op te lossen op basis van Runge-Kutta. Meer informatie over Runge-Kutta is te vinden in de sectie: [Achtergrondinformatie - Runge-Kutta](#runge-kutta)
- fit(): deze functie wordt gebruikt om de meest geschikte parameters te bepalen voor het gekozen model.
	- MSE_calc(): deze functie is een inner functions van fit(). De MSE_calc() functie berekent de mean-squared error, dit is een maat om de fout mee uit te drukken. Hoe lager de MSE, hoe lager de fout. Daarom is deze essentieel voor de fit() functie.
- aic(): deze functie berekent de Akaike information criterion (AIC). Meer informatie over AIC is te vinden in de sectie: [Achtergrondinformatie - Information criterion](#information-criterion)
- bic(): deze functie berekent de Bayes information criterion (BIC). Meer informatie over BIC is te vinden in de sectie: [Achtergrondinformatie - Information criterion](#information-criterion)
- plot(): deze functie genereert een simpele plot van het gekozen model.

De modellen:

- allee()
- exponentieel_afvlakkend()
- exponentieel_toenemend()
- gompertz()
- lineair()
- lineair_gelimiteerd()
- logistisch()
- mendelsohn()
- montroll()
- oppervlakte_gelimiteerd()
- von_bertalanffy()

Voor verdere informatie over deze modellen lees [Achtergrondinformatie - Modellen](#modellen)

# Systeem vereisten:
Python 3.12 of hoger  
Math  
Matplotlib 3.10 of hoger  


# Gebruik:

## Gedetailleerde handleiding:

In het bestand `ode_demo.ipynb` is een uitgebreide handleiding te vinden van hoe deze module in zijn werk gaat aan de hand van een voorbeeld.  

Hieronder een kort voorbeeld voor het initilizeren van de klasse en het uitvoeren van de montroll ode methode.  
De initialisatie van de class moet te minste een start volume, n(datapunten) en een delta t   
``
model = ode_solver(start_volume, number_of_data_points, delta_t)
``

verder verwachten alle vergelijkingen een dictionary met daarin de parameters die voor dat specifieke model nodig zijn in dit geval c,d en max volume.  
``
parameters = {"c" : 5, "d" : 1, "max_volume":1000}
``

Voorbeeld uitvoeren met de montroll methode
``
voorspelde_dagen, voorspelde_volumes = model.montroll(**params)
``



# Achtergrondinformatie:

## Information criterion:  
Om de modelen met elkaar te vergelijken zijn er 2 methodes geimplementeerd de Bayesian information criterion(BIC) en de Akaike information critirion(AIC). Deze methodes houden rekening met de potentie van een model om te overfitten door een foutmarge aan de hoeveelheid parameters toe te voegen.
Het grootste verschil tussen de 2 methodes is dat BIC de hoeveelheid datapunten zwaarder weegt dan AIC.  

Bij het vergelijken van 2 modelen met dezelfde methode heeft het model met de laagste waarde de voorkeur.

### BIC  
De formule van BIC is alsvolgt  

$$
BCE = n \cdot ln(MSE) + ln(n) \cdot k  
$$

De n staat voor de hoeveelheid datapunten.  
De MSE staat voor Mean Squared Error.  
De k staat voor de hoeveelheid parameters.  

### AIC  

$$  
AIC = n \cdot ln(MSE) + 2 \cdot k  
$$  

De n staat voor de hoeveelheid datapunten.  
De MSE staat voor Mean Squared Error.  
De k staat voor de hoeveelheid parameters.  

## Runge-Kutta:

Runge-Kuttamehoden zijn numerieke methoden om differentiaal vergelijkingen op te lossen. Voor dit project hebben wij de klassieke Runge-Kuttamethode gebruikt. Deze lost de differentiaal vergelijking met 4 tussenstappen op:

- Eerst wordt er een halve stap genomen
- Daarna wordt er nog een halve stap genomen
- Gevolgd door een hele stap
- En tot slot nog een hele stap
- De helling van deze verschillende stappen wordt samengenomen, hierbij weegt de eerste stap 1/6, de tweede stap 1/3, de derde stap 1/3 en de laatste stap 1/6

Op deze manier wordt de meeste accurate helling berekent voor het specifieke punt waarop het model zich bevind, dit gaat zo door tot het laatste punt is bereikt.

(Wikipedia-bijdragers, 2023)

## Modellen:

Wiskundige modellen, waaronder ordinary differential equations (ODEs), worden gebruikt om tumor groei te simuleren en behandeling van kanker te bestuderen (Chan et al., 2023). Er zijn verschillende differentiaal vergelijkingen die hiervoor gebruikt kunnen worden. Verderop volgt een kort overzicht van een aantal verschillende differentiaal vergelijkingen die gebruikt kunnen worden om tumor groei te simuleren.

### Lineaire groei:
De formule voor lineaire groei is:

$$
\frac{\text{d}V}{\text{d}t} = c
$$

In het liniare model is word de volume $V$ bepaald door de groeifactor $c$ over tijd zonder limiet.
hierin word volume berekent als functie van tijd aan de hand van de volume + de groeifactor

### Exponentieel toenemende groei:
De formule voor de exponentieel toenemende groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot V
$$

In het exponentiele model is de groei proportioneel aan de tumor-grootte. Hierbij is $c$ de groeifactor en $V$ is het volume van de tumor op  een gegeven moment. Dit model werkt goed voor het voorspellen van tumorgroei in vroege stadia (Hassan & Al-Saedi, 2024).

### Mendelsohn groei:
De formule voor Mendelsohn groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot V^d
$$

Dit model gaat uit van een exponentiele groei van de groefactor C * volume tot de macht van factor D [1]

### Exponentieel afvlakkende groei:
De formule voor exponentieel afvlakkende groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot( V_{\max} - V)
$$

Deze formule is een variant op de 'normale' exponentiele groei, deze versie heeft een maximaal volume wat de tumor kan bereiken, dit is iets wat de 'normale' exponentiele formule niet heeft. Hierbij is $c$ de groeifactor, $V_{max}$ is het maximale volume dat de tumor kan krijgen en $V$ is het volume van de tumor op een gegeven moment. 

### Logistische groei:
De formule voor logistische groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot V \cdot \left( V_\max - V \right)
$$

De logistische groei model gaat uit van een sigmoidale curve waarbij de groei afvlakt aan de hand van het maximale volume

### Montroll groei:
De formule voor Montroll groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot V \cdot \left( V_{\max}^d - V^d \right)
$$

Dit model gaat uit van continue groei, maar in een echt systeem groeit de tumor niet elke dag even snel. Hierbij is $c$ de groeifactor, $V$ is het volume van de tumor op een gegeven moment, $V_{\max}^d$ is de maximale groeiruimte die beschikbaar is, waarbij $d$ bepaalt hoe sterk de remming en $V^d$ is hoeveel van de groeiruimte al is gebruikt (Rodrigues, 2024).

### Allee effect groei:
De formule voor Allee effect groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot \left( V - V_\min \right) \cdot \left( V_\max - V \right)
$$

Het allee effect neemt de omgeving en de volume van een tumor mee met de groeifactor (zowel positief als negatief)[2]

### Lineair gelimiteerde groei:
De formule voor lineair gelimiteerde groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot \frac{V}{V + d}
$$

Deze formule is een variant op de 'normale' lineaire groei, deze versie heeft een maximum snelheid waarmee de tumor kan groeien, dit is iets wat de 'normale' formule niet heeft. Hierbij is $c$ de groeifactor, $V$ is het huidige volume van de tumor en $V + d$ voegt een constante toe waardoor de snelheid waarmee de tumor kan groeien beperkt wordt.

### Oppervlakte gelimiteerde groei:
De formule voor Oppervlakte gelimiteerde groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot \frac{V}{\left( V + d \right)^\frac{1}{3}}
$$

Dit model gaat er vanuit dat voornamenlijk de bovenste laag van een tumor groeit en de cellen binnenin de tumor niet meer. Dit model gaat uit van een exponentiele groei in het beginstadium en daarna uitgaat van de groei factor van de bovenste laag. [1]

### Von Bertalanffy groei:
De formule voor Von Bertalanffy groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot V^\frac{2}{3} - d \cdot V
$$

Dit model impliceert dat het volume van de tumor afneemt met celldood en dat groei toeneemt proportioneel aan het oppervlakte. Hierbij is $c$ de groeifactor, $V^\frac{2}{3}$ beschrijft de starttoestand en $-d \cdot V$ zorgt voor een afname in volume. Als er een populatie wordt beschreven kunnen $V^\frac{2}{3}$ en $-d \cdot V$ ook gezien worden als de geboorte- en sterftecijfers, maar dat is niet hoe tumoren te werk gaan (Hassan & Al-Saedi, 2024).

### Gompertz groei:
De formule voor Gompertz groei is:

$$
\frac{\text{d}V}{\text{d}t} = c \cdot V \cdot \ln \left( \frac{V_\max}{V} \right)
$$

Gompertz gaat uit van een sigmoidal curve die asymetrisch is van het infectiepunt. Dit model is een generalisatie van een logistiek model dat de groei van organisme's nabootst.[1]
hierbij komt de variable Vmax te staan voor het maximale volume dat de tumor theoretisch kan berijken.

# Bronvermelding:
- Chan, K., Kao, C., Gordinier, J., & Ganden, K. (2023). Treatment Optimization for Tumor Growth by Ordinary Differential Equations. Journal Of Student Research, 12(4). https://doi.org/10.47611/jsrhs.v12i4.5202
- Hassan, S. S., & Al-Saedi, H. M. (2024). Comparative Study of Tumor Growth Based on Single Species Models. BIO Web Of Conferences, 97, 00118. https://doi.org/10.1051/bioconf/20249700118
- Rodrigues, J. A. (2024). Using Physics-Informed Neural Networks (PINNs) for Tumor Cell Growth Modeling. Mathematics, 12(8), 1195. https://doi.org/10.3390/math12081195
- Wikipedia-bijdragers. (2023, 19 december). Runge-Kuttamethode. Wikipedia. https://nl.wikipedia.org/wiki/Runge-Kuttamethode
- [1] https://link.springer.com/article/10.1186/s12885-016-2164-x
- [2] https://zakopane.if.uj.edu.pl/event/24/contributions/591/contribution.pdf
ODD - Protokoll Fischerei und Allmende

## 1. Purpose and Patterns
Was modellieren wir und warum?

Das Modell soll veranschaulichen, unter welchen Bedingungen eine gemeinsam genutzte Ressource, wie ein See mit einem bestimmten Fischbestand, stabil bleibt oder kippt. Konkret geht es uns um das Verhalten der Fischer, das mehr oder weniger gravierende Auswirkungen auf den Fischbestand zeigt. Welche Parameter haben eine hohe Sensitivität für die Stabilität des Fischbestands? 
Wir erwarten: Je indivividueller das Nutzungsverhalten der Fischer (Gewinnmaximierung des Einzelnen) ist, umso früher kollabiert der Bestand. Je mehr soziales Verhalten, umso stabiler bleibt das System. Nähe fördert das voneinander lernen. Isolation führt zur schrittweisen Abkehr von sozialem Verhalten.

Für uns interessant: 
- Die Fischer als Individuum und als soziale Gruppe. 
- Welches Verhalten und welche Verhaltensadaption wirkt destabilisierend/stabilisierend für die gemeinsam genutzte Ressource.
- Welche Verhaltensbeeinflussenden Parameter wirken besonders sensitiv?

Für uns nicht interessant: 
- Welcher Fischer ist wie erfolgreich
- Welche Mechanismen im See wirken beschleunigend oder stabilierend für den Fischbestand (z.B. Diffusion zwischen den Patches)

## 2. Entities, State Variables, and Scales
Welche Dinge/Elemente gibt es? Was charakterisiert sie?

Fischer
- Anzahl der Fischer am See (z.B. 20)
- Postion der Fischer (Patch)
- Verhalten der Fischer (von 1/kooperativ bis 9/ego => Faktor bestimmt den Fischfang: 1 bis 9 Fische pro Zeitschritt)
- Nähe/Distanz zu anderen Fischern (beeinflusst das Verhalten)
Auf Saktionierung/Bestrafung bzw. Belohnung wird im Modell verzichtet. 

Fische
- Anzahl im See (Patch für Fischbestand nicht wichtig.)
- Maximale Kapazität im See (z.B. 1.000)
- Minimumbestand (Kipp-Größe, ab der sich der Bestand nicht mehr erholen kann, z.B. 200)
- Regenerationsrate (z.B. 10% pro Zeitschritt bis zur Maximalgrenze)

Patches (See als Gitter von Fisch-Patches dargestellt.)
- Anzahl Patches (z.B. 10x10)
- Koordinaten der Patches (Wird benötigt für Position der Fischer und die Grenzen des Sees?)
Max. Kapazität an Fischen pro Patch nicht wichtig.
Diffusion zwischen Patches wird nicht betrachtet.

- Simulationsdauer: 1.000 Zeitschritte

## 3. Prozess Overview and Scheduling (Zeitplan)
Was tun die Entitäten in welcher Reihenfolge?

Pro Zeitschritt passiert folgendes:
Schritt 1: Fischer fischen (auf Basis der hinterlegten Verhaltensregel je Fischer) und darauf aufbauend wird der neue Fischbestand im See gespeichert.
Schritt 2: Die Verhaltensregel bei den Fischern wird adaptiert (auf Basis Nähe/Distanz). 
Schritt 3: Fischer wechseln den Patch (ein Patch weiter auf Basis "Zufall")
Schritt 4: Fische regeneriern sich.

## 4. Design Concepts
# 4.1 Basic Principles
Welche Theorien oder Hypothesen liegen dem Modell zugrunde?

Das Modell basiert auf der Common-Pool-Theory. Die zentrale Frage die sich dieses Modell stellt lautet ob nicht nur Ressourcen sondern auch soziale Regelstrukturen den Ausgang bestimmen.

# 4.2 Emergence
Welche Ergebnisse entstehen aus dem Verhalten der Agenten, welche sind durch Regeln erzwungen?

In diesem Modell können verschiedene Makro Muster entstehen wie der Kollaps des Fischbestandes, Dominanz einzelner Strategien und die Durchsetzung von sozialen Verhaltensregeln.

# 4.3 Adaptation
Welche Entscheidungen treffen die Agenten? Wie reagieren sie auf Veränderungen?

Die Fischer passen ihr Verhalten durch Regeln an (Nähe führt zur Orientierung am Verhalten des stärker ausgeprägten Verhaltens. Isolation führt zum Schrittweisen Abbau von sozialem hin zu egoistischem Verhalten).

# 4.4 Objectives
Was optimieren die Agenten?

Jeder Fischer verfolgt primär das Ziel, Fische zu fangen - die Menge steuert seine hinterlegte Verhaltensregel. Isolation führt zur Gewinnmaximierung. Nähe optimiert das Verhalten in Bezug soziale Angleichung an das stärker ausgeprägte Verhalten. 

# 4.5 Learning
Ändern Agenten ihre Entscheidungsregeln über die Zeit?

Die Agenten ändern ihr Verhalten auf Basis von Nähe und Distanz. 
Isolation: Sie lernen von sich selbst (Je egoistischer, umso mehr Ertrag)
Nähe (Fischer treffen sich in benachbarten Feldern): Sie lernen von/orientieren sich an jenem Fischer, dessen Verhalten am stärksten ausgeprägt ist.

# 4.5 Prediction
Wie antizipieren Agenten zukünftige Zustände?
-

# 4.6 Sensing
Was können Agenten über ihre Umgebung und andere Agenten wahrnehmen? Über welche Distanz?

Die Wahrnehmung ist lokal auf benachbarte Zellen (Moore-Nachbarschaft) beschränkt. Wenn sie sich auf unmittelbaren Nachbarfeldern begegnen, nehmen sie das Fischverhalten des/der anderen wahr. Die Fischer orientieren sich am Fischer mit dem am stärksten ausgeprägten Verhalten. 

# 4.7 Interaction
Wie beeinflussen sich Agenten gegenseitig?

Über Nähe/Distanz: Begegnen sich ein oder mehrere Fischer auf einem Nachbarpatch, orientieren sie sich am Fischer mit dem am stärksten ausgeprägten Verhalten.

# 4.8 Stochasticity
Wo und warum wird Zufall verwendet?

Zufall wird verwendet bei:
- Initialisierung: Verhaltensregeln den einzelnen Fischern zuordnen. 
- Initialisierung: Startpositionen der Fischer auf dem See (Patches) fixieren.
Basis dafür sind einstellbare Durchschnittswerte für das Verhalten aller Fischer (z.B. ego/sozial zw. 1 und 9) und Nähe/Distanz-Verhältnis
Ein Random Seed wird gesetzt, um Reproduzierbarkeit zu gewährleisten.

# 4.9 Collectives
Gibt es Gruppen von Agenten, die als Einheit handeln?
-

# 4.10 Observation
Welche Outputs brauchen wir, um das Modell gegen unsere Patterns zu testen?

Wichtige Outputgrößen:
- Gesamtfischbestand über Zeit
- Anteil der jeweiligen Verhaltensstrategien, bei der der Fischbestand kippt

## 5. Initialization
Wie wird das Modell gestartet?

Der See wird als 10x10 Gitter initialisiert (x,y-Koordinatensystem)

Der See:
- Maximale Kapazität, max_capacity_lake=1.000
- Minimale Kapazität (Kipppunkt), min_capacity_lake=200
- Regenerationsrate Fischbestand, regen_rate=0,1 (10%) bis max_capacity

Fische im See: 
- Anfangsbestand, fish_stock=1.000

Fischer:
- Anzahl der Fischer am See: fisherman=20
- Postion der Fischer (Patch): position_fm= (x,y-Koordinaten), zufallsverteilt (von 0-1 / 0 bedeutet alle starten isoliert. 1 bedeutet alle starten als Gruppe in direkter Nachbarschaft)
- Verhalten der Fischer: behavefactor_gr= (gewünschter Start-Durchschnittswert eingeben, z.B. 5) => daraus ergeben sich die Einzelwerte zufallsgeneriert.
behavefactor_fm1=... (von 1/kooperativ bis 9/ego. Der Faktor bestimmt den Fischfang: bei behavefactor_fm=1 wird 1 Fisch pro Zeitschritt gefangen / bei behavefactor_fm=9 werden 9 Fische pro Zeitschritt gefangen / gleiches Prinzip für 2-8)

Random Seed wird gesetzt.

## 6. Input Data
Welche externen Daten fließen ein?

Externe, zeitabhängige Daten sind im Basismodell nicht erforderlich.

## 7. Submodels
Wie funktioniert jeder Prozess im Detail?

Schritt 1: Fischer fischen.
Am Beginn jedes Zeitschritts fischen die Fischer auf Basis der jeweils hinterlegten Verhaltensregel je Fischer.
fishing_fm1 = ...
Neuer Fischbestand im See wird gespeichert: fish_stock = fish_stock - fishing_fm1 - ...
Kipppunkt-Abgleich: Wenn fish_stock < min_capacity_lake, dann bricht die Animation ab. 

Schritt 2: Die Verhaltensregel bei den Fischern wird adaptiert. 
Hat ein Fischer keinen anderen Fischer auf einem Nachbarpatch: 
behavefactor_fm = behavefactor + 1 (er wird egoistischer). Bis max. 9 möglich.
Begegnen sich ein oder mehrere Fischer auf einem Nachbarpatch: 
Abgleich, wer den am stärksten ausgeprägten behavefactor hat (wie weit ist der Fischer von der Mitte entfernt): 
|behavefactor_fm1 - 5| =
|behavefactor_fm2 - 5| =
wenn |behavefactor_fm1 - 5| - |behavefactor_fm2 - 5| = 0, dann bleibt das Verhalten unverändert. 
wenn |behavefactor_fm1 - 5| - |behavefactor_fm2 - 5| = +, dann passt sich fm2 um 1 an fm1 an.
wenn |behavefactor_fm1 - 5| - |behavefactor_fm2 - 5| = -, dann passt sich fm1 um 1 an fm1 an.

Schritt 3: Fischer wechseln den Patch: 
Ein Patch weiter. Maximal 8 Nachbarfelder zur Auswahl (außer an den Rändern des Sees). Zufallsgeneriert. 
???

Schritt 4: Fische regeneriern sich.
Am Ende jedes Zeitschritts regeneriert sich der Fischbestand um den Regenerationsfaktor bis maximal zur Kapazitätsgrenze:
fish_stock = fish_stock + fish_stock*regen_rate
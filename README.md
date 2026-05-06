# ODD

## Overview

### 1. Purpose & Patterns - Zweck des Modells
Purpose: Wir wollen wissen, unter welchen Bedingungen eine gemeinsam genutzte Ressource (Fische im See) stabil bleibt oder zwangsläufig zum Kollaps führt. Im speziellen geht es darum, die Entwicklungen auf Basis einzelner Verhaltensregeln bzw. Sanktionen zu simulieren und miteinander zu verlgeichen. 
Patterns: Je indivividueller das Nutzungsverhalten der Fischer (Gewinnmaximierung des Einzelnen) ist, umso früher kollabiert der Bestand. Je höher die Kooperation unter den Fischern ist, umso stabiler bleibt das System. Bestärkung und Sanktionierung erhöhen die Stabilität. 

### 2. Entities, State Variables & Scales

Fischer:
- Position (Patch)
- Strategie/Verhalten (egoistisch, kooperativ, mischwert)

Fische: 
- Bestand für jeden Patch (den See gesamt) 
Ausgangsbestand. Kumulierter Bestand nach jeder Runde
- Bestandsgrenze nach oben: maximal mögliche Kapazität je Patch bzw. im See
- Regenerationsrate je Runde

See/Patches:
- See besteht aus einzelnen Gitterfeldern (Größe des Sees, Anzahl der Patches)
- Anzahl an Fischen pro Gitter
- Fische bewegen sich in Umgebungspatch/Nachbarpatch? Eher nicht.

Scales:
- Anzahl der Fischer
- Position je Fischer
- Veränderung der Position (Patch) je Fischer
- Strategie/Verhalten je Fischer: 0 (egoistisch), 1 (kooperativ), mischwert zw. 0 und 1
- (kumulierter) Fischerfolg je Fischer: Anzahl der gefangenen Fische
- See - Anzahl der Patches, Anzahl der Fische je Patches (und gesamt)
- Maximale Kapazität der Patches: 10 Fische (max. Kapazität im See: 1.000 Fische) 

- Simulationsdauer: 1.000 Zeitschritte

Lernen, wenn Treffen 
Sanktionierung: Bestrafung bei Überfischung
Bestärkung wenn hoher koop_Faktor

### 3. Prozess Overview and Scheduling (Zeitplan)

Pro Zeitschritt passiert folgendes:

- Fische im Patch (Regeneration oder nicht)
- Fischen (auf Basis Strategie/Verhaltensregel. Fischerfolg pro Fischer verfolgen.)
- Strategie/Verhaltensregel überprüfen/neu festlegen (Lernen oder Verlernen)
- Bestärkung/Bestrafung
- Bewegen oder nicht (Patch wechseln oder nicht)

## Design Concepts

### 4.1 Basic Principles
Das Modell basiert auf der Common-Pool-Theory
Die zentrale Frage die sich dieses Modell stellt lautet ob nicht nur Ressourcen sondern auch soziale Regelstrukturen den Ausgang bestimmen.
Individuelle Nutzenmaximierung vs. kooperatives Verhalten.

### 4.2 Emergence
In diesem Modell können verschiedene Makro Muster entstehen wie der Kollaps des Fischbestandes, Cluster von räumlicher Überfischung, Dominanz einzelner Strategien und die durchsetzung von sozialen Verhaltensregeln.

### 4.3 Adaptation
Die Fischer passen ihr Verhalten durch Regeln/ Imitation des Nachbarns / Wahrnehmung des sinkend Fischbestandes / Sanktionen an

### 4.4 Sensing
Durch Beobachtung erfolgt Lernen/Annäherung an das Verhalten der Beobachteten. 

### 4.6 Stochasticity
Bei einzelnen Faktoren wird ein Zufallsmechanismus eingebaut, wie z.B. .

### 4.7 Objectives
Die Fischer verfolgen - abhängig vom "Kooperationsfaktor" - die persönliche Ertragsmaximierung bis hin zu einem Fischertrag, der den Erhalt des Gemeinguts ermöglicht,samt den Stufen zwischen diesen Extremen. 

### 4.8 Learning
Die Agenten lernen durch die Beobachtung der anderen Fischer und einer vereinfachten Form von reinforcement learning. Beobachtung ist möglich, wenn sie sich in unmittelbar benachbarten Feldern befinden. 

## Details

### 5) Initialization
Anzahl der Fischer, gesamt: 20
Verteilung der Fischer auf dem See: Zufallsfaktor einstellen für Verteilung auf dem See (mit/ohne direkt angrenzendem Nachbar-Fischer)
Strategie-/Verhalten: Zufallsfaktor für "koop_Faktor" 
Fischanzahl im See, gesamt: 1.000 (max. Kapazität)
Patch-Raster: 10x10 Felder
Verteilung der Fische im See: gleichverteilt 10 je Patch
Regenerationsfaktor der Fische pro Runde: reg_Faktor = 0,1 (10%)

### 6) Input Data
-

### 7) Submodels

Pro Zeitschritt:

Fische im Patch
- Am Ende jedes Zeitschritts regeneriert sich der Fischbestand in jenen Patches, in denen nicht gefischt wird, um Reg_Faktor = 0,1 (10%), sofern die maximale Kapazität nicht erreicht ist bzw. bis zum Erreichen der maximalen Kapazität. Ausnahme: Der Fischbestand < 2.
- Wechseln Fische zwischen den Feldern? Eher nicht. Damit gibt es Felder, die nur mehr leergefischt werden können. Eine Erholung ist aber nicht mehr möglich. 
- Am Ende jedes Zeitschritts wird der Fischbestand je Patch und für den gesamten See gespeichert. Wenn mehr als 2/3 der Felder weniger als 2 Fische beinhalten, bricht die Simulation vorzeitig ab. 

Fischen:
- Auf Basis der bestehenden Strategie/Verhaltensregel, die beim jeweiligen Fischer hinterlegt ist, wird gefischt: koop_Faktor = 0 (absolut egoistisch) bis 1 (absolut kooperativ), dazwischen Mischformen. Wenn der koop_Faktor = 1, dann fischt der Fischer nur so viel aus dem Patch, wie der reg_Faktor pro Zeitschritt ersetzt (10%) und zieht am Ende jeden Schritts zum nächsten Patch weiter. Wenn der koop_Faktor = 0, dann fischt der Fischer in einem Zeitschritt den Patch leer und zieht weiter. Die Mischformen gehen in Zehntelschritten von einem Extrem ins andere Extrem. 
- Das Fischergebnis wird jedem Fischer am Ende des Zeitschritts zu seinem bisherigen Fischfang-Stand addiert. 

Strategie/Verhaltensregel überprüfen/neu festlegen:
- Treffen sich zwei Fischer in unmittelbar sich berührenden Patsches, dann nähern sie sich im Verhalten an. Am Ende des Zeitschritts lernen die Fischer von ihren unmittelbaren Nachbarn und adaptieren ihre Strategie/ihr Verhalten um den lern_Faktor = 0,1 in Richtung des Nachbarfischers (Z.B. Treffen am Nachbarfeld von Fischer 17 mit koop_Faktor=0,3 (plus 0,1) und Fischer 2 mit koop_Faktor=0,8 (-0,1)).
-Treffen sich die Fischer nicht, sinkt der koop_Faktor je Zeitschritt um 0,1. 

Bestärkung/Bestrafung:
- Bestrafung: Fischt ein Fischer mit einem koop_Faktor<=0,2 oder ein Patch auf unter 2 Fische, dann wird er bestraft. 50% seines Fischerfolgs wird auf die anderen Fischer zu gleichen Teilen aufgeteilt und dafür sein koop_Faktor um 0,5 erhöht.
- Bestärkung: Fischt ein Fischer mit einem koop_Faktor >=0,8, ...?

Zum nächsten Patch bewegen oder nicht?
- Der koop_Faktor des Fischers wird mit dem Fischbestand des Patch am Ende des Zeitschritts verglichen. Bei einem koop_Faktor von 0 bis 0,2 und 0,8 bis 1 ziehen die Fischer weiter. Bei einem koop_Faktor dazwischen nicht, außer wenn der Fischbestand < 0,5*max_Kap ist.
In welchen Patch bewegen?
- Wenn der Fischer wechselt, dann zufallsgesteuert in eines der max. 8 möglichen Umgebungsfelder (je nach Position am See). Wie umgehen mit den Seegrenzen bzw. weniger als 8 Möglichkeiten (Koordinatensytem)? 

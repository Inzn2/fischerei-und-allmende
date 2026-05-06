ODD - Protokoll Fischerei und Allmende

## 1. Purpose and Patterns
Das Ziel dieses Modelles ist es, die Dynamik der gemeinschaftlichen Nutzen Ressourcen anhand des Beispiels eines Fischbestandes in einem See darzustellen. Hierbei gibt es zwei zentrale Perspektiven, die genauer betrachtet werden. Der erste Ansatz bezieht sich auf die zwangsläufige Übernutzung und Zerstörung der gemeinsam genutzten Ressourcen und der andere Ansatz soll zeigen, dass durch Regeln, an welche sich die Gemeinschaft hält, ein gemeinschaftlicher Nutzen möglich ist.
In diesem Modell sollen folgende Punkte analysiert werden:
- Wann bricht der Fischbestand zusammen
- Wann ist eine nachhaltige Nutzung möglich
- Welche Verhaltensregeln beeinflussen den Fischbestand
- Welche Muster führen zur Überfischung


## 2. Entities, State Variables, and Scales
Der See wird in einem zweidimensionalen Grid dargestellt, wobei jede Zelle des Gitters einen Fisch Patch darstellen soll.
Variablen:
- fischerman_stock
- fish_stock:
- max_capacity_patch:
- growth_rate:
- decrease_rate:
- behave_rate
- learning_faktor
- position



## 3. Process Overview and Scheduling
4 verschiedene Szenarien
1. Der Fischertrag wird maximiert ohne Rücksicht auf Nachhaltigkeit
2. Der Fischer passt seine Strategie an den erfolgreichsten Fischer an
3. Der Fischer fischt nachhaltig wenn es sein Nachbar auch tut
4. Alle Fischer kooperieren und fischen Nachhaltig, und werden bei Nichteinhaltung sanktioniert

Pro Zeitschritt passiert folgendes:

- Fische im Patch (Regeneration/Diffusion)
- Fischer (auf Basis Strategie/Verhaltensregel. Fischerfolg pro Fischer verfolgen.)
- Strategie/Verhaltensregel überprüfen/neu festlegen (Lernen oder Verlernen)
- Bestärkung/Bestrafung
- Bewegen oder nicht (Patch wechseln oder nicht)


## 4. Design Concepts
# 4.1 Basic Principles
Das Modell basiert auf der Common-Pool-Theory
Die zentrale Frage die sich dieses Modell stellt lautet ob nicht nur Ressourcen sondern auch soziale Regelstrukturen den Ausgang bestimmen.

# 4.2 Emergence
In diesem Modell können verschiedene Makro Muster entstehen wie der Kollaps des Fischbestandes, Cluster von räumlicher Überfischung, Dominanz einzelner Strategien und die durchsetzung von sozialen Verhaltensregeln

# 4.3 Adaptation
Die Fischer passen ihr Verhalten durch Regeln/ Imitation des Nachbarns / Wahrnehmung des sinkend Fischbestandes / Sanktionen an

# 4.4 Objectives
Jeder Fischer verfolgt primär das Ziel seinen Fischertrag zu maximieren, jedoch unter der Berücksichtigung von der Vermeidungen von Sanktionen, das Erhalten von Fangmöglichkeiten/erhaltung des Ökosystems und der aufgestellten Verhaltensregeln

# 4.5 Learning
Die Agenten lernen durch die Beobachtung der anderen Fischer und einer vereinfachten Form von reinforcement learning

# 4.5 Prediction
/

# 4.6 Sensing
Fischer können ihren eigenen Fang, den lokalen Fischbestand im aktuellen Patch sowie (je nach Szenario) den Erfolg und/oder das Verhalten benachbarter Fischer wahrnehmen. Die Wahrnehmung ist lokal auf benachbarte Zellen (Moore-Nachbarschaft) beschränkt.

# 4.7 Interaction
Interaktionen erfolgen indirekt über die Ressource (Fischbestand) sowie direkt über soziale Mechanismen:

- Konkurrenz um Fisch im selben oder benachbarten Patch
- Imitiation erfolgreicher Nachbarn
- Konditionale Kooperation basierend auf Nachbarschaftsverhalten
- Sanktionen gegenüber Übernutzern (z.B. Reduktion ihres Ertrags)

# 4.8 Stochasticity
Zufall tritt auf bei:
- Initialverteilung der Fischer im Raum (Anfang varriert)
- Verhaltensentscheidungen
Ein Random Seed wird gesetzt, um Reproduzierbarkeit zu gewährleisten

# 4.9 Collectives
/

# 4.10 Observation
Wichtige Outputgrößen:
- Gesamtfischbestand über Zeit
- Durchschnittlicher Ertrag pro Fischer
- Anteil der jeweiligen Verhaltensstrategien
- Häufigkeit und Wirkung von Sanktionen

## 5. Initialization
Der See wird als 10x10 Gitter initialisiert

Jeder Patch erhält:
- Anfangsbestand fish_stock 
- Parameter max_capacity_patch 
- growth_rate 

Fischer:
- Anzahl M wird festgelegt
- Zufällige Startpositionen im Grid

Anfangsverhalten je nach Szenario
Random Seed wird gesetzt

## 6. Input Data
Externe, zeitabhängige Daten sind im Basismodell nicht erforderlich.

## 7. Submodels
# 7.1 Fischdynamik
Logistisches Wachstum pro Patch:
Wachstum abhängig von growth_rate und max_capacity_patch

Diffusion: Abgleich mit den Umgebungs Patches 

- Am Ende jedes Zeitschritts regeneriert sich der Fischbestand in jenen Patches, in denen nicht gefischt wird, um Reg_Faktor = 0,1 (10%), sofern die maximale Kapazität nicht erreicht ist bzw. bis zum Erreichen der maximalen Kapazität. Ausnahme: Der Fischbestand < 2.
- Wechseln Fische zwischen den Feldern? Eher nicht. Damit gibt es Felder, die nur mehr leergefischt werden können. Eine Erholung ist aber nicht mehr möglich. 
- Am Ende jedes Zeitschritts wird der Fischbestand je Patch und für den gesamten See gespeichert. 

# 7.2 Fischerei (Erntefunktion)
Fischer entnehmen abhängig von ihrer Strategie eine Menge Fisch aus ihrem aktuellen Patch
Entnahme reduziert fish_stock direkt

- Auf Basis der bestehenden Strategie/Verhaltensregel, die beim jeweiligen Fischer hinterlegt ist, wird gefischt: behave_rate = 0 (absolut egoistisch) bis 1 (absolut kooperativ), dazwischen Mischformen. Wenn der behave_rate = 1, dann fischt der Fischer nur so viel aus dem Patch, wie der growth_rate pro Zeitschritt ersetzt (z.b.10%) und zieht am Ende jeden Schritts zum nächsten Patch weiter. Wenn der behave_rate = 0, dann fischt der Fischer in einem Zeitschritt den Patch leer und zieht weiter. Die Mischformen gehen in Zehntelschritten von einem Extrem ins andere Extrem. 


# 7.3 Verhaltensregeln der Fischer
- Maximierung: maximal mögliche Entnahme
- Imitation: Übernahme der Strategie des erfolgreichsten Nachbarn
- Konditionale Kooperation: nachhaltige Nutzung, wenn Nachbarn kooperieren
- Sanktionierung: Bestrafung von Übernutzern (z.B. Kosten oder Fangreduktion)

- Treffen sich zwei Fischer in unmittelbar sich berührenden Patsches, dann nähern sie sich im Verhalten an. Am Ende des Zeitschritts lernen die Fischer von ihren unmittelbaren Nachbarn und adaptieren ihre Strategie/ihr Verhalten um den learning_faktor = 0,1 in Richtung des Nachbarfischers (Z.B. Treffen am Nachbarfeld von Fischer 17 mit behave_rate=0,3 (plus 0,1) und Fischer 2 mit behave_rate=0,8 (-0,1)).

Zum nächsten Patch bewegen oder nicht?
- Der behave_rate des Fischers wird mit dem Fischbestand des Patch am Ende des Zeitschritts verglichen. Bei einem behave_rate von 0 bis 0,2 und 0,8 bis 1 ziehen die Fischer weiter. Bei einem behave_rate dazwischen nicht, außer wenn der Fischbestand < 0,5*max_Kap ist.
- Wenn der Fischer wechselt, dann zufallsgesteuert in eines der max. 8 möglichen Umgebungsfelder (je nach Position am See). 

# 7.4 Anpassung / Lernen
Strategiewechsel basierend auf Vergleich von Erträgen
Optional probabilistische Anpassung (Reinforcement-ähnlich)

# 7.5 Sanktionen
Identifikation von Übernutzung (z.B. über Schwellenwerte)
Anwendung von Strafen durch andere Agenten oder globales Regelwerk:(z.B. Kosten oder Fangreduktion)
Bestärkung/Bestrafung:
- Bestrafung: Fischt ein Fischer mit einem behave_rate<=0,2 oder ein Patch auf unter 2 Fische, dann wird er bestraft. Darf im nächsten Zeitschritt nicht fischen.



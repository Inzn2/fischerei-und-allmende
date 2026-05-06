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
Variablen des Grids
- fish_stock:
- max_capacity:
- growth_rate:
- decrease_rate:
Variablen der Agenten
- behave
- position


## 3. Process Overview and Scheduling
4 verschiedene Szenarien
1. Der Fischertrag wird maximiert ohne Rücksicht auf Nachhaltigkeit
2. Der Fischer passt seine Strategie an den erfolgreichsten Fischer an
3. Der Fischer fischt nachhaltig wenn es sein Nachbar auch tut
4. Alle Fischer kooperieren und fischen Nachhaltig, und werden bei Nichteinhaltung sanktioniert


## 4. Design Concepts
# 4.1 Basic Principles
Das Modell basiert auf der Common-Pool-Theory
Die zentrale Frage die sich dieses Modell stellt lautet ob nicht nur Ressourcen sondern auch soziale Regelstrukturen den Ausgang bestimmen.

# 4.2 Emergence
In diesem Modell können verschiedene Makro Muster entstehen wie der Kollaps des Fischbestandes, Cluster von räumlicher Überfischung, Dominanz einzelner Strategien und die durchsetzung von sozialen Verhaltensregeln

# 4.3 Adaptation
Die Fischer passen ihr Verhalten durch Regeln/ Imitation des Nachbarns / Wahrnehmung des sinkend Fischbestandes / Sanktionen an

# 4.4 Objectives
Jeder Fischer verfolgt primär das Ziel seinen Fischertrag zu maximieren, jedoch unter der Berücksichtigung von der Vermeidungen von Sanktionen, das Erhalten von Fangmöglichkeiten und der aufgestellten Verhaltensregeln

# 4.5 Learning
Die Agenten lernen durch die Beobachtung der anderen Fischer und einer vereinfachten Form von reinforcement learning

# 4.5 Predictions
Sind in dem Modell nicht wesentlich

################################################## 

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
- Anfangsbestand der Fische (optional)
- Verhaltensentscheidungen
Ein Random Seed wird gesetzt, um Reproduzierbarkeit zu gewährleisten

# 4.9 Collectives
Es können sich Gruppen von Fischern mit ähnlichen Strategien bilden (z.B. Cluster kooperativer Agenten). Diese wirken als funktionale Einheiten, indem sie lokal nachhaltige Nutzung stabilisieren oder Übernutzung verstärken.

# 4.10 Observation
Wichtige Outputgrößen:
- Gesamtfischbestand über Zeit
- Durchschnittlicher Ertrag pro Fischer
- Anteil der jeweiligen Verhaltensstrategien
- Räumliche Verteilung von Überfischung (Clusterbildung)
- Häufigkeit und Wirkung von Sanktionen

## 5. Initialization
Der See wird als N×N Gitter initialisiert

Jeder Patch erhält:
- Anfangsbestand fish_stock (hätten hier jetzt zufällig (siehe 4.8. gewählt))
- Parameter max_capacity und growth_rate

Fischer:
- Anzahl M wird festgelegt
- Zufällige Startpositionen im Grid

Anfangsverhalten je nach Szenario
Random Seed wird gesetzt

## 6. Input Data
Externe, zeitabhängige Daten sind im Basismodell nicht erforderlich.
Optional könnten reale Daten integriert werden, z.B.:

saisonale Wachstumsraten
Umweltveränderungen (Temperatur, Verschmutzung)
Diese sind jedoch nicht Teil des Kernmodells.

## 7. Submodels
# 7.1 Fischdynamik
Logistisches Wachstum pro Patch:
Wachstum abhängig von growth_rate und max_capacity

Diffusion:
Ein Teil der Fische wandert in benachbarte Zellen

# 7.2 Fischerei (Erntefunktion)
Fischer entnehmen abhängig von ihrer Strategie eine Menge Fisch aus ihrem aktuellen Patch
Entnahme reduziert fish_stock direkt

# 7.3 Verhaltensregeln der Fischer
- Maximierung: maximal mögliche Entnahme
- Imitation: Übernahme der Strategie des erfolgreichsten Nachbarn
- Konditionale Kooperation: nachhaltige Nutzung, wenn Nachbarn kooperieren
- Sanktionierung: Bestrafung von Übernutzern (z.B. Kosten oder Fangreduktion)

# 7.4 Anpassung / Lernen
Strategiewechsel basierend auf Vergleich von Erträgen
Optional probabilistische Anpassung (Reinforcement-ähnlich)

# 7.5 Sanktionen
Identifikation von Übernutzung (z.B. über Schwellenwerte)
Anwendung von Strafen durch andere Agenten oder globales Regelwerk:(z.B. Kosten oder Fangreduktion)


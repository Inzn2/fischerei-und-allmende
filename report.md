# Fischerei und Allmende 

## Abstract
Diese Arbeit untersucht die Frage, wie soziale Nähe und Isolation das Verhalten von Fischer*innen sowie die Stabilität einer gemeinsam genutzten Ressource beeinflussen. Hierzu wurde ein agentenbasiertes Modell entwickelt, in dem 30 Fischer*innen auf einem 20×20-Raster agieren und auf einen gemeinsamen Fischbestand zugreifen. Verglichen werden zwei Szenarien: ein Szenario ohne soziale Regeln, in dem egoistisches Verhalten kontinuierlich zunimmt, und ein Szenario mit sozialen Regeln, in dem Begegnungen zwischen benachbarten Fischer*innen egoistische Tendenzen reduzieren. 
Die Simulationsergebnisse zeigen, dass der Fischbestand ohne soziale Regeln bereits nach kurzer Zeit kollabiert, während soziale Regeln den Kollaps deutlich verzögern und den Bestand über einen langen Zeitraum auf hohem Niveau stabilisieren. Bei einer Verlängerung der Simulation auf 300 Zeitschritte wird jedoch deutlich, dass auch dieses Szenario langfristig nicht vollständig nachhaltig ist. Die Ergebnisse legen wenngleich nahe, dass nicht räumliche Nähe allein, sondern deren Einfluss auf das Verhalten der Akteur*innen entscheidend für die nachhaltige Nutzung gemeinsam genutzter Ressourcen ist. Die Aussagekraft des Modells wird jedoch durch seine bewusste Vereinfachung begrenzt, insbesondere durch die Modellierung eines einzigen globalen Fischbestands sowie die Reduktion sozialer Interaktionen auf eine einfache Verhaltensanpassungsregel.

## 1. Introduction
Die nachhaltige Nutzung gemeinsam genutzter natürlicher Ressourcen stellt eine zentrale Herausforderung sozial-ökologischer Systeme dar. Besonders deutlich wird dieses Problem am Beispiel von Fischbeständen: Einzelne Nutzer*innen profitieren kurzfristig von einer möglichst hohen Entnahme, während die langfristigen Folgen einer Übernutzung von allen Beteiligten getragen werden. Die Frage, unter welchen Bedingungen gemeinsame Ressourcen nachhaltig genutzt werden können, bildet daher einen wichtigen Forschungsgegenstand der Commons-Forschung.

Einen einflussreichen theoretischen Ausgangspunkt liefert Garrett Hardins Essay The Tragedy of the Commons (1968). Hardin argumentiert, dass individuell rationales und nutzenmaximierendes Verhalten bei gemeinsam genutzten Ressourcen langfristig zu deren Übernutzung führen kann. Da die unmittelbaren Vorteile einer erhöhten Nutzung den einzelnen Akteur*innen zugutekommen, die negativen Folgen jedoch von der gesamten Gemeinschaft getragen werden, entsteht ein Anreiz zur fortschreitenden Ausweitung der Ressourcennutzung. In Hardins Modell führt diese Dynamik letztlich zum Zusammenbruch der Ressource.

Einen wichtigen Gegenpol zu dieser Perspektive bildet Elinor Ostroms Werk Governing the Commons (1990). Auf Grundlage zahlreicher empirischer Fallstudien zeigte Ostrom, dass Gemeinschaften durchaus in der Lage sind, gemeinsame Ressourcen langfristig und nachhaltig zu verwalten. Entscheidend sind dabei soziale Regeln und Institutionen, die das Verhalten der Nutzer*innen beeinflussen und koordinieren. Ostrom identifizierte verschiedene Gestaltungsprinzipien erfolgreicher Selbstverwaltung und stellte damit die Annahme infrage, dass ein Ressourcenkollaps zwangsläufig eintreten müsse.

Aufbauend auf diesen Überlegungen untersuchte Marco Janssen (2010) die Wechselwirkungen zwischen menschlichem Verhalten und ökologischer Dynamik in sogenannten Common-Pool-Resource-Experimenten. Während viele frühere Untersuchungen ökologische Prozesse nur vereinfacht berücksichtigten, integrierte Janssen die Dynamik der Ressource selbst stärker in experimentelle und simulationsbasierte Ansätze. Dadurch rückte die Betrachtung von sozio-ökologischen Systemen in den Mittelpunkt, in denen menschliches Verhalten und ökologische Entwicklung wechselseitig aufeinander einwirken.

Ausgehend von diesen theoretischen Überlegungen wurde für die vorliegende Arbeit ein bewusst stark vereinfachtes agentenbasiertes Modell entwickelt. Im Mittelpunkt steht dabei nicht die detaillierte ökologische Beschreibung eines Fischbestands, sondern die Frage, wie soziale Nähe beziehungsweise Isolation das Verhalten von Nutzer*innen beeinflusst. Das Modell konzentriert sich daher auf die Wechselwirkung zwischen räumlicher Begegnung, Verhaltensanpassung und Ressourcennutzung.

Die zentrale Forschungsfrage lautet:

Wie beeinflussen soziale Begegnungen und räumliche Isolation das Fischverhalten der Fischer*innen und die langfristige Entwicklung einer gemeinsam genutzten Ressource?

Zur Untersuchung dieser Fragestellung werden zwei Szenarien miteinander verglichen. Im ersten Szenario existieren keine sozialen Regeln, sodass sich die Fischer*innen unabhängig von ihrer Umgebung zunehmend egoistisch verhalten. Im zweiten Szenario beeinflussen Begegnungen zwischen benachbarten Fischer*innen das Verhalten unmittelbar, indem soziale Nähe egoistische Tendenzen reduziert und Isolation diese verstärkt. Durch den Vergleich beider Szenarien soll untersucht werden, welchen Beitrag soziale Interaktion zur Stabilisierung gemeinsamer Ressourcen leisten kann und welche Folgen sich ergeben, wenn soziale Einbettung und gegenseitige Wahrnehmung fehlen.

## 2. Method

### Modellaufbau und Simulationsumgebung
Das Modell wurde als agentenbasierte Simulation in Python implementiert. Die tatsächliche Modellbeschreibung orientiert sich an der implementierten Version des Codes. Die Simulationsumgebung besteht aus einem zweidimensionalen Raster mit einer Größe von 20×20 Feldern. Die Felder dienen ausschließlich zur räumlichen Positionierung der Fischer*innen und besitzen keine eigenen Fischbestände. Die Simulation läuft über 200 diskrete Zeitschritte. Alle Fischer*innen werden zu Beginn zufällig auf dem Raster verteilt. Die Bewegung und Interaktion der Akteur*innen erfolgen ausschließlich innerhalb dieser räumlichen Umgebung.


### Fischbestand
Der Fischbestand wird als eine einzige globale Ressource für den gesamten See modelliert. Im Gegensatz zu früheren Konzeptüberlegungen existieren keine lokalen Fisch-Patches und keine räumlich verteilten Fischpopulationen. Alle Fischer*innen greifen auf denselben gemeinsamen Bestand zu.
Die wichtigsten Parameter lauten:
Anfangsbestand "start_fish"= 5000 Fische
Maximale Kapazität "max_fish" = 5000 Fische
Minimalbestand "min_fish" = 0 Fische
Regenerationsrate "regen_rate" = 3,66% pro Zeitschritt

Der Fischbestand wird nach jedem Zeitschritt regeneriert und kann die maximale Kapazität nicht überschreiten.

### Fischer*innen-Agenten
Das Modell enthält 30 Fischer*innen, die als autonome Agenten implementiert sind. Jede Person besitzt drei Zustandsvariablen:
x-Position auf dem Raster
y-Position auf dem Raster
Verhaltenswert („behavior“)
Alle Fischer*innen starten mit einem Verhaltenswert von 1 und damit maximal kooperativem Verhalten. Der Verhaltenswert liegt stets zwischen 1 und 9.
Die Bedeutung des Verhaltenswerts ist unmittelbar mit der Fangmenge verknüpft:
Interpreation Verhaltenswert:
1 … stark kooperatuv
2-3 … kooperativ
4-6 … mittleres verhalten
7-8 … egoistisch
9 … maximal egoistisch
Der Verhaltenswert bestimmt direkt die Anzahl der Fische, die eine Person pro Zeitschritt fängt. Ein*e Fischer*in mit Verhalten 1 entnimmt einen Fisch pro Zeitschritt, ein*e Fischer*in mit Verhalten 9 entsprechend neun Fische.

### Nachbarschaft und soziale Nähe
Die Wahrnehmung anderer Fischer*innen erfolgt über eine Moore-Nachbarschaft. Dabei werden alle acht unmittelbar angrenzenden Felder berücksichtigt.
Der folgende Codeausschnitt implementiert diese Nachbarschaftsdefinition.
```python
def get_neighbors(self, fisher):
    neighbors = []
    for other in self.fishers:
        if other is fisher:
            continue

        dx = abs(fisher["x"] - other["x"])
        dy = abs(fisher["y"] - other["y"])

        if dx <= 1 and dy <= 1:
            neighbors.append(other)

    return neighbors
```
Technisch überprüft die Funktion, welche Fischer*innen höchstens ein Feld horizontal, vertikal oder diagonal entfernt sind. Die Modellannahme besteht darin, dass soziale Wahrnehmung nur lokal erfolgt. Die Auswirkungen dieser Regel sind zentral für die Forschungsfrage, da Begegnungen innerhalb dieser Nachbarschaft das spätere Verhalten beeinflussen können.

### Fischfang
Zu Beginn jedes Zeitschritts wird Fischfang betrieben. Die individuelle Fangmenge entspricht unmittelbar dem aktuellen Verhaltenswert.
Die Gesamtfangmenge ergibt sich schließlich aus der Summe aller individuellen Fangmengen.
Falls die gewünschte Gesamtfangmenge größer ist als der aktuell verfügbare Bestand, wird lediglich der verbleibende Fischbestand entnommen, der Bestand kann somit niemals negativ werden. Die tatsächliche Fangmenge wird für jeden Zeitschritt gespeichert und zusätzlich als kumulierter Gesamtfang dokumentiert.

### Verhaltensanpassung
Die Verhaltensanpassung stellt den zentralen Mechanismus des Modells dar. Hier unterscheiden sich die beiden untersuchten Szenarien.
Der entsprechende Code hierzu sieht wie folgt aus.
```python
def adapt_behavior(self):
    for fisher in self.fishers:
        neighbors = self.get_neighbors(fisher)

        if self.rules:
            if len(neighbors) > 0:
                fisher["behavior"] -= 1
            else:
                fisher["behavior"] += 1
        else:
            fisher["behavior"] += 1
```
Der Code implementiert die Verhaltensanpassung der Fischer*innen in jedem Zeitschritt. Im Szenario mit Regeln wird zunächst geprüft, ob sich andere Fischer*innen in der Moore-Nachbarschaft befinden. Ist dies der Fall, wird der Verhaltenswert um eins reduziert, wodurch die betreffende Person kooperativer wird. Befindet sich ein*e Fischer*in hingegen in Isolation, steigt der Verhaltenswert um eins und damit auch die Tendenz zu egoistischem Verhalten. Im Szenario ohne Regeln erhöht sich der Verhaltenswert unabhängig von der Anwesenheit anderer Akteur*innen kontinuierlich. Die zugrunde liegende Modellannahme lautet, dass soziale Begegnungen Rücksichtnahme und kooperatives Verhalten fördern, während Isolation egoistische Verhaltensweisen begünstigt. Dieser Mechanismus bildet den zentralen Unterschied zwischen beiden Szenarien und bestimmt maßgeblich die langfristige Entwicklung des Fischbestands.

### Szenario ohne Regeln
Im Szenario ohne Regeln besitzen Begegnungen keinerlei soziale Bedeutung. Unabhängig von ihrer Umgebung werden alle Fischer*innen in jedem Zeitschritt egoistischer. Der Verhaltenswert steigt kontinuierlich um eins an, bis die Obergrenze von 9 erreicht wird.
Dadurch nimmt die Fangmenge dauerhaft zu, was den Druck auf die Ressource kontinuierlich erhöht.

### Szenario mit Regeln
Im Szenario mit Regeln beeinflussen soziale Begegnungen das Verhalten unmittelbar.

Treffen Fischer*innen auf mindestens eine*n Nachbarn*in, sinkt ihr Egoismus.
Befinden sie sich isoliert, steigt ihr Egoismus.
Der Verhaltenswert bleibt stets zwischen 1 und 9 begrenzt.

Die zentrale Modellannahme lautet somit, dass soziale Nähe Rücksichtnahme erzeugt, während Isolation egoistisches Verhalten begünstigt.
Diese einfache Regel erzeugt die wesentlichen Unterschiede zwischen beiden Simulationen und bildet die theoretische Verbindung zu Ostroms Überlegungen über die Bedeutung sozialer Institutionen und gemeinsamer Regeln.

### Bewegung der Fischer*innen
Nach der Verhaltensanpassung bewegen sich die Fischer*innen zufällig über das Raster. Pro Zeitschritt kann eine Bewegung um maximal ein Feld in horizontaler, vertikaler oder diagonaler Richtung erfolgen. Bewegungen außerhalb der Grenzen des Sees sind nicht zulässig. Zudem können bereits von anderen Fischer*innen besetzte Felder nicht betreten werden. Durch die zufällige Bewegung entstehen fortlaufend neue räumliche Konstellationen, wodurch sich Begegnungen und Phasen der Isolation dynamisch verändern. Da die Verhaltensanpassung unmittelbar von der lokalen Nachbarschaft abhängt, stellt die Bewegung einen zentralen Mechanismus für die Entstehung der sozialen Dynamik im Modell dar.

### Regeneration des Fischbestands
Nach dem Fischfang wächst der Fischbestand entsprechend einer festgelegten Regenerationsrate. Der entsprechende Mechanismus ist im folgenden Code dargestellt.
```python
def regenerate_fish(self):
    self.fish_stock += self.fish_stock * regen_rate

    if self.fish_stock > max_fish:
        self.fish_stock = max_fish
```
Der Code implementiert einen proportionalen Wachstumsprozess, bei dem der aktuelle Fischbestand in jedem Zeitschritt um 3,66 % erhöht wird. Anschließend wird überprüft, ob die maximale Kapazität des Sees überschritten wird. In diesem Fall wird der Bestand auf den festgelegten Maximalwert von 5000 Fischen begrenzt.

Die Modellannahme besteht darin, dass sich größere Bestände schneller erholen als kleinere Bestände, da das Wachstum proportional zur vorhandenen Population erfolgt. Die Regenerationsrate von 3,66 % wurde dabei so gewählt, dass der Fischbestand bei kooperativem Verhalten langfristig erhalten bleiben kann, während eine dauerhaft hohe Entnahme durch egoistisches Verhalten weiterhin zu einer Übernutzung der Ressource führt. Dadurch wird sichergestellt, dass die beobachteten Unterschiede zwischen den beiden Szenarien primär auf die soziale Dynamik der Fischer*innen und nicht ausschließlich auf die ökologische Regeneration zurückzuführen sind.

Der Regenerationsmechanismus wirkt dem durch den Fischfang verursachten Bestandsrückgang entgegen und bestimmt gemeinsam mit dem Verhalten der Fischer*innen, ob die Ressource langfristig stabil bleibt oder kollabiert.

### Datenspeicherung
Während der Simulation werden mehrere Kenngrößen gespeichert:
Fischbestand pro Zeitschritt (history)
Fangmenge pro Zeitschritt (catch_per_step)
kumulierte Gesamtfangmenge (total_caught)
Diese Daten bilden die Grundlage für die spätere Auswertung der Ressourcenentwicklung und des Entnahmedrucks.

### Visualisierung
Zur Analyse werden zwei parallele Simulationen dargestellt:
1.	Szenario ohne Regeln
2.	Szenario mit Regeln
Die Fischer*innen werden farblich nach ihrem Verhalten codiert, hierbei steht die Farbe Grün für ein kooperatives Verhalten (1–3), Gelb verdeutlicht ein mittleres Verhalten (4–6) und die Visualisierung in Rot zeigt egoistisch (7–9)an.
Zusätzlich wird während der Simulation der aktuelle Fischbestand angezeigt. Nach Abschluss wird die Entwicklung des Fischbestands beider Szenarien in einem Vergleichsdiagramm dargestellt.

### Verwendete Bibliotheken
#### matplotlib.pyplot
Die Bibliothek matplotlib.pyplot übernimmt die grafische Darstellung des Modells. Sie wird verwendet, um die Positionen der Fischer*innen auf dem Raster darzustellen, die Vergleichsgrafiken des Fischbestands zu erzeugen und die Ergebnisse visuell auszuwerten.

#### matplotlib.animation.FuncAnimation
FuncAnimation ermöglicht die zeitliche Animation der Simulation. Nach jedem Zeitschritt werden beide Szenarien aktualisiert und neu gezeichnet, wodurch die Entwicklung des Systems in Echtzeit beobachtet werden kann.

### random
Die Bibliothek random steuert sämtliche Zufallsprozesse des Modells. Dazu gehören die zufällige Initialisierung der Positionen, die zufälligen Bewegungen der Fischer*innen sowie die Verwendung eines festen Seeds zur Reproduzierbarkeit der Simulationsergebnisse.


## 3. Results
Zur Untersuchung der Forschungsfrage wurden zwei Szenarien mit identischen Ausgangsbedingungen simuliert. Der einzige Unterschied bestand in der Verhaltensanpassung der Fischer*innen. Zur Auswertung wurden sowohl die räumliche Verteilung der Agent*innen als auch die zeitliche Entwicklung des Fischbestands betrachtet.

### Szenario ohne Regeln
Abbildung 1 zeigt den Zustand der Simulation nach 200 Zeitschritten im Szenario ohne soziale Regeln.

![Abbildung 1: Endzustand ohne Regeln nach 200 Schritten](Abbildung1_Endzustand_ohne_regel_200.png)

Im Szenario ohne Regeln entwickelt sich das Verhalten aller Fischer*innen schrittweise in Richtung maximaler Egoismus. Da der Verhaltenswert in jedem Zeitschritt ansteigt und schließlich die Obergrenze von 9 erreicht, nimmt auch die gesamte Fangmenge kontinuierlich zu.

Wie in Abbildung 1 erkennbar, beträgt der Fischbestand nach 200 Zeitschritten 0 Fische. Gleichzeitig sind ausschließlich rote Agent*innen sichtbar, was darauf hinweist, dass alle Fischer*innen den maximalen Verhaltenswert erreicht haben.

Die zeitliche Entwicklung des Fischbestands ist in Abbildung 2 dargestellt.

![Abbildung 2: Fischbestand nach 200 Schritten](Abbildung2_Fischbestand_200.png)

Die rote Kurve zeigt, dass der Bestand bereits nach ungefähr 40 Zeitschritten vollständig erschöpft ist. Der eigentliche Ressourcenkollaps tritt somit deutlich früher ein als der dargestellte Endzustand der Simulation.

Da der Programmcode kein Abbruchkriterium bei leerem Fischbestand enthält, bewegen sich die Fischer*innen auch nach dem Kollaps weiterhin über das Raster und passen ihr Verhalten an. Die Endpositionen der Agent*innen repräsentieren daher nicht den Zeitpunkt des Ressourcenkollapses, sondern lediglich den Zustand nach Abschluss der Simulation.

### Szenario mit Regeln
Abbildung 3 zeigt den Zustand des Regel-Szenarios nach 200 Zeitschritten.

![Abbildung 3: Endzustand mit Regeln nach 200 Schritten](Abbildung3_Endzustand_mit_regel_200.png)

Im Szenario mit sozialen Regeln beeinflussen Begegnungen innerhalb der Moore-Nachbarschaft das Verhalten der Fischer*innen. Die Anwesenheit von Nachbar*innen reduziert egoistische Tendenzen, während Isolation diese verstärkt.
Nach 200 Zeitschritten beträgt der Fischbestand 4970 Fische und liegt damit nur geringfügig unter der maximalen Kapazität von 5000 Fischen. Gleichzeitig existieren kooperative (grün), mittlere (gelb) und egoistische (rot) Verhaltensweisen nebeneinander. Dies deutet auf ein dynamisches Gleichgewicht unterschiedlicher Strategien hin.

Die grüne Kurve in Abbildung 2 bestätigt diesen Befund. Über nahezu den gesamten Simulationszeitraum bleibt der Bestand nahe der maximalen Kapazität und zeigt lediglich temporäre Schwankungen. Die niedrigsten Werte liegen bei etwa 4550 Fischen, bevor sich der Bestand erneut erholt.

### Langfristige Entwicklung
Um die Stabilität des Systems über einen längeren Zeitraum zu untersuchen, wurde die Simulation zusätzlich auf 300 Zeitschritte erweitert.

Abbildung 4 zeigt die Entwicklung des Fischbestands für diesen längeren Zeithorizont.

![Abbildung 4: Fischbestand über 300 Zeitschritte](Abbildung4_Fischbestand_300.png)

Während der Fischbestand im Regel-Szenario bis etwa Zeitschritt 200 nahezu stabil bleibt, setzt anschließend ein kontinuierlicher Rückgang ein. Der Bestand sinkt zunächst langsam, beschleunigt sich jedoch im weiteren Verlauf und erreicht gegen Ende der Simulation ebenfalls den Wert 0.

Die zusätzlichen Simulationen zeigen daher, dass die implementierte soziale Regel den Kollaps der Ressource nicht dauerhaft verhindert. Sie verlängert jedoch die Lebensdauer des Systems erheblich. Während die Ressource ohne Regeln bereits nach etwa 40 Zeitschritten kollabiert, bleibt sie mit Regeln über mehr als 200 Zeitschritte weitgehend erhalten.

### Vergleich der Szenarien
Der Vergleich der beiden Szenarien verdeutlicht den Unterschied zwischen räumlicher Nähe und sozial wirksamer Interaktion. In beiden Simulationen bewegen sich die Fischer*innen nach identischen Bewegungsregeln über das Raster und weisen somit vergleichbare Begegnungswahrscheinlichkeiten auf. Dennoch entwickeln sich die Systeme aufgrund der unterschiedlichen Verhaltensanpassung grundlegend verschieden.

Ohne soziale Regeln führt die kontinuierliche Zunahme egoistischen Verhaltens zu einer raschen Übernutzung der Ressource und einem frühzeitigen Kollaps des Fischbestands. Soziale Regeln reduzieren diesen Effekt erheblich und ermöglichen über lange Zeiträume eine stabile Ressourcennutzung. Die langfristigen Simulationen zeigen jedoch, dass die Regel unter den gegebenen Modellannahmen keine vollständige Nachhaltigkeit gewährleistet, sondern den Zusammenbruch der Ressource vor allem verzögert.

Die Ergebnisse legen somit nahe, dass soziale Interaktion einen wesentlichen Beitrag zur Stabilisierung gemeinsamer Ressourcen leisten kann, ihre langfristige Erhaltung jedoch von zusätzlichen Faktoren abhängen dürfte.


## 4. Discussion, Conclusion and Limitations

### Was unser Modell zeigt. 
Auf Grundlage unserer Forschungsfrage (Wie wirkt sich Nähe bzw. Isolation auf das Fisch-Verhalten der Fischer*innen und letztendlich auf die Stabilität der gemeinsam genutzten Ressource aus?) lassen sich folgende Ergebnisse formulieren: Unsere beiden Simulationen zeigen zwar exakt dieselben Bewegungsmuster, führen aber trotzdem zu diametral unterschiedlichen Entwicklungen, was das Verhalten der Fischer*innen am und in weiterer Folge die Stabilität des Fischbestands im See angeht. Die erste Simulation führt trotz Nähe/Begegnung schnell zum Kippen der Ressource, während die zweite sich durch Nähe/Begegnung immer wieder stabilisiert. 

### Warum? 
Uns ging es hier nicht nur um den Wert von Begegnung als Verstärker für soziales Verhalten, sondern auch darum, das dieser Wert nicht perse als solcher verstanden werden kann, ohne ihn als solchen zu pflegen und zu erhalten. Solange eine Begegnung auch damit zu tun hat, sich wahrzunehmen und zu interagieren - im Besten Falle sogar als ein in-Beziehung-treten verstanden werden kann - wird ein soziales Gefüge davon profitieren. Sobald diese Komponenten aber alle wegfallen und man sich trotz der vorhanden örtlichen Nähe isoliert und für sich bleibt, entfällt die Wirkung, was im Vergleich der Simulationen sehr schnell ersichtlich wird. 

### Was unser Modell nicht zeigt. 
Ein Schwachpunkt ist die extreme Vereinfachung. Das menschliche Verhalten ist sehr vielschichtig und komplex. Kaum etwas lässt sich auf Basis einer einfach-formulierbaren Ursache-Wirkungs-Beziehung beschreiben bzw. erklären. In unserem Modell arbeiten wir mit genau einem Parameter. Und gerade darin zeigt sich auch die starke Limitation der Aussagekraf und die bewusst gewählte Eingrenzung des Modells.

Um es realistischer zu machen, müssten wir unsere starken Vereinfachungen zumindest teilweise wieder zurücknehmen und eine Reihe weiterer Parameter aufnehmen. Außerdem bräuchte es eine eingehendere Betrachtung der Wechselwirkungen und Rückkoppelungen in positiver wie negativer Richtung.  
Die Ergebnisse hängen teilweise von der gewählten Simulationsdauer ab. Während das Szenario mit sozialen Regeln nach 200 Zeitschritten nahezu stabil erscheint, zeigt eine Verlängerung auf 300 Zeitschritte einen verzögerten Ressourcenkollaps. Die Interpretation von Stabilität ist daher stets relativ zum betrachteten Zeithorizont.

## References
Hardin, G. (1968). The Tragedy of the Commons. Science, 162(3859), 1243–1248
Janssen, M. A. (2010). Introducing ecological dynamics into common-pool resource experiments. Ecology and Society, 15(2), Article 8
Ostrom, E. (1990). Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge: Cambridge University Press

## Appendix A: ODD


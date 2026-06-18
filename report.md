# Fischerei und Allmende 

## Abstract
Diese Arbeit untersucht die Frage, wie soziale Nähe und Isolation das Verhalten von Fischer*innen sowie die Stabilität einer gemeinsam genutzten Ressource beeinflussen. Hierzu wurde ein agentenbasiertes Modell entwickelt, in dem 30 Fischer*innen auf einem 20×20-Raster agieren und auf einen gemeinsamen Fischbestand zugreifen. Verglichen werden zwei Szenarien: ein Szenario ohne soziale Regeln, in dem egoistisches Verhalten kontinuierlich zunimmt, und ein Szenario mit sozialen Regeln, in dem Begegnungen zwischen benachbarten Fischer*innen egoistische Tendenzen reduzieren. Die Simulationsergebnisse veranschaulichen, dass der Fischbestand ohne soziale Regeln bereits vor dem Ende des Simulationszeitraums kollabiert, während er im Szenario mit sozialen Regeln langfristig nahezu auf dem maximalen Bestandsniveau erhalten bleibt. Die Ergebnisse legen nahe, dass nicht räumliche Nähe allein, sondern deren Einfluss auf das Verhalten der Akteur*innen entscheidend für die nachhaltige Nutzung gemeinsam genutzter Ressourcen ist. Die Aussagekraft des Modells wird jedoch durch seine bewusste Vereinfachung begrenzt, insbesondere durch die Modellierung eines einzigen globalen Fischbestands sowie die Reduktion sozialer Interaktionen auf eine einfache Verhaltensanpassungsregel.

## 1. Introduction
Die Aufgabenstellung unserer Gruppenarbeit ist schnell erklärt: Ein See, mehrere Fischer*innen am See und Fische im See. Der See soll als Gitter von Fisch-Patches dargestellt werden – jeder Patch mit logistischem Wachstum und Diffusion in die Nachbarzellen. Die Fischer*innen nutzen den See – je nach Verhaltensregeln bzw. -mix (naive Gewinnmaximierung, Imitation des erfolgreichsten Nachbarn, konditionale Kooperation oder Sanktionierung von Übernutzern) zeigt sich, ob der Bestand kollabiert, welche räumlichen Übernutzungsmuster entstehen und ob sich kooperative Normen selbst tragen. 

Das Thema „Fischerei und Allmende“, das der Aufgabenstellung zugrunde liegt, ist deutlich komplexer, als ein erster Blick vermuten lässt. Um zu verstehen, muss man sich die dahinter liegenden Theorie ansehen. Im speziellen geht es um mehrere Werke, die eine direkte theoretische und historische Entwicklungslinie in der Erforschung der Allemendegüter bilden. Ein kurzer Überblick zeigt die Unterschiede und Zusammenhänge und wie sie einander bedingen: 
·	Im Essay „The Tragedy of the Commons“, der von Garrett Hardin 1968 veröffentlicht wurde formuliert er darin das Grundproblem einer gemeinsam genutzten Ressource als ihr unausweichliches Schicksal: Da die Menschen rational und nutzenmaximierend handeln, führt dies letztendlich zur Zerstörung der Ressource. Jene die sie nutzen, streichen den Ertrag ein und die Allgemeinheit trägt die Folgen. 
·	„Governing the Commons“, die 1990 von Elinor Olstroms veröffentlichte Arbeit, lässt sich als wissenschaftliche Antwort auf Hardins Aussagen sehen: Sie widerlegte Hardins Theorie und zeigte auf Basis ihrer empirischen Feldstudien, dass reale Gemeinschaften den Kollaps oft vermeiden, indem sie nachhaltige Regeln für die Nutzung einer Ressource aufstellen – ganz ohne staatlichen Zwang oder Privatisierung, wie Hardin als Lösung schlussfolgerte. Ostrom identifizierte acht Design-Prinzipien für erfolgreiche Selbstverwaltung, wie klar definierte Grenzen, die Möglichkeit der Nutzer*innen, Regeln selbst mitzugestalten, funktionierende Überwachungssysteme durch die Nutzer*innen selbst und definierte Sanktionen bei Regelverstößen. 
·	Mit „Introducing ecological dynamics into common-pool resource experiments” baute Marco Janssen 2010 auf Ostroms Werk auf, und schloss gleichzeitig eine methodische Forschungslücke: Während in „Governing the Commons“ der Fokus sehr stark auf dem menschlichen Verhalten lag und die Ressource selbst oft stark vereinfacht dargestellt wurde, entwickelte Janssen Computerexperimente – meist in Form von interaktiven Spielen – bei denen es die Probanden nicht mehr mit einem statischen Konstrukt, sondern einer sich dynamisch verändernden Ökologie als Ressource zu tun hatten. Bei Janssen ging es konzeptionell um ein sozio-ökologisches System. Er testete sozusagen unter „Realbedingungen“, wo genau die Grenzen von Ostroms Design-Prinzipien liegen, wenn die Natur als aktiver, sehr komplexer und teils unberechenbarer Gegenspieler auftritt.  

Wie gingen wir vor? In der ersten Annäherung stellten wir uns der komplexen Herausforderung und versuchten aus allen drei Ansätzen Parameter zu formulieren und in unser Konzept mitaufzunehmen. Folgende Fragestellungen leiteten uns u.a. an: Wie entwickelt sich der See vertikal (Fischer*innen-Fische-Beziehung) und horizontal (Die Fischer*innen bewegen sich auf der Oberfläche, was zu Isolation und Begegnung führt, aus denen sich Regeln ableiten. Die Fische bewegen sich unterhalb der Oberfläche, schließen sich zu Schwärmen zusammen, vermehren sich.)? Wie sanktioniert die Gruppe das gewinnmaximierende bzw. kooperative Fischverhalten Einzelner (Einführung von Regeln für Bestrafung und Bestärkung von Verhalten)? Es wurde immer vielschichtiger und faszinierender aber auch undurchschaubarer in Richtung der Wechselwirkungen und möglicher Schrittfolgen. Im zur Verfügung stehenden Zeitkorsett schwer machbar. Und so reduzierten wir den Ansatz und beschränkten uns auf eine Kombination aus Hardin und Ostrom, indem wir uns auf die „Tragik der Allmende“ fokussierten, die wir anhand einer Regel zu widerlegen versuchten.

Wir konzentrierten uns ab da auf folgende Forschungsfrage: Wie wirkt sich Nähe bzw. Isolation auf das Fisch-Verhalten der Fischer*innen und letztendlich auf die Stabilität der gemeinsam genutzten Ressource aus? 

Zweck des Modells ist es zu veranschaulichen, wie echte Nähe das soziale Verhalten befördert und dadurch das Verhalten des Einzelnen zu Gunsten der Gemeinschaft verändert, während nur Nähe, ohne Wahrnehmung und Interaktion, exakt gleich wie die Isolation der Fischer*innen wirkt – sie werden immer egoistischer. Ein leicht dystopischer Blick auf unsere Welt, die Gefahr läuft, soziale Prozesse zu verlernen. 

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
Nach dem Fischfang regeneriert sich der Bestand.
Der entsprechende Mechanismus sieht im Code wie folgt aus.
```python
def regenerate_fish(self):
    self.fish_stock += self.fish_stock * regen_rate

    if self.fish_stock > max_fish:
        self.fish_stock = max_fish
```
Technisch handelt es sich um einen Wachstumsprozess mit einer Wachstumsrate von 3,66 % pro Zeitschritt. Gleichzeitig begrenzt die maximale Kapazität das Wachstum nach oben. Die Modellannahme besteht darin, dass sich der Bestand umso schneller erholt, je größer der verbleibende Bestand ist. Dieser Mechanismus wirkt dem Fischfang entgegen und bestimmt gemeinsam mit dem Verhalten der Fischer*innen die langfristige Systemdynamik.

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

Zur Untersuchung der Forschungsfrage wurden zwei Szenarien mit identischen Ausgangsbedingungen simuliert. Der einzige Unterschied bestand in der Verhaltensanpassung der Fischer*innen.

### Szenario ohne Regeln
Im Szenario ohne Regeln entwickelt sich das Verhalten aller Fischer*innen schrittweise in Richtung maximaler Egoismus. Da der Verhaltenswert in jedem Zeitschritt ansteigt und schließlich die Obergrenze von 9 erreicht, nimmt auch die gesamte Fangmenge kontinuierlich zu.
Die Folge ist ein rascher Rückgang des Fischbestands. Der gemeinsame Bestand wird bereits deutlich vor dem Ende der 200 Zeitschritte vollständig erschöpft und erreicht den Wert 0. Der Kollaps tritt somit bereits vor dem Ende der 200 Simulationsschritte ein.
Im Endzustand der Visualisierung sind ausschließlich rote Agenten sichtbar, welches verdeutlicht, dass sich alle Fischer*innen zu maximal egoistischem Verhalten entwickelt haben. 

Das Ergebnis entspricht den Erwartungen der „Tragedy of the Commons“ nach Hardin, wonach individuelle Nutzenmaximierung langfristig zur Übernutzung gemeinsamer Ressourcen führt.
Wichtig ist jedoch die Interpretation des Endbildes. Der Programmcode enthält kein Abbruchkriterium bei leerem Fischbestand. Nachdem der Bestand bereits auf 0 gefallen ist, bewegen sich die Fischer*innen weiterhin über das Raster und passen ihr Verhalten weiterhin an. Sichtbare Endpositionen zeigen daher nicht den Zeitpunkt des eigentlichen Ressourcenkollapses, sondern lediglich den Zustand nach Abschluss der gesamten Simulationsdauer.

### Szenario mit Regeln
Im Szenario mit Regeln führt soziale Nähe zu einer Reduktion egoistischen Verhaltens. Begegnungen innerhalb der Moore-Nachbarschaft bewirkt eine stärkere Rücksichtnahme, hingegen Isolation egoistisches Verhalten begünstigt.
Dadurch entsteht ein dynamisches Gleichgewicht verschiedener Verhaltensweisen. Kooperative, mittlere und egoistische Strategien existieren parallel nebeneinander. Der Bestand schwankt nur geringfügig um die maximale Kapazität und zeigt keine langfrisitge Abwärtstendenz. Dies ist auch in der Endvisualisierung sichtbar, in der grüne, gelbe und rote Agenten gemeinsam auftreten.

Der Fischbestand bleibt während der gesamten Simulation nahezu auf maximalem Niveau. Nach 200 Zeitschritten betrug der Bestand in einem Durchlauf noch 4970 Fische und lag damit praktisch auf Höhe der maximalen Kapazität von 5000 Fischen. Die Ressource bleibt langfristig stabil und zeigt keinen Hinweis auf einen drohenden Kollaps.

### Vergleich der Szenarien
Der Vergleich der beiden Szenarien verdeutlicht den Unterschied zwischen räumlicher Nähe und sozial wirksamer Interaktion. In beiden Simulationen bewegen sich die Fischer*innen nach identischen Bewegungsregeln über das Raster und weisen somit vergleichbare Begegnungswahrscheinlichkeiten auf. Dennoch entwickeln sich die Systeme aufgrund der unterschiedlichen Verhaltensanpassung grundlegend verschieden.

Im Szenario ohne soziale Regeln führt die kontinuierliche Zunahme egoistischen Verhaltens zu einer steigenden Entnahme von Fischen und schließlich zum vollständigen Zusammenbruch der Ressource. Im Szenario mit sozialen Regeln wirken Begegnungen hingegen verhaltensmodifizierend, indem sie egoistische Tendenzen reduzieren und dadurch den Entnahmedruck auf den Fischbestand begrenzen. Dies ermöglicht die langfristige Stabilisierung der Ressource.

Die Ergebnisse legen somit nahe, dass nicht die räumliche Nähe allein, sondern deren Einfluss auf das Verhalten der Akteur*innen entscheidend für die nachhaltige Nutzung gemeinsam genutzter Ressourcen ist.


## 4. Discussion, Conclusion and Limitations

### Was unser Modell zeigt. 
Auf Grundlage unserer Forschungsfrage (Wie wirkt sich Nähe bzw. Isolation auf das Fisch-Verhalten der Fischer*innen und letztendlich auf die Stabilität der gemeinsam genutzten Ressource aus?) lassen sich folgende Ergebnisse formulieren: Unsere beiden Simulationen zeigen zwar exakt dieselben Bewegungsmuster, führen aber trotzdem zu diametral unterschiedlichen Entwicklungen, was das Verhalten der Fischer*innen am und in weiterer Folge die Stabilität des Fischbestands im See angeht. Die erste Simulation führt trotz Nähe/Begegnung schnell zum Kippen der Ressource, während die zweite sich durch Nähe/Begegnung immer wieder stabilisiert. 

### Warum? 
Uns ging es hier nicht nur um den Wert von Begegnung als Verstärker für soziales Verhalten, sondern auch darum, das dieser Wert nicht perse als solcher verstanden werden kann, ohne ihn als solchen zu pflegen und zu erhalten. Solange eine Begegnung auch damit zu tun hat, sich wahrzunehmen und zu interagieren - im Besten Falle sogar als ein in-Beziehung-treten verstanden werden kann - wird ein soziales Gefüge davon profitieren. Sobald diese Komponenten aber alle wegfallen und man sich trotz der vorhanden örtlichen Nähe isoliert und für sich bleibt, entfällt die Wirkung, was im Vergleich der Simulationen sehr schnell ersichtlich wird. 

### Was unser Modell nicht zeigt. 
Ein Schwachpunkt ist die extreme Vereinfachung. Das menschliche Verhalten ist sehr vielschichtig und komplex. Kaum etwas lässt sich auf Basis einer einfach-formulierbaren Ursache-Wirkungs-Beziehung beschreiben bzw. erklären. In unserem Modell arbeiten wir mit genau einem Parameter. Und gerade darin zeigt sich auch die starke Limitation der Aussagekraf und die bewusst gewählte Eingrenzung des Modells.

Um es realistischer zu machen, müssten wir unsere starken Vereinfachungen zumindest teilweise wieder zurücknehmen und eine Reihe weiterer Parameter aufnehmen. Außerdem bräuchte es eine eingehendere Betrachtung der Wechselwirkungen und Rückkoppelungen in positiver wie negativer Richtung.  


## References


## Appendix A: ODD


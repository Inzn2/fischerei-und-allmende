# Fischerei und Allmende 

## Abstract
Diese Arbeit untersucht den Einfluss sozialer Nähe und Isolation auf das Verhalten von Akteuren*innen sowie auf die Stabilität einer gemeinsam genutzten Ressource. Hierzu wurde ein agentenbasiertes Modell entwickelt, in dem 30 Fischer*innen auf einem zweidimensionalen Raster agieren und auf einen gemeinsamen Fischbestand zugreifen. Ausgehend von theoretischen Überlegungen zu Allmendegütern werden zwei Szenarien verglichen: ein Szenario ohne soziale Regeln sowie ein Szenario, in dem lokale Begegnungen kooperatives Verhalten fördern. Die Ergebnisse zeigen deutliche Unterschiede zwischen beiden Bedingungen. Während im Szenario ohne Regeln egoistisches Verhalten kontinuierlich zunimmt und der Fischbestand innerhalb des Simulationszeitraums kollabiert, bleibt die Ressource im Szenario mit sozialen Regeln langfristig stabil und nahe ihrer maximalen Kapazität. Die Simulation verdeutlicht damit die Bedeutung sozialer Interaktionen für die nachhaltige Nutzung gemeinsamer Ressourcen. Die Aussagekraft der Ergebnisse wird jedoch durch die bewusste Vereinfachung des Modells begrenzt, insbesondere durch die Modellierung eines einzigen globalen Fischbestands sowie die Reduktion sozialer Prozesse auf eine einfache Verhaltensanpassungsregel.

## 1. Introduction
Die Nutzung gemeinsam genutzter Ressourcen zählt zu den klassischen Fragestellungen der Sozial- und Umweltwissenschaften. Besonders relevant ist dabei die Frage, unter welchen Bedingungen Individuen bereit sind, ihre eigenen Interessen zugunsten des langfristigen Erhalts einer Ressource einzuschränken. Fischbestände, Weideflächen oder Bewässerungssysteme stellen typische Beispiele solcher Allmendegüter (Common-Pool Resources) dar.

Einen wichtigen Beitrag zur theoretischen Diskussion lieferte Garrett Hardin (1968) mit seinem einflussreichen Essay 
„The Tragedy of the Commons“. Hardin argumentiert, dass Individuen bei freiem Zugang zu einer gemeinsamen Ressource dazu neigen, ihren persönlichen Nutzen zu maximieren. Da die negativen Folgen der Übernutzung von allen Beteiligten getragen werden, führt dieses Verhalten langfristig zur Erschöpfung der Ressource.

Dieser Sichtweise widersprach Elinor Ostrom (1990) auf Grundlage umfangreicher empirischer Untersuchungen. Sie zeigte, dass Gemeinschaften durchaus in der Lage sind, gemeinsame Ressourcen dauerhaft zu bewirtschaften, wenn geeignete Regeln, Kontrollmechanismen und soziale Normen etabliert werden. Ostrom identifizierte mehrere Gestaltungsprinzipien erfolgreicher Selbstverwaltung, darunter klar definierte Nutzungsrechte, gemeinschaftliche Regelsetzung und soziale Kontrolle innerhalb der Nutzergruppe.

Aufbauend auf diesen Arbeiten betonte Janssen (2010) die Bedeutung dynamischer Wechselwirkungen zwischen menschlichem Verhalten und ökologischen Prozessen. Seine Untersuchungen verdeutlichen, dass nachhaltige Ressourcennutzung nicht allein von institutionellen Regeln abhängt, sondern auch von den Rückkopplungen zwischen sozialem und ökologischem System.

Vor diesem theoretischen Hintergrund untersucht die vorliegende Arbeit einen spezifischen Aspekt gemeinschaftlicher Ressourcennutzung: die Bedeutung sozialer Nähe und sozialer Isolation. Während viele Modelle institutionelle Regeln oder Sanktionen in den Mittelpunkt stellen, konzentriert sich das hier entwickelte Modell auf die Frage, ob bereits lokale soziale Begegnungen das Verhalten von Akteur*innen beeinflussen können.

Daraus ergibt sich folgende Forschungsfrage:

Wie wirken sich soziale Nähe beziehungsweise Isolation auf das Verhalten von Fischer*innen und damit auf die Stabilität einer gemeinsam genutzten Ressource aus?

Zur Beantwortung dieser Frage wurde ein agentenbasiertes Simulationsmodell entwickelt, in dem Fischer*innen auf einem Raster agieren und einen gemeinsamen Fischbestand nutzen. Verglichen werden zwei Szenarien: eines ohne soziale Einflussnahme und eines, in dem Begegnungen zwischen benachbarten Fischer*innen kooperatives Verhalten fördern. Ziel des Modells ist es nicht, reale Fischereisysteme vollständig abzubilden, sondern die grundlegende Bedeutung sozialer Interaktionen für die nachhaltige Nutzung gemeinsamer Ressourcen sichtbar zu machen.

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
Interpretation Verhaltenswert:
1 … stark kooperativ
2-3 … kooperativ
4-6 … mittleres Verhalten
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
Die Ergebnisse der Simulation liefern eine klare Antwort auf die Forschungsfrage. Obwohl sich die Fischer*innen in beiden Szenarien unter identischen räumlichen Bedingungen bewegen, entstehen grundlegend unterschiedliche Entwicklungen. Im Szenario ohne soziale Regeln nimmt egoistisches Verhalten kontinuierlich zu, wodurch der „Entnahmedruck“ auf den Fischbestand steigt und die Ressource schließlich kollabiert. Im Szenario mit sozialen Regeln wirken Begegnungen zwischen Fischer*innen hingegen verhaltensmodifizierend. Soziale Nähe fördert kooperatives Verhalten und reduziert den Druck auf den gemeinsamen Fischbestand, sodass der Kollaps der Ressource deutlich verzögert wird.

Die Ergebnisse stehen damit im Einklang mit theoretischen Überlegungen der Allmendeforschung. Das Szenario ohne Regeln entspricht der von Hardin beschriebenen „The Tragedy of the Commons“, bei der individuelle Nutzenmaximierung zur Übernutzung gemeinsamer Ressourcen führt. Das Szenario mit Regeln zeigt dagegen, dass selbst einfache soziale Mechanismen ausreichen können, um kooperatives Verhalten zu stabilisieren und die nachhaltige Nutzung einer Ressource zu ermöglichen. Die Simulation unterstützt somit die grundlegende Annahme Ostroms, dass soziale Interaktionen und gemeinschaftliche Regeln einen wesentlichen Beitrag zur Stabilität gemeinsamer Ressourcen leisten können.

Die zusätzlichen Langzeitsimulationen zeigen zudem, dass die im Modell implementierte soziale Regel zwar eine deutliche Stabilisierung des Systems bewirkt, jedoch keine vollständige Nachhaltigkeit garantiert. Während der Fischbestand über mehr als 200 Zeitschritte hinweg nahezu auf seinem Ausgangsniveau verbleibt, tritt bei einer Verlängerung der Simulation auf 300 Zeitschritte schließlich ebenfalls ein Zusammenbruch der Ressource auf. Die Ergebnisse deuten daher darauf hin, dass soziale Nähe und Verhaltensanpassung allein nicht ausreichen, um eine gemeinsame REssource dauerhaft zu sichern. Sie können jedoch die Geschwindigkeit der Übernutzung erheblich reduzieren und die Lebensdauer des Systems deutlich verlängern. 

Gleichzeitig verdeutlichen die Ergebnisse, dass räumliche Nähe allein nicht ausreichend ist. Entscheidend ist, ob aus dieser Nähe tatsächlich soziale Wahrnehmung und Verhaltensanpassung entstehen. Im Modell entfalten Begegnungen nur dann eine stabilisierende Wirkung, wenn sie mit einer Veränderung des individuellen Verhaltens verbunden sind. Die nachhaltige Nutzung der Ressource ist somit nicht das Ergebnis der räumlichen Struktur selbst, sondern der sozialen Prozesse, die innerhalb dieser Struktur stattfinden.

Die Aussagekraft des Modells wird jedoch durch mehrere Vereinfachungen begrenzt. Erstens existiert lediglich ein globaler Fischbestand, auf den alle Fischer*innen gleichermaßen zugreifen. Räumliche Unterschiede im Ressourcenangebot werden nicht berücksichtigt. Zweitens wird menschliches Verhalten ausschließlich über einen eindimensionalen Verhaltenswert beschrieben. Reale Entscheidungen werden dagegen von zahlreichen sozialen, ökonomischen und kulturellen Faktoren beeinflusst. Drittens basiert die Verhaltensanpassung auf einer einzigen Regel, die soziale Begegnungen unmittelbar mit kooperativem Verhalten verknüpft. Komplexere Mechanismen wie Lernen, Kommunikation, Sanktionen oder strategische Anpassungen bleiben unberücksichtigt.

Für zukünftige Erweiterungen könnten räumlich verteilte Fischbestände, unterschiedliche Agententypen, soziale Netzwerke oder explizite Sanktionsmechanismen integriert werden. Dadurch ließe sich die Komplexität realer Allmendesituationen genauer abbilden und die Robustheit der Ergebnisse überprüfen.

Zusammenfassend zeigt das Modell, dass soziale Interaktionen einen entscheidenden Einfluss auf die langfristige Stabilität gemeinsam genutzter Ressourcen haben können. Trotz seiner Vereinfachungen verdeutlicht es anschaulich, wie bereits einfache Formen sozialer Einflussnahme den Übergang von Übernutzung zu nachhaltiger Ressourcennutzung ermöglichen.



## References
Hardin, G. (1968). The Tragedy of the Commons: Science 162, 1243-1248.

Ostrom, E. (1990); Governing the Commons: The evolution of institutions for collective action. Cambridge University Press.

Janssen, M.A., Holahan, R., Lee, A., & Ostrom, E. (2010). Lab experiments for the study of social-ecological systems. Science, 328(5978), 613-617.


## Appendix A

# ODD - Protokoll Fischerei und Allmende

## 1. Purpose and Patterns
Was modellieren wir und warum?

Das Modell soll veranschaulichen, unter welchen Bedingungen eine gemeinsam genutzte Ressource, wie ein See mit einem bestimmten Fischbestand, stabil bleibt oder kippt. Konkret geht es uns um das Verhalten der Fischer, das mehr oder weniger gravierende Auswirkungen auf den Fischbestand zeigt. Welche Parameter haben eine hohe Sensitivität für die Stabilität des Fischbestands? 
Wir erwarten: Je indivividueller das Nutzungsverhalten der Fischer (Gewinnmaximierung des Einzelnen) ist, umso früher kollabiert der Bestand. Je mehr soziales Verhalten, umso stabiler bleibt das System. Soziale Nähe fördert kooperatives Verhalten, während Isolation egoistisches Verhalten begünstigt.

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
- Anzahl der Fischer am See (30)
- Postion der Fischer (Patch)
- Verhalten der Fischer (von 1/kooperativ bis 9/ego => Faktor bestimmt den Fischfang: 1 bis 9 Fische pro Zeitschritt)
- Nähe/Distanz zu anderen Fischern (beeinflusst das Verhalten)
Auf Saktionierung/Bestrafung bzw. Belohnung wird im Modell verzichtet. 

Fische
- Anzahl im See (Patch für Fischbestand nicht wichtig.)
- Maximale Kapazität im See (5000)
- Minimumbestand (0)
- Regenerationsrate (3,66% pro Zeitschritt bis zur Maximalgrenze)

Patches (See als Gitter dargestellt. Räumliches Raster für Position der Fischer*innen)
- Anzahl Patches (20x20)
- Koordinaten der Patches (Wird benötigt für Position der Fischer*innen und die Grenzen des Sees)
Max. Kapazität an Fischen pro Patch nicht wichtig.
Diffusion zwischen Patches wird nicht betrachtet.

- Simulationsdauer: Die Simulation läuft standardmäßig über 200 Zeitschritte. 

## 3. Prozess Overview and Scheduling (Zeitplan)
Was tun die Entitäten in welcher Reihenfolge?

Pro Zeitschritt passiert folgendes:
Schritt 1: Fischer*innen fischen (auf Basis der hinterlegten Verhaltensregel je Fischer*in) und darauf aufbauend wird der neue Fischbestand im See gespeichert.
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

Treffen Fischerìnnen auf mindestens eine Person in ihrer Moore-Nachbarschaft, wird ihr Verhaltenswert um 1 reduziert (kooperativer). Bei Isolation erhöht sich der Verhaltenswert um 1 (egoistischer) 
Isolation führt zum Schrittweisen Abbau von sozialem hin zu egoistischem Verhalten.

# 4.4 Objectives
Was optimieren die Agenten?

Jeder Fischer verfolgt primär das Ziel, Fische zu fangen - die Menge steuert seine hinterlegte Verhaltensregel. Isolation führt zur Gewinnmaximierung. Nähe optimiert das Verhalten in Bezug soziale Angleichung um Verhaltenswert -1. 

# 4.5 Learning
Ändern Agenten ihre Entscheidungsregeln über die Zeit?

Die Agenten ändern ihr Verhalten auf Basis von Nähe und Distanz. 
Isolation: Sie lernen von sich selbst (Je egoistischer, umso mehr Ertrag)
Nähe (Fischer*innen treffen sich in benachbarten Feldern): Sie lernen von/orientieren sich an benachbarten Fischer*innen

# 4.5 Prediction
Wie antizipieren Agenten zukünftige Zustände?
-

# 4.6 Sensing
Was können Agenten über ihre Umgebung und andere Agenten wahrnehmen? Über welche Distanz?

Die Wahrnehmung ist lokal auf benachbarte Zellen (Moore-Nachbarschaft) beschränkt. Wenn sie sich auf unmittelbaren Nachbarfeldern begegnen, nehmen sie das Fischverhalten des/der anderen wahr. Treffen Fischerìnnen auf mindestens einen anderen Fischer*in in ihrer Moore-Nachbarschaft, wird ihr Verhaltenswert um 1 reduziert (kooperativer).

# 4.7 Interaction
Wie beeinflussen sich Agenten gegenseitig?

Über Nähe/Distanz: Treffen Fischerìnnen auf mindestens eine Person in ihrer Moore-Nachbarschaft, wird ihr Verhaltenswert um 1 reduziert (kooperativer).

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

Der See wird als 20x20 Gitter initialisiert (x,y-Koordinatensystem)

Der See:
- Maximale Kapazität, max_capacity_lake= 5000
- Minimale Kapazität (Kipppunkt), min_capacity_lake= 0
- Regenerationsrate Fischbestand, regen_rate=0,366 (3,66%) bis max_capacity

Fische im See: 
- Anfangsbestand, fish_stock=5000

Fischer:
- Anzahl der Fischer am See: fisherman=50
- Postion der Fischer (Patch): position_f= (x,y-Koordinaten), zufallsverteilt (von 0-1, 0 bedeutet alle starten isoliert, 1 bedeutet alle starten als Gruppe in direkter Moore-Nachbarschaft)
- Alle Fischer*innen starten mit Verhalten = 1 
- Verhalten der Fischer: behavefactor_gr= 1
behavefactor_f1=... (von 1/kooperativ bis 9/ego. Der Faktor bestimmt den Fischfang: bei behavefactor_f=1 wird 1 Fisch pro Zeitschritt gefangen / bei behavefactor_f=9 werden 9 Fische pro Zeitschritt gefangen / gleiches Prinzip für 2-8)

Random Seed wird gesetzt.

## 6. Input Data
Welche externen Daten fließen ein?

Externe, zeitabhängige Daten sind im Basismodell nicht erforderlich.

## 7. Submodels
Wie funktioniert jeder Prozess im Detail?

Schritt 1: Fischer fischen.
Am Beginn jedes Zeitschritts fischen die Fischer*innen auf Basis der jeweils hinterlegten Verhaltensregel je Fischer*in.
fishing_f1 = ...
Neuer Fischbestand im See wird gespeichert: fish_stock = fish_stock - fishing_f1 - ...
Kipppunkt-Abgleich: Wenn fish_stock < min_capacity_lake, dann bricht die Animation ab = Spielstopp

Schritt 2: Die Verhaltensregel bei den Fischern wird adaptiert. 
Hat ein Fischer keinen anderen Fischer auf einem Nachbarpatch: 
behavefactor_f = behavefactor + 1 (er wird egoistischer). Bis max. 9 möglich.

Treffen Fischer*ìnnen auf mindestens einen Nachbarn in ihrer Moore-Nachbarschaft, wird ihr Verhaltenswert um 1 reduziert (kooperativer).

Schritt 3: Fischer wechseln den Patch: 
Ein Patch weiter. Maximal 8 Nachbarfelder zur Auswahl (außer an den Rändern des Sees). Zufallsgeneriert


Schritt 4: Fische regeneriern sich.
Am Ende jedes Zeitschritts regeneriert sich der Fischbestand um den Regenerationsfaktor 0,366 bis maximal zur Kapazitätsgrenze (max 5000):
fish_stock = fish_stock + fish_stock*regen_rate
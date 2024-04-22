# LeistungsApp_Matti_Samuel
## Anwendung
Dieser Code generiert ein von Matplotlib erstelltes Diagramm welches eine Power-Curve dargestellt. Es kann eine Liste von unsortierten Messwerten in die Applikation gegeben werden und sie erhalten eine sortierte ABbildung ihres Leistungstets.
## Setup
- Laden sie sich das Repository in die gewünschte Programierumgebung
- Öffnen sie die Conole und legen sie hier ein Virtuelles Enviorment an mit: ```python -m venv .venv```
- Virtuelles Enviorment aktivieren: ```.\.venv\Scripts\activate``` (Windows) oder source ```.venv/bin/activate``` (Linux/Mac)
    - falls es hierbei zu einem ungewünschten Fehler kommt führen ```Set-ExecutionPolicy Unrestricted -Scope Process``` aus und aktivieren sie nochmal das Venv
- Installieren sie alle benötigten packages mit ```pip install -r requirements.txt```
- Laden sie nun ihre eigenen Daten in die Applikation hier wurde als Beispiel mit ```activity.csv``` als Datensatz gearbeitet
- Führen sie einmal ```load_data.py``` und ```sort.py``` aus um die hier codierten Funktionen zu aktivieren
- Final können sie jetzt die ```main.py```` ausführen 
## Anmerkungen zur Applikation
  - Ihre Daten werden hier mithilfe des Bubble Sort Algorithmus sortiert, wenn hier ein anderer Sortieralgorithmus gewünscht ist können sie diesen in dem File ```sort.py``` anpassen.
  - Numpy wird im Code als ```np``` und matplotlib.pyplot als ```plt``` genutzt

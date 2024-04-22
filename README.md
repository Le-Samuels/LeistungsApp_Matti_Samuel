# LeistungsApp_Matti_Samuel
## Anwendung
Dieser Code generiert ein von Matplotlib erstelltes Diagramm welches eine Power-Curve dargestellt. Es kann eine Liste von unsortierten Messwerten in die Applikation.
## Setup
- Laden sie sich das Repository in die gewünschte Programierumgebung
- Öffnen sie die Conole und legen sie hier ein Virtuelles Enviorment an mit: ```python -m venv .venv```
- Virtuelles Enviorment aktivieren: ```.\.venv\Scripts\activate```
    - falls es hierbei zu einem ungewünschten Fehler kommt führen ```Set-ExecutionPolicy Unrestricted -Scope Process``` aus und aktivieren sie nochmal das Venv
- Installieren sie alle benötigten packages mit ```pip install -r requirements.txt```
- Laden sie nun ihre eigenen Daten in die Applikation hier wurde als Beispiel mit ```activity.csv``` als Datensatz gearbeitet
- Führen sie nun ```python main.py``` aus
## Anmerkungen zur Applikation
  - Ihre Daten werden hier mithilfe des Bubble Sort Algorithmus sortiert, wenn hier ein anderer Sortieralgorithmus gewünscht ist können sie diesen in dem File ```sort.py``` anpassen.

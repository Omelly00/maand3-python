# Week 12 - Flask API koppelen aan frontend

## Doel

In deze week heb ik geleerd hoe ik een Flask-backend kan koppelen aan een frontend met HTML, CSS en JavaScript.

## Wat heb ik gebouwd?

Een kleine trainingen-webapp. De frontend haalt data op uit de backend via API endpoints. De backend stuurt JSON responses terug.

## Gebruikte technieken

- Python
- Flask
- HTML
- CSS
- JavaScript
- JSON
- Fetch API

## API endpoints

| Endpoint | Beschrijving |
|---|---|
| `/` | Toont de webpagina |
| `/api/trainingen` | Geeft alle trainingen terug als JSON |
| `/api/totaal` | Geeft de totale kosten terug als JSON |
| `/api/aantal` | Geeft het aantal trainingen terug als JSON |

## Wat heb ik geleerd?

- Hoe een backend werkt met Flask
- Hoe ik data terugstuur als JSON
- Hoe ik met JavaScript data ophaal via `fetch()`
- Hoe ik API-data toon op een webpagina
- Hoe frontend en backend samenwerken

## Starten

Installeer Flask:

```bash
pip3 install flask

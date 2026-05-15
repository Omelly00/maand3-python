const knop = document.getElementById("laadTrainingenBtn");
const trainingenLijst = document.getElementById("trainingenLijst");
const totaalKosten = document.getElementById("totaalKosten");
const aantalTrainingen = document.getElementById("aantalTrainingen");

knop.addEventListener("click", function () {
    laadTrainingen();
    laadTotaal();
    laadAantal();
});

knop.addEventListener("click", function () {
    laadTrainingen();
    laadTotaal();
});

function laadTrainingen() {
    fetch("/api/trainingen")
        .then(response => response.json())
        .then(data => {
            trainingenLijst.innerHTML = "";

            data.forEach(training => {
                const kaart = document.createElement("div");
                kaart.classList.add("training-card");

                kaart.innerHTML = `
                    <h3>${training.naam}</h3>
                    <p>Prijs per maand: €${training.prijs}</p>
                    <p>Aantal maanden: ${training.maanden}</p>
                    <p>Subtotaal: €${training.prijs * training.maanden}</p>
                `;

                trainingenLijst.appendChild(kaart);
            });
        });
}

function laadTotaal() {
    fetch("/api/totaal")
        .then(response => response.json())
        .then(data => {
            totaalKosten.textContent = `Totale kosten: €${data.totaal}`;
        });
}

function laadAantal() {
    fetch("/api/aantal")
        .then(response => response.json())
        .then(data => {
            aantalTrainingen.textContent = `Aantal trainingen: ${data.aantal}`;
        });
}

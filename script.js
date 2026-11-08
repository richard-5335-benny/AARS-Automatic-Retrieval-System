const search = document.getElementById("itemSearch");

if (search) {

    search.addEventListener("input", function () {

        const query = this.value.toLowerCase();

        const cards = document.querySelectorAll(".item-card");

        cards.forEach(card => {

            const text = card.innerText.toLowerCase();

            card.style.display =
                text.includes(query)
                    ? "flex"
                    : "none";

        });

    });

}


function changeQuantity(amount) {

    const input = document.getElementById("quantity");

    if (!input) return;

    let value = parseInt(input.value);

    value += amount;

    if (value < 1) value = 1;

    if (value > 20) value = 20;

    input.value = value;

}
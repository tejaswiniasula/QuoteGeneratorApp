const API_URL = "http://127.0.0.1:8000";

const button = document.getElementById("generate");

button.addEventListener("click", async () => {

    try {

        const response = await fetch(API_URL + "/quote");

        const data = await response.json();

        document.getElementById("quote").innerText =
            `"${data.quote}"`;

        document.getElementById("author").innerText =
            "- " + data.author;

        loadHistory();

    }

    catch (error) {

        alert("Backend not running!");

        console.log(error);

    }

});

async function loadHistory() {

    const response = await fetch(API_URL + "/history");

    const history = await response.json();

    const list = document.getElementById("historyList");

    list.innerHTML = "";

    history.reverse().forEach(item => {

        list.innerHTML += `

        <li>

        "${item.quote}"

        <br>

        <b>- ${item.author}</b>

        </li>

        `;

    });

}

loadHistory();
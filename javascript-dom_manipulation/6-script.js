fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then(response => response.json())
  .then(data => {
    console.log(data.name);
    const char = document.querySelector("#character");
    char.textContent = data.name
  })
  .catch(error => console.error("Erreur :", error));

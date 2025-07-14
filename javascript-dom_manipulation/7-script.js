fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json())
  .then(data => {
    const list = document.querySelector("#list_movies");
    data.results.forEach(film => {
      const new_li = document.createElement("li");
      new_li.textContent = film.title;
      list.appendChild(new_li);
    })
  })
  .catch(error => console.error("Erreur :", error));

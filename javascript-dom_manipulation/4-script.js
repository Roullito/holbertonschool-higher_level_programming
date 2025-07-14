const item = document.querySelector("#add_item");
const ul = document.querySelector(".my_list")

item.addEventListener("click", () => {
    const new_li = document.createElement("li");
    new_li.textContent = "Item";
    ul.appendChild(new_li);
})

const btn = document.querySelector("#theme");
const addBtn = document.querySelector("#add");
const body = document.body;
btn.addEventListener("click", () => {
    body.classList.toggle("dark");
    body.classList.toggle("light");
    
});
addBtn.addEventListener("click", () => {
    const card = document.createElement("div");
    card.classList.add("card"); 
    card.innerHTML = `<h2>another card</h2>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facere eius veritatis dicta at necessitatibus omnis voluptas sint. Molestias ad magni architecto. Nihil nisi rem ad dolorum eveniet saepe vero aut?</p>`;
    body.appendChild(card);
});
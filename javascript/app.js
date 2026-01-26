const btn = document.querySelector("button")
const log = document.getElementById("log")
btn.addEventListener("click", (e)=>{
    e.preventDefault()
    log.innerHTML += "hello"
})
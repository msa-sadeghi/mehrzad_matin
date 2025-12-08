const h1Elem = document.querySelector('#first')
const btn = document.querySelector("button")
const div = document.querySelector("div")
btn.onclick = function(){
    let items = ["apple", "sumsung",  "lg", "lenovo"]
    let html = ''
    items.forEach((n, i) => {
        html += `<div class="red">${i+1}-${n}</div>`
    })
    div.innerHTML = html
}



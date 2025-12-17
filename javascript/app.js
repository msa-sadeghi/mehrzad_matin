const todoInput = document.getElementById("todoInput")
const todoList = document.getElementById("todoList")

let allTodoItems = []
let idG
window.onload = ()=>{
    allTodoItems = localStorage.getItem('todos')
    if(allTodoItems === null){
        allTodoItems = []
    }
    else{
        allTodoItems = JSON.parse(allTodoItems)
        
    }
   idG  = IDGenerator()
   renderList()
}


function IDGenerator(){
    let id = allTodoItems.length
    return function(){
        id++
        return id
    }
}



function Item(name){
    this.name = name
    this.id = idG()
}


function addTodo(){
    let inputValue = todoInput.value.trim()
    let newItem =new Item(inputValue)
    allTodoItems.push(newItem)
    localStorage.setItem('todos', JSON.stringify(allTodoItems))  
    renderList()
}

function renderList(){
    todoList.innerHTML = ''
    allTodoItems.forEach((item)=>{
    let newDiv = document.createElement('div')
    newDiv.classList.add('todo-item')
    let span = document.createElement("span")
    span.textContent = item.name
    let i = document.createElement("i")
    i.className = "fa-solid fa-trash-can"
    i.setAttribute("id", item.id)
    i.addEventListener('click', (e)=>{
        allTodoItems = allTodoItems.filter((i) => i.id !== item.id)
        renderList()
    })
    newDiv.append(span, i)
    todoList.append(newDiv)
    todoInput.value = ''

    })
}




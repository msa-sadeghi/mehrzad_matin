const todoInput = document.getElementById("todoInput")
const todoList = document.getElementById("todoList")

function IDGenerator(){
    let id = 0
    return function(){
        id++
        return id
    }
}

let idG = IDGenerator()

function Item(name){
    this.name = name
    this.id = idG()
}

let  allTodoItems = []

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
       
    })
    newDiv.append(span, i)
    todoList.append(newDiv)
    })
}


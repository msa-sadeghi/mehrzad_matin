import { useState } from "react"
import TodoList from "./components/TodoList"
import TodoForm from "./components/TodoForm"
import FilterButtons from "./components/FilterButtons"
import './assets/css/style.css'
function App(){
    const [todos, setTodos] = useState(()=>{
        const saved = localStorage.getItem("todos")
        return saved ? JSON.parse(saved) : []
    })
    const [filter, setFilter] = useState('All')

    const filteredTodos = todos.filter(t => {
        if(filter === 'Active') return !t.completed
        if(filter === 'Completed') return t.completed
        return true
    })

    const deleteTodo = (id)=>{
        const newTodos = todos.filter(t=>t.id !== id)
        setTodos(newTodos)
        localStorage.setItem('todos', JSON.stringify(newTodos))
    }
    const toggleTodo = (id)=>{
        const newTodos = todos.map(
        t=>t.id === id ? {...t, completed: !t.completed} : t)
        setTodos(newTodos)    
        localStorage.setItem('todos', JSON.stringify(newTodos))
    }
    const addTodo = (text)=>{
        const  newTodo = {
            id:Date.now(),
            text:text
        }
        const newTodos = [...todos, newTodo]
        setTodos(newTodos)
        localStorage.setItem("todos",  JSON.stringify(newTodos))
    }
    return(
        <div style={{ width:"400px", margin:"50px auto"}}>
            <h1>Todo App</h1>
            <TodoForm 
            addTodo={addTodo}
            />
            <FilterButtons setFilter={setFilter}/>
            <TodoList
            todos={filteredTodos}
            toggleTodo={toggleTodo}
            deleteTodo={deleteTodo}
            />
        </div>
    )
}

export default App
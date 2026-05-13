import { useState } from "react"
import TodoList from "./components/TodoList"
import TodoForm from "./components/TodoForm"

function App(){
    const [todos, setTodos] = useState([
        {
        id:1,
        text:'todo #1'
            },
        {
        id:2,
        text:'todo #2'
            },
])
    const deleteTodo = (id)=>{

    }
    const toggleTodo = (id)=>{

    }
    const addTodo = (text)=>{

    }
    return(
        <div style={{ width:"400px", margin:"50px auto"}}>
            <h1>Todo App</h1>
            <TodoForm 
            addTodo={addTodo}
            />
            <TodoList
            todos={todos}
            toggleTodo={toggleTodo}
            deleteTodo={deleteTodo}
            />
        </div>
    )
}

export default App
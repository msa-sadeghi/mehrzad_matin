import { useState } from "react"

function TodoForm({addTodo}){
    const [text, setText] = useState("")
    const handleChange = (e)=>{
        setText(e.target.value)
    }
    const handleSubmit=(e)=>{
    }
    return(
        <form onSubmit={handleSubmit}>
            <input 
            placeholder="Net todo..."
            value={text}
            onChange={handleChange}
            type="text" />
            <button type="submit">Add</button>
        </form>
    )
}

export default TodoForm
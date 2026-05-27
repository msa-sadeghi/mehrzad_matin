function TodoItem({ todo, deleteTodo, toggleTodo}){
    
    return(
        <div style={{
            display:'flex',
            gap:'10px',
            marginTop:'10px'
        }}>
            <input 
            
            type="checkbox" name="" id="" checked={todo.completed}
            onChange={()=>toggleTodo(todo.id)}
            />
            
            <span style={{
               color: todo.completed ? 'blue' : 'black'
            }}
                
            >
                {todo.text}
            </span>
            <button onClick={()=>deleteTodo(todo.id)}>Delete</button>
        </div>
    )
}

export default TodoItem
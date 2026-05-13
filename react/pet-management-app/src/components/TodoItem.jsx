function TodoItem({ todo, deleteTodo, toggleTodo}){
    return(
        <div style={{
            display:'flex',
            gap:'10px',
            marginTop:'10px'
        }}>
            <input 
            
            type="checkbox" name="" id="" />
            
            <span
                
            >
                {todo.text}
            </span>
            <button>Delete</button>
        </div>
    )
}

export default TodoItem
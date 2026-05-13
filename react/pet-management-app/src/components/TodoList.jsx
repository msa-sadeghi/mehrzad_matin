import TodoItem from "./TodoItem"

function TodoList({todos, deleteTodo, toggleTodo}){
    return(
        <div>
            {
                todos.map((t) => (
                    <TodoItem
                        key={t.id}
                        todo={t}
                        deleteTodo={deleteTodo}
                        toggleTodo={toggleTodo}
                    />
                ))
            }
        </div>
    )
}

export default TodoList
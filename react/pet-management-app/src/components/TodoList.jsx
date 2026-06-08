import TodoItem from "./TodoItem";

function TodoList({ todos, deleteTodo, toggleTodo, saveTodo }) {
  return (
    <div>
      {todos.map((t) => (
        <TodoItem
          key={t.id}
          todo={t}
          deleteTodo={deleteTodo}
          toggleTodo={toggleTodo}
          saveTodo={saveTodo}
        />
      ))}
    </div>
  );
}

export default TodoList;

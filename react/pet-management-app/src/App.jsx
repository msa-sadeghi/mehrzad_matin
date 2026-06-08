import { useEffect, useState } from "react";
import "./assets/css/style.css";
import FilterButtons from "./components/FilterButtons";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";
function App() {
  const [todos, setTodos] = useState(() => {
    const saved = localStorage.getItem("todos");
    return saved ? JSON.parse(saved) : [];
  });
  const [filter, setFilter] = useState("All");

  const filteredTodos = todos.filter((t) => {
    if (filter === "Active") return !t.completed;
    if (filter === "Completed") return t.completed;
    return true;
  });
  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);
  const deleteTodo = (id) => {
    setTodos(todos.filter((t) => t.id !== id));
  };
  const toggleTodo = (id) => {
    setTodos(
      todos.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t)),
    );
  };
  const addTodo = (text) => {
    const newTodo = {
      id: Date.now(),
      text: text,
    };
    setTodos([...todos, newTodo]);
  };

  const saveTodo = (id, newText) => {
    setTodos((prev) =>
      prev.map((t) => (t.id === id ? { ...t, text: newText } : t)),
    );
  };

  return (
    <div style={{ width: "400px", margin: "50px auto" }}>
      <h1>Todo App</h1>
      <TodoForm addTodo={addTodo} />
      <FilterButtons setFilter={setFilter} />
      <TodoList
        todos={filteredTodos}
        toggleTodo={toggleTodo}
        deleteTodo={deleteTodo}
        saveTodo={saveTodo}
      />
    </div>
  );
}

export default App;

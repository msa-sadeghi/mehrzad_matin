import { useState } from "react";
function UserForm() {
  const [inputValue, setInputValue] = useState("");
  const [todos, setTodos] = useState([
    { id: 1, title: "task # 1", completed: false },
    { id: 2, title: "task # 2", completed: false },
    { id: 3, title: "task # 3", completed: false },
    { id: 4, title: "task # 4", completed: false },
    { id: 5, title: "task # 5", completed: false },
  ]);
  const handleAdd = () => {
    const t = {
      id: Date.now(),
      title: inputValue,
      completed: false,
    };
    setTodos([...todos, t]);
  };
  const handleRemove = (id) => {
    setTodos(todos.filter((t) => t.id !== id));
  };

  const handleToggle = (id) => {
    setTodos(
      todos.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t)),
    );
  };
  return (
    <>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      <button onClick={handleAdd}>Add</button>
      {todos.map((t) => (
        <div>
          <span style={{ textDecoration: t.completed ? "line-through":"" }} key={t.id}>
            {t.title}
          </span>
          <button onClick={() => handleRemove(t.id)}>remove</button>
          <button>update</button>
          <button onClick={() => handleToggle(t.id)}>toggle</button>
        </div>
      ))}
    </>
  );
}

export default UserForm;

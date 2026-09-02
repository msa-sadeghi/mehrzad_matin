import { useState } from "react";

function UserForm() {
  const [todos, setTodos] = useState([
    { id: 1, title: "task # 1", completed: false },
    { id: 2, title: "task # 2", completed: false },
    { id: 3, title: "task # 3", completed: false },
    { id: 4, title: "task # 4", completed: false },
    { id: 5, title: "task # 5", completed: false },
  ]);
  return (
    <>
      <input type="text" />
      <button>Add</button>
      {todos.map((t) => (
        <div>
          <span key={t.id}>{t.title}</span>
          <button>remove</button>
          <button>update</button>
          <button>toggle</button>
        </div>
      ))}
    </>
  );
}

export default UserForm;

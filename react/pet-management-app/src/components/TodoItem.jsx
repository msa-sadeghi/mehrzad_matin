import { useState } from "react";

function TodoItem({ todo, deleteTodo, toggleTodo, saveTodo }) {
  const [isEditing, setIsEditing] = useState(false);
  const [text, setText] = useState(todo.text);

  const handleClick = (e) => {
    saveTodo(todo.id, text);
    setIsEditing(false);
  };

  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        marginTop: "10px",
      }}
    >
      <input
        type="checkbox"
        name=""
        id=""
        checked={todo.completed}
        onChange={() => toggleTodo(todo.id)}
      />

      {isEditing ? (
        <div>
          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button onClick={handleClick}>save</button>
          <button onClick={() => setIsEditing(false)}>cancel</button>
        </div>
      ) : (
        <>
          <span style={{ color: todo.completed ? "blue" : "black" }}>
            {todo.text}
          </span>
          <button onClick={() => setIsEditing(true)}>Edit</button>
        </>
      )}
      <button onClick={() => deleteTodo(todo.id)}>Delete</button>
    </div>
  );
}

export default TodoItem;

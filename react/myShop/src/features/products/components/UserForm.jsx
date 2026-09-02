import { useState } from "react";

function UserForm() {
  const [user, setUser] = useState({ name: "", age: 0 });

  function handleNameChange(event) {
    user.name = event.target.value; 
    setUser(user);
  }

  return <input value={user.name} onChange={handleNameChange} />;
}

export default UserForm;

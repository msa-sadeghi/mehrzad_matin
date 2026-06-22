export default function Test() {
  const users = [
    {
      name: "sara",
      age: 34,
      n_c: "025000000",
      gender: "male",
    },
    {
      name: "sara",
      age: 34,
      n_c: "025000000",
      gender: "male",
    },
  ];
  return <div>
    {users.map(u=>(<ul>
      <li>{u.name}</li>
      <li>{u.age}</li>
    </ul>))}
  </div>;
}

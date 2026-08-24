export default function ProductList() {
  return (
    <div>
      <ul>
        {ProductList.map((p) => (
          <li>{p.name}</li>
        ))}
      </ul>
    </div>
  );
}

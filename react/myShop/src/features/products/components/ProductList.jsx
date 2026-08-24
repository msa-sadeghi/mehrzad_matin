export default function ProductList({ products, handleRemove }) {
  return (
    <div>
      <ul>
        {products.map((p) => (
          <li key={p.id}>
            {p.name}
            <button onClick={() => handleRemove(p.id)}>delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function SearchForm() {
  function handleSubmit(event) {
    event.preventDefault(); // جلوگیری از رفرش شدن صفحه
    console.log("فرم ارسال شد");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" />
      <button type="submit">جستجو</button>
    </form>
  );
}

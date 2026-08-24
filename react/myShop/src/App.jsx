import "./assets/css/style.css";
import ProductList from "./features/products/components/ProductList";
function App() {
  const fruits = [
    { id: 1, name: "apple", price: 234 },
    { id: 2, name: "bana", price: 456 },
    { id: 3, name: "orange", price: 4556 },
  ];
  return (
    <>
      <ProductList />
    </>
  );
}

export default App;

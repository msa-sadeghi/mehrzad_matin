import { useState } from "react";
import "./assets/css/style.css";
import ProductList, {
  SearchForm,
} from "./features/products/components/ProductList";
function App() {
  const [fruits, setFruits] = useState([
    { id: 1, name: "apple", price: 234 },
    { id: 2, name: "bana", price: 456 },
    { id: 3, name: "orange", price: 4556 },
  ]);
  const handleRemove = (id) => {
    console.log("clicked");
    const newFruits = fruits.filter((p) => p.id !== id);
    setFruits(newFruits);
  };
  return (
    <>
      <SearchForm />
      <ProductList products={fruits} handleRemove={handleRemove} />
    </>
  );
}

export default App;

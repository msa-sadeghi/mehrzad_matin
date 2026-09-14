import { useEffect, useState } from "react";
import getAllProducts from "./Data";
import Product from "./Product";
export default function Products() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    async function getData() {
      const data = await getAllProducts();
      setProducts(data);
    }
    getData();
  }, []);
  return (
    <div>
      {products.map((p) => (
        <Product
          name={p.name}
          description={p.description}
          price={p.price}
          inStock={p.inStock}
          image={p.image}
        />
      ))}
    </div>
  );
}

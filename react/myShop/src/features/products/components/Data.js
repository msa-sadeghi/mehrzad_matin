export default async function getAllProducts() {
  try {
    const response = await fetch("http://127.0.0.1:5000/products");
    if (response.ok) {
      const data = await response.json();
      return data.items;
    }
  } catch (ex) {
    console.log(ex);
    return [];
  }
}

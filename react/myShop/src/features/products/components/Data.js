export default function getData() {
  try {
    const response = fetch("https://dummyjson.com/products");
    console.log(response);
  } catch (ex) {
    console.log(ex);
  }
}

getData();

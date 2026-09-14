export default function Product({ name, description, price, image, inStock }) {
  return (
    <div className="card">
      <h2>{name}</h2>
      <img src={image} alt={name} />
      <p>{description}</p>
      <p>price : {price} </p>
      <input type="checkbox" name="" id="" checked={inStock} />
    </div>
  );
}

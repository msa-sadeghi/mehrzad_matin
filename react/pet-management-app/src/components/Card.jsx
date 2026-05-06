function Card({name,  price, details, category}){
    return(
        <div className="card">
            <h2>{name}</h2>
            <h3>Price: {price}</h3>
            <h4>Details: {details}</h4>
            <h4>category: {category}</h4>
            {/* <img src="" alt="" /> */}
            <button>Add</button>
        </div>
    )
}

export default Card
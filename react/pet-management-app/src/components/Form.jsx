import { useState } from "react"

function Form({addItem}){

    const [product, setProduct] = useState(
        {name:"", price:"", details:"", category:""}
    )

    const handleSubmit = (e)=>{
        e.preventDefault()
        addItem(product)
    }

    const handleChange =(e)=>{
        setProduct({...product, [e.target.name]: e.target.value})
    }
    return(
        <form onSubmit={handleSubmit}>
            
            <input type="text" placeholder="name..."
            onChange={handleChange}
             name="name" />
            <input type="number" 
            onChange={handleChange}
            name="price" id="" placeholder="price" />
            <textarea name="details"
            onChange={handleChange}
            id=""></textarea>
            <button type="submit">Add</button>
        </form>
    )
}

export default Form
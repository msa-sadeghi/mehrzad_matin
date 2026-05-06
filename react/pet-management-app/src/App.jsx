import Card from "./components/Card"
import "./assets/css/Card.css"
import { useState } from "react"
import Form from "./components/Form"
function App(){
    const [items, setItems] = useState([
        {id : 1, name: "laptop asus", price:"1000" , details:"asus pro", category:"electronic" },
        {id : 2, name: "IPHone 17", price:"2000" , details:"Iphone pro", category:"electronic" },
        {id : 3, name: "IPHone 16", price:"1000" , details:"Iphone pro", category:"electronic" },
    ])
    const addItem = (product)=>{
        setItems(prev => [...prev, product])
    }
    return(
        <div>
            <Form addItem={addItem}/>
            {items.map(pr => (
                <Card name={pr.name} price ={pr.price} details={pr.details} category={pr.category}/>
            ))}
        </div>
    )
}

export default App
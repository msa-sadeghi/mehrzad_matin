import './Pet.css'
const PetCard = () => {
    const pet = {
        name:'leno',
        breed : 'German',
        age:3
    }
    const {name, breed, age} = pet
    const colors = ["brown", "black", "white"]
    const [firstColor, secondColor, thirdColor] = colors
    return (<div>
                <h1 style={{color:thirdColor}}>اطلاعات حیوان</h1>
                <p className='red'>{name}</p>
                <p>{breed}</p>
                <p className='green'>{age.toLocaleString('fa-ir')}</p>
            </div>
            )
}
export default PetCard
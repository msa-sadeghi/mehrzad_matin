fetch("https://jsonplaceholder.typicode.com/users")
.then(response => response.json())
.then(data => {
    setTimeout(()=>{
    displayUsers(data)
        },2000)
})
.catch(error=>console.log(error))

let container = document.getElementById("container")
let loadingElement = document.getElementById("loading")
function displayLoading(flag){
  
    loadingElement.style.display = flag ? 'block' : 'none'
}

function displayUsers(users){
    displayLoading(true)
        users.forEach(element => {
        const userDiv = document.createElement("div")
        userDiv.innerText = element.name

        container.append(userDiv)
    });
    
    displayLoading(false)
}
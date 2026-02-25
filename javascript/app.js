const loginForm = document.getElementById("loginForm")
const message = document.getElementById("message")

loginForm.addEventListener('submit', async (e) =>{
    e.preventDefault()
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value
    try{
        const response = await fetch('http://127.0.0.1:5000/login',{
            method:'POST',
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({username, password})
        })
        const data = await response.json()
        if(data.status === 200 ){
            message.classList.remove('error')
            message.classList.add('success')
            message.textContent = "success"
        }else{
            message.classList.remove('success')
            message.classList.add('error')
            message.textContent = "not valid user"

        }
    }
    catch(error){
        console.log(error)
    }

})



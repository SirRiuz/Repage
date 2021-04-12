

/* 
    Este archivo contiene la las funciones que 
    se van a encargar de hacer todo el proceso de 
    autenticacion con la API
*/


function onAuthError (authTypeErrror) {
    switch(authTypeErrror) {
        case 'user-not-found':
            alert('El usuario es incorrecta')
            break

        case 'password-error':
            alert('Contraseña incorrecta')
            break
    }
}


function onAuth(nick,password) {
    var data = new FormData()

    data.append('nickName',nick)
    data.append('password',password)

    fetch(config["api-url"]+'/v1/auth/',{
        method:'POST',
        body:new URLSearchParams(data)
    })
    .then(response => response.json())
    .then(response => {
        if (response.status == "ok"){
            localStorage.setItem('token',response.data.token)
            window.location = '/home/'
        } else {
            onAuthError(response['type-error'])
        }
    })
    .catch(error => {
        console.log('Error')
    })
}



function onSubmit(){
    const formData = document.getElementById('form-auth')
    const buttomElement = document.getElementById('btn-sub')

    buttomElement.addEventListener('click',(e)=>{
        e.preventDefault()
        var nickName = formData[0].value
        var password = formData[1].value
        
        onAuth(nickName,password)
    })
}


if (localStorage.getItem('token') != null){ window.location = '/home/' }

onSubmit()






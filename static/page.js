
function onCreatePage(pageName) {

    var params = new FormData()
    params.append('pageName',pageName)

    fetch('http://api.localhost:8000/v1/page/',{
        method:'POST',
        headers:{'Authorization':'Token ' + localStorage.getItem('token')},
        body:new URLSearchParams(params)
    })

    .then(response => response.json())
    .then(response => {
        console.log(response)
        if(response.status == "ok") {
            window.location = '/home/'
        } else {
            var element = document.getElementById('error-messege')
            console.log(response['type-error'])
            element.innerHTML = `<div class="notification is-danger is-light">
            <button class="delete"></button>
            No a sido posible crear esta pagina con este nombre ya que hay otra pagina con el mismo nombre
          </div>`
        }
    })

    .catch(err => {
        console.log(err)
    })
    .catch(err => {
        console.log('Server error')
    })

}


function onSubmit(){
    const formData = document.getElementById('form-page-creator')
    const buttomElement = document.getElementById('btn-sub')

    buttomElement.addEventListener('click',(e)=>{
        e.preventDefault()
        onCreatePage(formData[0].value)
    })
}


onSubmit()
if(localStorage.getItem('token') ==null ) { window.location = '/auth/' }

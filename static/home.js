
function onCloseSesion(){
    const buttonClose = document.getElementById('close')
    buttonClose.addEventListener('click',() => {
        localStorage.removeItem('token')
        window.location = '/home/'
    })
}


function onGetPages() {
    console.log('Token ' + localStorage.getItem('token'))
    fetch(config["api-url"]+'/v1/page/',{
        headers:{
            'Authorization':'Token ' + localStorage.getItem('token')
        }
    })
    .then(response => response.json())
    .then(response => {
        console.log(response)
        if(response.status == "ok") {
            var el = document.getElementById('pages-list')
            var pages = ''
            response.pages.map((item) => {
                console.log(item)
                pages += `
                <div class='card'>
                    <div class='content'>
                        <a href='/page/${item.name}/'>${item.name}</a>
                    </div>
                </div>`
            })
            el.innerHTML = pages
        }
    })

    .catch(error=> {
        console.log('Error')
    })
    .catch(error => {
        console.log('Server error')
    })
}



onCloseSesion()
onGetPages()


if(localStorage.getItem('token') ==null ) { window.location = '/auth/' }


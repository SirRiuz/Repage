
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
                <div class="col-md-6 col-xs-10">
                    <div class="box card">
                    <a id="title-txt" href='/page/${item.name}/'>${item.name}</a>
                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s</p>                    </div>
                </div>
                `
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


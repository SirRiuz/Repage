

var rootElenet = document.getElementById('root')


function getPageName(){
    var path = window.location.pathname.split('/')
    path = path[2]
    return path
}

function onShowFileContend(data){
    const container = document.getElementById('aplication-file-container')
    container.innerHTML = `
        <div class='line-indicator' id="line-indicator">
            <p>1</p>
            <p>1</p>
            <p>1</p>
        </div>
        <textarea class="editor-text" id="editor-text">
            ${data.contend}
        </textarea>
    `
    document.getElementById('editor-text').addEventListener('input',(e) => {
        var listItem = document.getElementById('line-indicator')
        var lines = e.target.value.split('\n').length
        listItem.innerHTML += `<p>${lines}</p>`
    })
}




function desambleRecItem() {
    var el = document.getElementsByClassName('a-reg')
    console.log(el)
}



function onCreateFile(type){

    /*
      Esta funcion es la encargada de la creacion de 
      archivos
    */
   
    var type_ = 'file'

    if(type != undefined) {
        type_ = type
    }

    const buttom = document.getElementById('create-file-btn')
    const formElement = document.getElementById('create-file-modal')
    const form = document.getElementById('file-form')
    var data = new FormData()
    data.append('type',type_)
    
    buttom.addEventListener('click',() => {
        formElement.style.display = 'block'
        form.addEventListener('submit',(e)=>{
            e.preventDefault()
            const fileName = form[0].value
            data.append('name',fileName)
            var url = `${config["api-url"]}/v1/file/?page=${getPageName()}`

            fetch(url,{
                method:'POST',
                body:new URLSearchParams(data)
            })

            .then(res => res.json())
            .then(res => {
                if(res.status == "ok") {
                    formElement.style.display = 'none'
                    onGetFiles()
                }
            })

        })

    })
}


function onShowThreadFiles(data){
    const container = document.getElementById('aplication-file-container')
    var dataHtml = ''
    var path = ''

    if (window.location.search.split('=')[1] != undefined) {
        path = window.location.search.split('=')[1]
    }
    data.map((item) => {

        var icon = "src='/static/filder.svg'"
        if (!item.isDir) {
            icon = "src='/static/file.svg'"
        }

        console.log(item.type)

        switch(item.type){
            case 'text/css':
                icon = "src='/static/css-3.svg'"
                break

            case 'text/html':
                icon = "src='/static/html5.svg'"
                break

            case 'application/json':
                icon = "src='/static/json.svg'"
                break

            case 'application/javascript':
                icon = "src='/static/js.svg'"
                break

            case 'application/pdf':
                icon = "src='/static/pdf.svg'"
                break

            case 'image/jpeg':
                icon = "src='/static/jpg.svg'"
                break
        }

        dataHtml += `
        <div class='aplication-file-item row item-file'>
            <div class="col-md-0">
                <div class="box"><img ${icon} class='vector-img'/></div>
            </div>
            <div class="col-md-11 col-xs-11" id='item-contemt'>
                <div class="box item-container">
                    <a class='a-reg' href='?p=${path}/${item.name}'>${item.name}</a>
                    <br/>
                    <a  class='a-reg' id="subtitle" >${item.nameType}</a> 
                </div>
            </div>
        </div>`
    })
    container.innerHTML = dataHtml
    var el = document.getElementsByClassName('item-file')

    for(var x=0;x<el.length; x++){

        el[x].children[1].addEventListener('contextmenu',(e) => {
            e.preventDefault();
            const element = document.getElementById('menu-op-popup')

            element.style.top = `${e.pageY}px`
            element.style.left = `${e.pageX }px`
            element.style.display = 'block'

            window.addEventListener('scroll',(e) => { element.style.display = 'none' })
            window.addEventListener('click',(e) => { element.style.display = 'none' })
            //console.log(element,e.target.children)
            menuConteoller(element,e.target.children)
        })

        el[x].children[1].children[0].addEventListener('click',(e) => {
            history.pushState(null,"",e.target.children[0].href)
            onGetFiles()
        })
    }
}

function onGetFiles(){
    const container = document.getElementById('aplication-file-container')
    var path = window.location.search.split('=')[1]
    var dinamicPath = path
    if(path == undefined){ path='' }
    var url = `${config["api-url"]}/v1/file/${path}?page=${getPageName()}`

    container.innerHTML = 'LOAD ...'

    console.log(dinamicPath)
    
    fetch(url)
    .then(response => response.json())
    .then(response => {
        if(response.status == "ok"){
            console.log(response)
            if (response.thread != undefined) {
                onShowThreadFiles(response.thread)
            } 
            else {onShowFileContend(response.data) }
        } else {
            const container = document.getElementById('aplication-file-container')
            container.innerHTML = 'Imposible leer este archo'
        }
    })

    .catch(err => {
        console.log(err)
    }) 
    .catch(err => {
        console.log('Server err0r')
    }) 

}



function onGetData() {
    fetch(config["api-url"]+'/v1/page/'+getPageName()+'/',{
        headers:{'Authorization':'Token ' + localStorage.getItem('token')}
    })
    .then(respnse => respnse.json())
    .then(response => {
        document.title = response.data.name + ' | Repage'
        if(!response.isOwner){
            window.location = `http://${response.data.name}.${config["host-name"]}`
        }
        onGetFiles()
        onCreateFile()
        desambleRecItem()
    })

    .catch(err => {
        console.log(err)
    })
    .catch(err => {
        console.log(err)
    })
}


document.title = 'Cargando ...'


if(localStorage.getItem('token') ==null ) { window.location = '/auth/' }

onGetData()


window.onpopstate = function(event) { onGetFiles() }







const el = document.getElementById('upload-form-file')



function onUploadFiles(files){

    var params = new FormData()
    var path = window.location.search.split('?')
    
    for(var x=0; x<=files.length; x++) {
        params.append(`file${x}`,files[x])
    }

    params.append('page',getPageName())
    params.append('path',path)

    fetch(config["api-url"]+'v1/upload/',{
        method:'POST',
        body:params,
        headers:{
            'Authorization':'Token '+localStorage.getItem('token')
        }
    })

    .then(res => res.json())
    .then(res => {
        const modal = document.getElementById('modal-upload-file')
        if(res.status == "ok") {
            modal.style.display = 'none'
            onGetFiles()
        }
    })


    .catch(err => {
        console.log(err)
    })

    .catch(err => {
        alert('Server error')
    })

}


el.addEventListener('submit',(e) => {
    e.preventDefault()
    onUploadFiles(e.target[0].files)
})
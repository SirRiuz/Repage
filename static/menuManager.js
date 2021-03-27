


function menuConteoller(menuObject,context){
    const el = menuObject

    console.log(el)
    el.children[0].addEventListener('click',(e) => {
        history.pushState(null,"",context[0].href)
        onGetFiles()
    })



}



function renameFile(){
    alert('Rename !!')
}







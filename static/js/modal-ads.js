

const el = document.getElementById('modal-container')


function addChildrens (el) {
    el.innerHTML = `
        <div id="screem"></div>
        <div id="modal"></div>
    `
}

function onCanselable(el) {
    el.children[0].addEventListener('click',(e) => {
        el.style.display = 'none'
        document.getElementsByTagName("html")[0].style.overflow = "visible";

    })
}


setTimeout(() => {
    //alert('Ads')
    addChildrens(el)
    onCanselable(el)
    el.style.display = 'block'
    document.getElementsByTagName("html")[0].style.overflow = "hidden";
    window.scrollTo(0, 0);
    
},2050)
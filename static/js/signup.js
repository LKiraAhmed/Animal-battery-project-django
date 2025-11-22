const submitdata = document.querySelector(".submit-btn")
const name =  document.querySelector("#name")
const loader = document.querySelector('.loader')
const password =  document.querySelector("#password")
const tr_co = document.querySelector("#terms-and-cond")
form = document.querySelector("form")

let handleSubmit = async(e) => {
    e.preventDefault()
}    

submitdata.addEventListener('click',() => {
    if(password.value.length < 8){
        showAlert('password must be mor than 8')
        form.addEventListener('submit',handleSubmit)
    }else if(name.value.length <= 3){
        showAlert('name must be mor than 3')
        form.addEventListener('submit',handleSubmit)
    }else if(!tr_co.checked){
        showAlert('you must agree first')
        form.addEventListener('submit',handleSubmit)
    }else{
        loader.style.display = 'block'
    }
})

const showAlert = (msg) => {
    let alertBox  =document.querySelector(".alert-box")
    let alertMsg = document.querySelector(".alert-msg")
    alertMsg.innerHTML = msg
    alertBox.classList.add('show')
    setTimeout(()=>{
        alertBox.classList.remove('show')
        location.reload()
    },3000)
}

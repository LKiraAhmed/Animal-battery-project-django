let loader = document.querySelector('.loader')

const becameSellerEle =  document.querySelector('.became-seller')
const applyForm = document.querySelector('.apply-form')
const ShowApply  = document.querySelector('#apply-btn')

window.onload = () => {
    loader.style.display = 'block';
    setTimeout(()=>{
        becameSellerEle.classList.remove('hide')
        loader.style.display = 'none'
    },800)
}

ShowApply.addEventListener('click' , () => {
    becameSellerEle.classList.add('hide')
    loader.style.display = 'block';
    setTimeout(()=>{
        applyForm.classList.remove('hide')
        loader.style.display = 'none'
    },800)
})


// for submission data

const applyFormBtn = document.querySelector('#apply-form-btn')
const BusinessName = document.querySelector('#business-name')
const address = document.querySelector('#business-add')
const about = document.querySelector('#about')
const phone = document.querySelector('#phone')
const tac = document.querySelector('#terms-and-cond')
const legitInfo = document.querySelector('#legitInfo')
const form = document.querySelector("form")



let handleSubmit = async(e) => {
    e.preventDefault()
}   

applyFormBtn.addEventListener('click' , () => {
    if(!BusinessName.value.length ||!address.value.length ||
        !about.value.length ||!phone.value.length ){
            showAlert('fill out the form please')
            form.addEventListener('submit',handleSubmit)
        }
    else if (!tac.checked || !legitInfo.checked){
        showAlert('please check the boxes')
        form.addEventListener('submit',handleSubmit)
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
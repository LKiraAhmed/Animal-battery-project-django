// loader the page
let loader = document.querySelector('.loader')
let bodyy = document.querySelector('form')
bodyy.style.display = 'none';
window.onload = () => {
    loader.style.display = 'block';
    setTimeout(() =>{
        loader.style.display = 'none';
        bodyy.style.display = 'block';
    },1500)
}

// handle submiting dATA
const form = document.querySelector('form')

let handleSubmit = async(e) => {
    e.preventDefault()
}    


// pirce discount
const actualprice = document.querySelector('#actual-price')
const discountprecentage = document.querySelector('#discount-price')
const sellingprice = document.querySelector('#sell-price')

discountprecentage.addEventListener('input' , () => {
    if(discountprecentage.value > 100){
        discountprecentage.value= 95
    }else{
        let discount = actualprice.value * discountprecentage.value / 100;
        sellingprice.value = actualprice.value - discount
    }
})
sellingprice.addEventListener('input',() => {
    let discount = (sellingprice.value / actualprice.value) * 100
    discountprecentage.value = discount
})

// upload image 
const uploadedText =  document.querySelectorAll('.uploaded')
const uploadedImg = document.querySelectorAll('.upload-image')
let uploadImg= document.querySelectorAll('.fileupload')

uploadImg.forEach((fileupload,index) => {
    fileupload.addEventListener('click',() =>{
        uploadedText[index].style.display = 'block'
        uploadedImg[index].classList.add('img-uploaded')
    })
})

const proName= document.querySelector('#product-name')
const shortDes = document.querySelector('#short-des')
const description = document.querySelector('#des')
const tac = document.querySelector('#terms-and-cond')
const stock = document.querySelector('#stock')
const tags = document.querySelector('#tags')
const addBtn = document.querySelector('#add-btn')


const validForm = () => {
    if(!proName.value ||!shortDes.value ||
        !description.value ||!actualprice.value ||
        !discountprecentage.value ||!sellingprice.value ||
        !tac.checked ||!stock.value ||
        (tags.value == '0') ){
            form.addEventListener('submit',handleSubmit)
            showAlert("please fill out the form")
        }
}

addBtn.addEventListener('click',() => {
    if(validForm()){
        //well show the validate date or not 
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

const csrftoken_elmt = document.querySelector('[name=csrfmiddlewaretoken]'); 


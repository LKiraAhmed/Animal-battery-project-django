const productImg = document.querySelectorAll(".product-imgs img")
const imgSlider = document.querySelector(".image-slider img")

let activeImg = 0;

productImg.forEach((item , i) => {
    item.addEventListener('click',() => {
        productImg[activeImg].classList.remove('active')
        item.classList.add('active')
        imgSlider.src = item.src
        activeImg = i
    })
})
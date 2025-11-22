
const createnav = () => {
    let nav = document.querySelector('.navbar')
    nav.innerHTML = `
    {%load static%}
    <div class="logo">
            <a href=".html"><img src="{% static 'img/Picture1.png'%}" alt="" class="logo-img"></a>
            <div class="nav-item">
                <div class="search">
                    <input type="text" placeholder="search pet name or food or products" class="search-box">
                    <input type="button" value="search" class="search-btn">
                </div>
            
                <a class="a">
                <img src="img/user.png" id="user-img" alt="">
                <div class="login-logout-pop hide">
                    <p class="account-info">Log in as, name</p>
                    <button type="logout" class="btn" id="user-btn">Log out</button>
                </div>
                </a>

                <!--
                <div class="login-logout-pop hide">
                    <p class="account-info">Log in to place order</p>
                    <button type="login" class="btn" id="user-btn">Log in</button>
                </div>
                -->
                

                <a href="card.html" class="a"><img src="img/cart.png" alt=""></a>
            </div>
        </div>
        <ul class="links-container">
            <li class="links-item"><a href="index.html" class="link">Home</a></li>
            <li class="links-item"><a href="product.html" class="link">Dog</a></li>
            <li class="links-item"><a href="product.html" class="link">Cat</a></li>
            <li class="links-item"><a href="add-product.html" class="link">add Product</a></li>
            <li class="links-item"><a href="seller.html" class="link">Seller</a></li>
        </ul>
    `
}
const createFoot = () => {
    let nav = document.querySelector('.foot')
    nav.innerHTML = `
    <div class="footer-content">
            <img src="img/Picture1.png" alt="" class="foot-logo">
            <div class="footer-ul-category">
                <ul class="category">
                    <li class="category-title">Cat</li>
                    <li><a href="#" class="footerlink">Cats</a></li>
                    <li><a href="#" class="footerlink">Food</a></li>
                    <li><a href="#" class="footerlink">Cages</a></li>
                    <li><a href="#" class="footerlink">vitmens</a></li>
                    <li><a href="#" class="footerlink">clothes</a></li>
                    <li><a href="#" class="footerlink">accessories</a></li>
                </ul>
                <ul class="category">
                    <li class="category-title">Dog</li>
                    <li><a href="#" class="footerlink">Dogs</a></li>
                    <li><a href="#" class="footerlink">Food</a></li>
                    <li><a href="#" class="footerlink">Cages</a></li>
                    <li><a href="#" class="footerlink">vitmens</a></li>
                    <li><a href="#" class="footerlink">clothes</a></li>
                    <li><a href="#" class="footerlink">accessories</a></li>
                </ul>
            </div>
        </div>
        <p class="footer-title">about our team</p>
        <p class="info">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem quibusdam o
            fficia neque aliquid laudantium voluptate dolores, nostrum commodi soluta quae minima 
            itaque inventore fuga, impedit incidunt, quis eum nihil enim.</p>
        <p class="info">support Email:hazem12@gmail.com</p>
        <p class="info">tel :12589545521</p>
        <div class="footer-social-conatiner">
			<div>
				<a href="#" class="social-link">term & services</a>
				<a href="#" class="social-link">privacy page</a>
			</div>
			<div>
				<a href="#" class="social-link">facebook</a>
				<a href="#" class="social-link">Twitter</a>
				<a href="#" class="social-link">instgram</a>
			</div>
		</div>
        <p class="footer-credit">best online pet shop in egypt </p>
    `
}

// createnav()
// createFoot()

//create popup
const usrimgbtn = document.querySelector('#user-img')
const usrpop = document.querySelector('.login-logout-pop')
const poptxt = document.querySelector('.account-info')
const actionbtn = document.querySelector('#user-btn')

usrimgbtn.addEventListener('click', () => {
    usrpop.classList.toggle('hide')
})

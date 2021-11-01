function myFunction() {
  var nav = document.getElementById("toggle-collapse");
  if (nav.className === "nav") {
    nav.className += " collapse";
  } else {
    nav.className = "nav";
  }
}

const createNav = () => {
  const navbar = document.querySelector(".nav");
  navbar.innerHTML = ` <div class="nav-menu flex-row">
            <div class="nav-brand">
                <a href="/" class="text-gray">CampusConnect</a>
                
            </div>
            <div class="toggle-collapse"  >
                <div class="toggle-icons">
                  
                   <i class="fas fa-bars" style="color:white" onclick="myFunction()"></i>
                </div>
            </div>
            <div>
                <ul class="nav-items">
                    <li class="nav-link">
                        <a href="/">Home</a>
                    </li>
                <li class="nav-link">
                    <a href="/hoodies">Hoodies</a>
                </li>
                <li class="nav-link">
                    <a href="/tshirts">Tshirts</a>
                </li>
                <li class="nav-link">
                    <a href="/blogs">Blogs</a>
                </li>
                  <li class="nav-link">
                    <a href="/about Us">About us</a>
                </li>              
                </ul>
            </div>
            <div class="social text-gray">
                <a href="#">
                <i class="far fa-user-circle" id="user-img" style="font-size:20px color:white"></i>
                <div class="login-logout-popup hide">
                <p class="account-info">Log in as , name</p>
                <button class="btn" id="user-btn">Log out</button>
                </div>
                </a>
                <a href="/cart"><i class="fas fa-shopping-cart" style="font-size:20px color:white"></i></a>
                
            </div>
        </div>`;
};
createNav();

//nav popup
const userImageButton=document.querySelector('#user-img');
const userPop=document.querySelector('.login-logout-popup');
const popuptext=document.querySelector('.account-info');
const actionBtn=document.querySelector('#user-btn');

userImageButton.addEventListener('click',()=>{
    userPop.classList.toggle('hide');
})
window.onload=()=> {

        //means user is logged out
        popuptext.innerHTML='log in to place order'
        actionBtn.innerHTML='log in';
        actionBtn.addEventListener('click',()=>{
            location.href='/login';
        })


}
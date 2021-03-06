const createFooter = () => {
  const footer = document.querySelector("footer");
  footer.innerHTML = `      <div class="footer-content">
        <img
          src="{%static 'shop/campusconnectlogo.jpg' %}"
          alt="img"
          class="site-logo"
        />
        <div class="footer-ul-container">
          <ul class="category">
            <li class="category-title"><a href="#">Blogs</a></li>
          </ul>
          <ul class="category">
            <li class="category-title"><a href="#">Tshirts</a></li>
          </ul>
          <ul class="category">
            <li class="category-title"><a href="#">Hoodies</a></li>
          </ul>
        </div>
        -
      </div>
      <p class="footer-title">about CampusConnect</p>
      <p class="info">
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repellat
        tempore ad suscipit, eos eius quisquam sed optio nisi quaerat fugiat
        ratione et vero maxime praesentium, architecto minima reiciendis iste
        quo deserunt assumenda alias ducimus. Ullam odit maxime id voluptates
        rerum tenetur corporis laboriosam! Cum error ipsum laborum tempore in
        rerum necessitatibus nostrum nobis modi! Debitis adipisci illum nemo

      <p class="info">
        support emails - help@clothing.com, customersupport@clothing.com
      </p>
      <p class="info">telephone - 180 00 00 001, 180 00 00 002</p>
      <div class="footer-social-container">
        <div>
          <a href="" class="social-link"><i class="fab fa-instagram"></i></a>
          <a href="" class="social-link"><i class="fab fa-facebook"></i></a>
          <a href="" class="social-link"><i class="fab fa-discord"></i></a>
        </div>
      </div>
      <p class="footer-credit">
        | Copyright © 2021 CampusConnect.com | All Rights Reserved
      </p>`;
};
createFooter();

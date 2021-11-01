const createSmallCards = (data) => {
  return ` <div class="sn-product">
            <img
              src="${data.iamge}"
              alt=""
              class="sn-product-img"
            />
            <div class="sn-text">
              <p class="sn-product-name">${data.name}</p>
              <p class="sn-des">${data.shortDes}</p>
            </div>
            <div class="item-counter">
              <button class="counter-btn decrement">-</button>
              <p class="item-count">${data.item}</p>
              <button class="counter-btn decrement">+</button>
            </div>
            <p class="sn-price" data-price="${data.sellPrice}">${
    data.sellPrice * data.item
  }/-</p>
            <button class="sn-delete-btn"><img src="./img/close.png" alt=""></button>
          </div> `;
};
let totalBill = 0;

const setProducts = (name) => {
  const element = document.querySelector(`.${name}`);
  let data = JSON.parse(localStorage.getItem(name));
  if (data == null) {
    element.innerHTML = `<img src="./img/empty-cart.png" alt="" class="empty-img">`;
  } else {
    for (let i = 0; i < data.length; i++) {
      element.innerHTML += createSmallCards(data[i]);
      if (name == "cart") {
        totalBill += Number(data[i].sellPrice * data[i].item);
      }
    }
    updateBill();
  }
  setupEvents(name);
};
const updateBill = () => {
  let billPrice = document.querySelectorAll(".bill");
  billPrice.innerHTML = `${totalBill}/-`;
};

const setupEvents = (name) => {
  //setup counter event
  const counterMinus = document.querySelectorAll(`.${name} .decrement`);
  const counterPlus = document.querySelectorAll(`.${name} .increment`);
  const counts = document.querySelectorAll(`.${name} .item-counts`);
  const price = document.querySelectorAll(`.${name} .sn-price`);
  const deleteBtn = document.querySelectorAll(`.${name} .sn-delete-btn`);

  let product = JSON.parse(localStorage.getItem(name));
  counts.forEach((item, i) => {
    let cost = Number(price[i].getAttribute("data-price"));
    counterMinus[i].addEventListener("click", () => {
      if (itemm.innerHTML > 1) {
        item.innerHTML--;
        totalBill -= cost;
        price[i].innerHTML = `${item.innerHTML * cost}/-`;
        if (name == "cart") {
          updateBill();
        }

        product[i].item = item.innerHTML;
        localStorage.setItem(name, JSON.stringify(product));
      }
    });
    counterPlus[i].addEventListener("click", () => {
      if (itemm.innerHTML < 9) {
        item.innerHTML++;
        totalBill += cost;
        price[i].innerHTML = `${item.innerHTML * cost}/-`;
        if (name == "cart") {
          updateBill();
        }
        product[i].item = item.innerHTML;
        localStorage.setItem(name, JSON.stringify(product));
      }
    });
  });

  //delete product
  deleteBtn.forEach((item, i) => {
    item.addEventListener("click", () => {
      product = product.filter((data, index) => index != i);
      localStorage.setItem(name, JSON.stringify(product));
      location.reload();
    });
  });
};
setProducts("cart");
setProducts("wishlist");

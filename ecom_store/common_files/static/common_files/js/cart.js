let isOpen = false;
let cart = document.getElementById('shopping-cart')
let cartIcon = document.getElementById("shopping-cart-icon")

function openCloseCart() {
  if (isOpen) {
    isOpen = false;
    console.log(cart)
    cart.style.display = "none"
    console.log('closed')
  } else {
    isOpen = true;
    cart.style.display = "inline-block"
    console.log(cart)
    console.log('opened')
  }
}




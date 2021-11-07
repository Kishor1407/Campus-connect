   if(localStorage.getItem('cart') == null){
var cart = {};
}
else
{
cart = JSON.parse(localStorage.getItem('cart'));
}
$('.cart').click(function(){
console.log('clicked');
var idstr = this.id.toString();
console.log(idstr);
if (cart[idstr] !=undefined){
cart[idstr][0] = cart[idstr][0] + 1;
}
else
{
qty = 1;
name=document.getElementById('name').innerHTML;
name=document.getElementsByClassName('size-radio-btn').innerText;
cart[idstr] = [qty, name, size];
}
console.log(cart);
localStorage.setItem('cart', JSON.stringify(cart));
});
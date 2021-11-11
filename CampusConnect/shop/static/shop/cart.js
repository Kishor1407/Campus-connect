$('.cart').click(function(){
qty = 1;
name=document.getElementById('name').innerHTML;
price=document.getElementById('price').innerHTML;
var size=$('.check').text();
image = "/media/{{product.images}}";
$.ajax({
    url:'/managecart',
    type: "POST",
    data: cart,
});

});
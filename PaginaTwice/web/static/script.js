let cart = [];

function addToCart(productName, price) {
    cart.push({ name: productName, price: price });
    updateCart();
}

function updateCart() {
    const cartList = document.getElementById('cart-items');
    const totalElement = document.getElementById('total');

    cartList.innerHTML = '';
    
    let total = 0;

    cart.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = `${item.name} - $${item.price}`;
        cartList.appendChild(listItem);
        total += item.price;
    });

    totalElement.textContent = `Total: $${total}`;
}

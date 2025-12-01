products = []

function addProduct(){
    let name = document.getElementById("productName").value;
    let category = document.getElementById("productCategory").value;
    let price = document.getElementById("productPrice").value;
    let stock = document.getElementById("productStock").value;
    let desc = document.getElementById("productDesc").value;

    let p = new Product(name, category, price, stock, desc)
    products.push(p)
     document.getElementById("productName").value = '';
    document.getElementById("productPrice").value = '';
    document.getElementById("productStock").value = '';
    document.getElementById("productDesc").value = '';

    renderProducts()


}

function renderProducts(){
    let grid = document.getElementById('productsGrid')

    if(products.length === 0){
        grid.innerHTML = `
            <div>
                <p>محصولی یافت نشد</p>
            </div>
        `
        return
    }
    grid.innerHTML = products.map(p => `
        <div class="product-card">
            <div class="product-name">${p.name}</div>
            <div class="product-category">${p.category}</div>
            <div>${p.stock}</div>
            <div class="product-price">${p.price}</div>
            <div>${p.desc}</div>
        </div>
        `)
}




function Product(name, category, price, stock, desc){

    this.id = Date.now()
    this.name = name
    this.category = category
    this.price = price
    this.stock = stock
    this.desc = desc
    this.createAt = new Date()

    this.updateStock = function(quantity){
        this.stock += quantity
    }
    this.isAvailable = function(){
        return this.stock > 0
    }
    this.getInfo =  function(){
        return {
            id : this.id,
            name : this.name,
            category : this.category,
            price: this.price,
            stock : this.stock,
            available : this.isAvailable()
        }
    }
}

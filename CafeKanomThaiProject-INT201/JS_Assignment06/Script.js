// let number = 0;
// function addOrder(item){
//       alert("Your wish is granted.")
//       number++;
//       document.getElementById("cart").innerHTML = item+": "+ number
// }

import products from "./products.js";

let body = document.querySelector("body");

let topic = document.createElement("h1");
topic.textContent = "ร้านขายขนมรุ่งเรืองจริงๆ";
body.appendChild(topic);

let frame = document.createElement("div");
frame.className = "frame";

let items = body.appendChild(frame);

for (const product of products) {
	let lists = document.createElement("div");
	lists.className = "lists";
	lists.setAttribute("id", product.prodId);
	let item = items.appendChild(lists);
	item.className = "item";

	let image = document.createElement("img");
	image.src = product.prodImg;
	image.alt = product.name;
	image.style = "height:250px;";
	item.appendChild(image);

	let details = document.createElement("div");
	details.className = "details";

	let id = document.createElement("div");
	id.innerHTML = `<h5 class="detail"> Product ID : </h5> <p class="detail"> ${product.prodId} </p>`;
	details.appendChild(id);

	let name = document.createElement("div");
	name.innerHTML = `<h5 class="detail"> Name: </h5> <p> ${product.name} </p>`;
	details.appendChild(name);

	let price = document.createElement("div");
	price.innerHTML = `<h5 class = "detail"> Price: </h5> <p class="detail"> ${product.price} ฿ </p>`;
	details.appendChild(price);

	// let stock = document.createElement("div");
	// if (product.stock == 0) {
	// 	let outOfStock = document.createElement("b");
	// 	stock.innerHTML = `<h5 class = "detail"> Product in stock: </h5>`;
	// 	outOfStock.textContent = "This product is out of Stock";
	//     outOfStock.className = "empStock";
	// 	stock.appendChild(outOfStock);
	// } else {
	// 	stock.innerHTML = `<h5 class = "detail"> Product in stock: </h5> <p> ${product.stock} </p>`;
	// }

	let pieces = document.createElement("div");
	pieces.innerHTML = `<h5 class = "detail"> Pieces: </h5> <p class="detail"> ${product.pieces} </p>`;
	details.appendChild(pieces);

	let stock = document.createElement("div");
	if (product.stock > 0) {
		stock.innerHTML = `<h5 class = "detail"> Product in stock: </h5> <p> ${product.stock} </p>`;
	} else {
		let outOfStock = document.createElement("b");
		stock.innerHTML = `<h5 class = "detail"> Product in stock: </h5>`;
		outOfStock.textContent = "This product is out of Stock";
		outOfStock.className = "empStock";
		stock.appendChild(outOfStock);
	}
	details.appendChild(stock);

	item.appendChild(details);
}
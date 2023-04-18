<script setup>
import { ref, onBeforeMount } from "vue";
import Product from "../src/views/Product.vue";

const total = ref(0);
const cart = ref([]);
const products = ref([]);
const students = ref([]);
const editingQty = ref({});

onBeforeMount(async () => {
  await getProducts();
  console.log(products.value);
  await getStudents();
  console.log(students.value);
  await getCart();
  console.log(cart.value);
});
//GET Product
const getProducts = async () => {
  const res = await fetch("http://localhost:5000/products");
  if (res.status === 200) {
    products.value = await res.json();
  } else {
    console.log("not found");
  }
};
//GET Student
const getStudents = async () => {
  const res = await fetch("http://localhost:5000/students");
  if (res.status === 200) {
    students.value = await res.json();
  } else {
    console.log("not found");
  }
};
//GET Cart
const getCart = async () => {
  const res = await fetch("http://localhost:5000/cart");
  if (res.status === 200) {
    const data = await res.json();
    cart.value = data;
    total.value = data.length;
  } else {
    console.log("not found");
  }
};

const deleteProducts = async (delProdId) => {
  const res = await fetch(`http://localhost:5000/products/${delProdId}`, {
    method: "DELETE",
  });
  if (res.status === 200) {
    products.value = products.value.filter(
      (product) => product.id != delProdId
    );
    console.log("del successfully");
  } else {
    console.log("error , cannot del");
  }
};
// Edit Cart Item
const editCartItem = async (item) => {
  const res = await fetch(`http://localhost:5000/cart/` + item.id, {
    method: "PUT",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      qty: item.qty,
      price: item.price,
      name: item.name,
      id: item.id,
      src: item.src,
    }),
  });
  if (res.status === 200) {
    console.log("updated successfully");
  } else {
    console.log("error, cannot update");
  }
};
//Delete Cart Item
const removeCartItem = async (id) => {
  const res = await fetch(`http://localhost:5000/cart/` + id, {
    method: "DELETE",
    headers: { "content-type": "application/json" },
  });
  if (res.status === 200) {
    console.log("delete successfully");
  } else {
    console.log("error, cannot delete item");
  }
};

const increaseQty = (props) => {
  const index = cart.value.findIndex((item) => item.id == props.id);
  const baseIndex = products.value.findIndex((item) => item.id == props.id);
  cart.value[index].qty += 1;
  cart.value[index].price += products.value[baseIndex].price;
  editCartItem(cart.value[index]);
};

const decreaseQty = (props) => {
  const index = cart.value.findIndex((item) => item.id == props.id);
  const baseIndex = products.value.findIndex((item) => item.id == props.id);
  cart.value[index].qty -= 1;
  cart.value[index].price -= products.value[baseIndex].price;
  editCartItem(cart.value[index]);
};
//Delete Item
const deleteItem = (id) => {
  removeCartItem(id);
};
//Delete all item
const deleteAll = () => {
  for (var i = cart.value.length - 1; i >= 0; i--) {
    removeCartItem(cart.value[i].id);
  }
};
</script>

<template>
  <div>
    <header class="text-gray-600 body-font">
      <div
        class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center"
      >
        <a
          class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0"
        >
          <span class="ml-3 text-xl">Maew Bin</span>
        </a>
        <nav
          class="md:ml-auto flex flex-wrap items-center text-base justify-center"
        >
          <router-link to="/">
            <a class="mr-5 hover:text-gray-900">Home</a>
          </router-link>
          <router-link to="/About">
            <a class="mr-5 hover:text-gray-900">About</a>
          </router-link>
          <router-link to="/Cart">
            <button
              class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base md:mt-0"
            >
              Cart({{ total == 0 ? "-" : total }})
            </button>
          </router-link>
        </nav>
      </div>
    </header>
    <router-view
      :products="products"
      :students="students"
      :cart="cart"
      @deleteProducts="deleteProducts"
      @increase="increaseQty"
      @decrease="decreaseQty"
      @delete-item="deleteItem"
      @addToCart="increaseQty"
      @deleteAll="deleteAll"
    ></router-view>
  </div>
</template>

<style>
#app {
  font-family: Poppins, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #ffffff;
  color: black;
  margin: 0px;
}
</style>

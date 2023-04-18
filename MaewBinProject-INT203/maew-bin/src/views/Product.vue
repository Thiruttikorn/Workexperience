<script setup>
import { ref, computed } from "vue";
const emit = defineEmits(["deleteProducts", "addToCart"]);
const props = defineProps({
  products: {
    type: Array,
  },
  cart: {
    type: Array,
  },
});
console.log(props.products);
const addToCart = (product) => {
  const isHasInCart = props.cart.find((item) => item.id === product.id);
  if (!isHasInCart) {
    const newItem = { ...product, qty: 1 };
    fetch("http://localhost:5000/cart", {
      method: "POST",
      body: JSON.stringify(newItem),
      headers: { "content-type": "application/json" },
    })
      .then((response) => console.log(response.json))
      .catch((err) => console.log(err));
  } else {
    emit("addToCart", { id: isHasInCart.id });
    // console.log(isHasInCart);
  }
};
</script>

<template>
  <div>
    <div>
      <img class="banner" src="/src/assets/coffee.jpeg" />
    </div>
    <section class="text-gray-600 body-font">
      <div class="container px-5 py-10 mx-auto">
        <h1 class="title">Product of MaewBin</h1>
        <div class="flex flex-wrap -m-4">
          <div
            v-for="(product, index) of products"
            :key="index"
            class="lg:w-1/4 md:w-1/2 p-4 w-full"
          >
            <a class="block relative h-48 rounded overflow-hidden">
              <img
                alt="ecommerce"
                class="object-cover object-center w-full h-full block"
                :src="product.src"
              />
            </a>
            <div class="mt-4">
              <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">
                menu {{ product.id }}
              </h3>
              <h2 class="text-gray-900 title-font text-lg font-medium">
                {{ product.name }}
              </h2>
              <p class="mt-1">฿{{ product.price }}</p>
            </div>
            <div class="flex w-full md:justify-start set-flex items-end">
              <div
                @click="addToCart(product)"
                class="button-area mr-5 bg-green-400 hover:bg-green-500 rounded"
              >
                <button>Add to cart</button>
              </div>
              <div
                @click="$emit('deleteProducts', product.id)"
                class="button-area bg-red-500 hover:bg-red-600 rounded"
              >
                <button>Delete</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.set-flex {
  justify-content: center;
}
.banner {
  width: 100%;
}
.title {
  font-size: 25px;
  text-align: left;
  margin-bottom: 30px;
  color: black;
  font-weight: bold;
}
.button-area {
  border: none;
  color: white;
  padding: 10px 15px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin-top: 20px;
}
</style>

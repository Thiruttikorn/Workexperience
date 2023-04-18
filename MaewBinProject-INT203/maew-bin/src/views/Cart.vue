<script setup>
import { ref, onBeforeMount } from 'vue'
var totalBath = ref(0)
var totalItem = ref(0)
const emit = defineEmits(['increase', 'decrease', 'deleteItem', 'deleteAll'])
const props = defineProps({
  cart: {
    type: Array
  }
})
console.log(props.cart)

const increaseHandler = (id, price, qty) => {
  emit('increase', { id, price, qty })
}
const decreaseHandler = (id, price, qty) => {
  if (qty === 1) {
    // ลบออกจากตะกร้า
    emit('deleteItem', id)
    return
  }
  emit('decrease', { id, price, qty })
}
const DelAll = () => {
  emit('deleteAll')
  return
}
onBeforeMount(async () => {
  await getTotalBath()
  await getItem()
})

const getTotalBath = async () => {
  const res = await fetch('http://localhost:3000/cart')
  if (res.status === 200) {
    const data = await res.json()
    for (var i = 0; i < data.length; i++) {
      var plus = data[i]['price'] * data[i]['qty']
      totalBath.value = totalBath.value + plus
    }
  } else {
    console.log(' not found ')
  }
}

const getItem = async () => {
  const res = await fetch('http://localhost:3000/cart')
  if (res.status === 200) {
    const data = await res.json()
    for (var i = 0; i < data.length; i++) {
      var plus = data[i]['qty']
      totalItem.value = totalItem.value + plus
    }
  } else {
    console.log(' not found ')
  }
}
</script>

<template>
  <div>
    <h1 class="text-2xl">Product in the cart</h1>
    <br />
    <hr />
    <div v-for="item in cart" :key="item.id" :item="item">
      <div>
        <div class="text-xl">
          {{ item.name }}
        </div>
        <div class="text-lg">{{ item.price }} ฿</div>
        <div class="actions">
          <button
            @click="decreaseHandler(item.id, item.price, item.qty)"
            class="Cart mx-5"
          >
            -
          </button>
          <span class="item-qty">{{ item.qty }}</span>
          <button
            @click="increaseHandler(item.id, item.price, item.qty)"
            class="Cart mx-5"
          >
            +
          </button>
        </div>
        <br />
        <hr />
      </div>
    </div>
    <div class="mt-5 text-2xl">
      Total: {{ totalBath }}฿ with {{ totalItem }} items in the cart
    </div>
    <br />
    <div>
      <button @click="DelAll" class="ClearButton">Clear All Item</button>
    </div>
  </div>
</template>
<style scoped>
.Cart {
  background-color: #524229;
  border: none;
  color: white;
  padding: 2px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
.ClearButton {
  background-color: #f44336;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>

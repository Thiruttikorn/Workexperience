import Product from "../views/Product.vue"
import About from "../views/About.vue"
import Cart from "../views/Cart.vue"
import { createRouter, createWebHistory } from "vue-router";

const history = createWebHistory();
const routes = [
  { path: '/', component: Product},
  { path: '/About', component: About},
  { path: '/Cart', component: Cart}
];
const router = createRouter({ history, routes });
export default router;

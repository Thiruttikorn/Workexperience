import { createWebHistory, createRouter } from "vue-router";
import EventCategory from "../views/EventCategory.vue";
import EventScheduled from "../views/EventScheduled.vue";
import UserPage from "../views/UserPage.vue";
import LoginPage from "../views/LoginPage.vue";
import LogoutPage from "../views/LogoutPage.vue";
const routes = [
  {
    path: "/",
    name: "EventScheduled",
    component: EventScheduled,
  },
  {
    path: "/EventCategory",
    name: "EventCategory",
    component: EventCategory,
  },
  {
    path: "/Users",
    name: "UserPage",
    component: UserPage,
  },
  {
    path: "/LoginPage",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/LogoutPage",
    name: "LogoutPage",
    component: LogoutPage,
  },

];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;

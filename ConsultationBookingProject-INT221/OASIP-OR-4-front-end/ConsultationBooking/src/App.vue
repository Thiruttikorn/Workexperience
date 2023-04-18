<script>
export default {
  name:'App',
  data() {
    return {
      form: {
       
        email:'',
        password:''
      },
      showError: false
    };
  },
  computed: {
   isLoggedIn() {
    return window.localStorage.getItem("token");
  }
},
  methods:{
   handleLogout(){
            localStorage.removeItem('token');
            // this.$router.push('/LoginPage');
          }
        }
  }
</script>

<template>
  <div>
    <div class="bg-indigo-600">
      <nav class="container px-1 py-8 mx-auto md:flex md:items-center">
        <div class="flex flex-row">
          <div class="basis-1/8">
            <router-link
              to="/"
              class="text-xl font-bold text-gray-100 md:text-2xl hover:text-indigo-400"
            >
              Event Scheduled
            </router-link>
          </div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <div class="basis-1/8">
            <router-link
              to="/EventCategory"
              class="text-xl font-bold text-gray-100 md:text-2xl hover:text-indigo-400"
            >
              Event Category
            </router-link>
          </div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <div class="basis-1/8">
            <router-link
              to="/Users"
              class="text-xl font-bold text-gray-100 md:text-2xl hover:text-indigo-400"
            >
              User Page
            </router-link>
           </div>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <div class="basis-1/8" v-if="isLoggedIn==null">
            <router-link
              to="/LoginPage"
              class="text-xl font-bold text-gray-100 md:text-2xl hover:text-indigo-400"
            >
              LoginPage
            </router-link>
            </div>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <div class="basis-1/8" v-else>
            <router-link 
            @click="handleLogout"
              to="/LogoutPage"
              class="text-xl font-bold text-gray-100 md:text-2xl hover:text-indigo-400"
            >
              LogoutPage
            </router-link>
            </div>


        </div>
      </nav>
    </div>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<style scoped>
#container {
  display: flex;
  justify-content: center;
}
</style>


<script > 
import Login from './Login.vue';
export default {
  name: 'Logout',
     
    props:{   
    email:"",
    password:"",
    localStorage:"",
    emptyFields: false,
    isLoggedOut:false,
   
    } 
   ,methods: {
     handleLogout() {
      localStorage.removeItem('token',this.email);
         this.$router.push('Loginpage');
      }
   
}
,
mounted(){  
    // handleLogout(
      fetch(`https://${import.meta.env.VITE_API}/logout`, {
        headers: {
//  'Authorization':authToken,
     method: 'GET',
    'Content-Type': 'application/json'
     },
    }
    // .then(function(response) {
    //console.log(response.status ); // Will show you the status
    // localStorage.removeItem('token',this.email,this.accessToken);
//}
//)
)
},components: {Login}
   }
</script>



<template>

  <form >
    <!-- action="#" method="post" -->
    <div class="container">
        <div class="row">
           <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">

<div class="isLoggedOut" >
  <h3>Logout</h3>
<!-- <router-link to="/LoginPage"> -->
<button

  type="button" 
  id="logout-button" 
  class="isLoggedOut"
   @click="handleLogout()"
   :disabled="isLoggedOut"
   emptyFields = false
   > Logout
</button> 
 <!-- </router-link> -->
</div>
</div>
</div>
</div>

</form>

</template>

<style>
p {
  line-height: 1rem;
}

.card {
  padding: 20px;
}

.form-group {

     margin-bottom: 20px;
 
}

  
   .fade-enter-active,
  .fade-leave-active {
 transition: opacity .5s;
} 
  .fade-enter,
  .fade-leave-to {
     opacity: 0;
  }
  
  h1 {
     margin-bottom: 1.5rem;
  }


.error {
  animation-name: errorShake;
  animation-duration: 0.3s;
}


@keyframes errorShake {
  0% {
     transform: translateX(-25px);
  }
  25% {
     transform: translateX(25px);
  }
  50% {
     transform: translateX(-25px);
  }
  75% {
     transform: translateX(25px);
  }
  100% {
     transform: translateX(0);
  }
 
}
#logout-button {
    background-color: blue;
    color: white;
    border: none;
    padding: 5px 10px;
  }

  #logout-button[disabled] {
    background-color: lightgray;
    color: gray;
  }
  #login-button {
    background-color: blue;
    color: white;
    border: none;
    padding: 5px 10px;
  }

  #login-button[disabled] {
    background-color: lightgray;
    color: gray;
  }

</style>
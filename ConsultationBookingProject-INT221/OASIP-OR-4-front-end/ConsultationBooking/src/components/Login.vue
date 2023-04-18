
<script > 
import { required } from '@vuelidate/validators'
import useValidate from '@vuelidate/core'


import {reactive, computed} from 'vue'
export default {
  name: 'Login',
  setup() {
        const state = reactive({
            email:'',
            password:'',
            localStorage:''
        })

        const rules=computed(() => {
                 return {
                email: { required },
                password: { required },
                localStorage:{}
        }
    })
    
    const v$ =  useValidate(rules,state)

        return{
            state,v$,
        }
  
  },
mounted(){  
      fetch(`https://${import.meta.env.VITE_API}/login`, {
        headers: {
 // 'Authorization':authToken,
     method: 'POST',
    'Content-Type': 'application/json'
     },body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      }
    )
.then(function(response) {
    console.log(response.status ); // Will show you the status
   //  if (!response.ok) {
      if (res.status === 401) {
      //   throw new Error("HTTP status " + response.status);
      alert('ERROR: 401');
             console.log('ERROR: 401');
               res.sendStatus(401);
    }
      else{ res.json({
          authorizedData
               });
              alert("Login Successful ");
    return this.handleSubmit();
    }
    })
  },methods: {
  async handleSubmit(){
  
    this.v$.$validate()
            if (!this.v$.$error) {
          
            const response = ({
                    email:this.state.email,
                    password: this.state.password
            });
            console.log(response);
            localStorage.setItem('token',this.email);
            alert('Login Successful')
            this.$router.push('/LogoutPage');
          }else{
            alert('ERROR: 401')
           return false;
              
          }

    //  response = {
    //       email: this.email,
    //      password: this.password,
    //      token:this.token,
    //     };

    // localStorage.setItem('token',this.localStorage.token);
    //     if(this.localStorage.token === null || this.localStorage.token === "" ){
    //       return false;
         
    //   }else {
    //      this.$router.push("LogoutPage")
    //   }
   }

   
}
}



</script>



<template>

  <form >
    <!-- action="#" method="post" -->
    <div class="container">
        <div class="row">
           <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">


<div class="from-group"  >
  <h3>Login</h3>
 
<label>Email</label>
<input v-model="state.email" type="email"  class="from-control" placeholder="Email" required/>

<label>Password</label>
<input v-model="state.password" type="password" class="from-control" placeholder="password" required/>

<button
 type="submit" 
 id="login-button"
 class="isLoggedIn" 
 :disabled="isLoggedIn"
 emptyFields = false
 @click.prevent="handleSubmit()"
 >
  LogIn
</button>

<!-- <button
id="login-button"
 class="handleSubmit" 
 v-on:click='isLoggedIn' 
a href="/isLoggedOut" @click="handleSubmit =!handleSubmit, emptyFields = false">Login</button>
<p>Don't have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">register </a>                    </p> -->

</div>

</div>
</div>
</div>


</form>
  <!-- <div class="navbar-end">
  <div class="navbar-item">
    <div class="buttons"> -->
      <!-- Check that the SDK client is not currently loading before accessing is methods -->
      <!-- <div v-if="!$auth.loading"> -->
        <!-- show login when not authenticated -->
        <!-- <a v-if="!$auth.isAuthenticated" @click="login" class="button is-dark"
          ><strong>Sign in</strong></a
        > -->
        <!-- show logout when authenticated -->
        <!-- <a v-if="$auth.isAuthenticated" @click="logout" class="button is-dark"
          ><strong>Log out</strong></a
        >
      </div>
    </div>
  </div>
</div> -->
<!--    
<form action="/action_page.php" method="post">

     <div class="container">
        <div class="row">
           <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
              <div v-if="!login" class="login" v-bind:class="{ error: emptyFields }">
                 <h1>Sign In</h1>
                 <form class="form-group">
                    <input v-model="emailLogin" type="email" class="form-control" placeholder="Email" required>
                    <input v-model="passwordLogin" type="password" class="form-control" placeholder="Password" required>
                    <input type="submit" next-link to="/logout.vue"
                    a href="/logout" class="form-control" @click="login==login, emptyFields = true"> -->
                    <!-- <p>Don't have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">register </a>
                    </p>
                    <p><a href="#">Forgot your password?</a></p> -->
                 <!-- </form>
              </div> -->
            

              <!-- <div v-else- ="!registerActive" class="card register" v-bind:class="{ error: emptyFields }">
                 <h1>Register</h1>
                 <form class="form-group">
                    <input v-model="emailReg" type="email" class="form-control" placeholder="Email" required>
                    <input v-model="passwordReg" type="password" class="form-control" placeholder="Password" required>
                    <input v-model="confirmReg" type="password" class="form-control" placeholder="Confirm Password" required>
                    <input type="submit" class="btn btn-primary" @click="doRegister">
                    <p>Already have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign in here</a>
                    </p>
                 </form>
              </div> -->
<!-- 
              <div v-else="logout" class="card logout"  v-bind:class="{ error: emptyFields }">
                <form class="form-group">
             <button
               id="logout"
               @click.prevent="handleLogout"
               :disabled="isLoggedOut"
               href="/LoginPage.vue"
               @click="Logout" class="button--grey">Logout</button>
              </form>
              </div>      
            </div>
        </div> 
</div>
</form> -->
  
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
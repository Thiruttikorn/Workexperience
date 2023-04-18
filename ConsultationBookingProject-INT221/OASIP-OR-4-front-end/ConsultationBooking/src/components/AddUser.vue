<script>
import useVuelidate from '@vuelidate/core'
import { required, email, maxLength} from '@vuelidate/validators'
export default {
setup() {
    return { v$: useVuelidate() }
    },
data() {
    return {
Users:[],
Roles:'',
User_id: 0,
User_name: '',
User_email: '',
User_role: '',
User_createdOn: '',
User_updateOn: '',
User_password:''
    }
},
validations() {
    return {
User_name: { required, maxLength: maxLength(100)},
User_email: { required, email, maxLength: maxLength(50) },
User_role: {required },
User_createdOn: { required },
User_updateOn: { required},
User_password:{required,maxLength:maxLength(8,14)}
    }
  },
  mounted() {
    fetch(`https://${import.meta.env.VITE_API}/users`, {
      headers: {
        'Content-Type': 'application/json'
}
    })
.then((res) => {
        // console.log(res)
        return res.json()
})
.then((Users) => {
        this.Users.push(...Users)
        // console.log(this.categorys);
})
.catch((error) => {
        console.log('Users : Something went wrong!', error)
        console.log(import.meta.env)
})
},
methods: {
    async submit() {
const result = await this.v$.$validate()
if (!result) {
        // notify user form is invalid
        return false
}

    },
checkPass(){
if(password1 == password2){
  return true
}else{
  alert ("The password does not match")
  return false
}
},


    createClick() {
if (
        this.User_name != '' &&
        this.User_email != '' &&
        this.User_role != '' &&
        this.User_createdOn != ''&&
        this.User_updatedOn !=''&&
        this.User_password!=''
) {
        alert("create")
        let data = {
        User_id: this.User_id,
        User_name: this.User_name,
        User_email: this.User_email,
        User_role: this.User_role,
        User_createdOn: this.User_createdOn,
        User_updatedOn: this.User_updatedOn,
        User_password:this.User_password,
       
        }
        fetch(`https://${import.meta.env.VITE_API}/users`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }  ,
        body: JSON.stringify(data)
        })
        .then((res) => {
            return res.json()
        })
        .catch((error) => {
            console.log('POST:Something went wrong!', error)
            console.log(import.meta.env)
        })
        .then((res) => alert(res))
        .then(() => {
            // this.checkDateTime()
            this.clearClick()
            this.$emit('addUser')
})
}
else{
        alert("กรุณากรอกให้ครบถ้วน")
}
    },
    // checkDateTime: function () {
    //   var dateTime = this.startDateTime
    //   var date = Date.now
    //   if (dateTime <= date) {
    //     alert('Date must be in the  future')
    //   }
    //   return false
    // },
    // checkDateTimeDuplicated: function (userTime, nTime) {
    //   var startDateTime = this.startDateTime
    //   var Duration = this.category.Event_duration
    //   userTime = startDateTime + Duration
    //   var categoryDuration = this.category.Event_duration
    //   var nTime = this.Event_startTime
    //   nTime = nTime + categoryDuration
    //   if (Event.Event_startTime == startDateTime || userTime <= nTime) {
    //     alert("Date Time can't be duplicated")
    //   }
    //   return false
    // },
    clearClick() {
    this.User_id = ''
    this.User_name = ''
    this.User_email = ''
    this.User_role = ''
    this.User_createdOn=''
    this.User_updatedOn = ''
    this.User_password
    }
}
}
</script>
<template>
<div>
    <div
    class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
    id="AddUser"
    tabindex="-1"
    aria-labelledby="exampleModalCenterTitle"
    aria-modal="true"
    role="dialog"
    >
    <div
        class="modal-dialog modal-dialog-centered relative w-auto pointer-events-none"
>
    <div
        class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
        >
    <div class="py-6 px-6 lg:px-8">
            <h3 class="mb-4 text-xl font-medium text-gray-900">
            Add User 
            </h3>
        <form
        class="needs-validation space-y-6"
        @submit.prevent="submitForm"
        novalidate
            >
         <div>
            <label
            for="sname"
            :class="{ error: v$.User_name.$errors.length }"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Name<span class="text-danger">*</span></label
                >
        <input
            required
            type="text"
            id="sname"
            name="sname"
            v-model="v$.User_name.$model"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
            placeholder="Enter your name"
            unique
            notNull
                />
        </div>
                <div
                class="input-errors"
                v-for="(error, index) of v$.User_name.$errors"
                :key="index"
>
                <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                </div>
        </div>

            <div>
                <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                :class="{ error: v$.User_email.$errors.length }"
                >Your email<span class="text-danger">*</span></label
                >
                <input
                required
                type="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="Enter your email"
                v-model="v$.User_email.$model"
                unique
                notNull
                />
                <div
                  class="input-errors"
                  v-for="(error, index) of v$.User_email.$errors"
                  :key="index"
                >
                  <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                  </div>
                </div>
              </div>

          
              <div>
                <label
                  for="Roles"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >role<span class="text-danger">*</span></label
                >
                <select
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  v-model="v$.Roles"
                 
               >
                  <option value=" ">Select a role</option>
                      
                    <option    
                                  
                    v-for="Roles in Roles"
                    v-bind:value="{
                    User_id: Users.User_id,
                    User_role:Roles.ADMIN ,
                    User_role:Roles.LECTURER ,
                    User_role :Roles.STUDENT 
                    
                    }"
                    SET DEFAULT ROLE STUDENT  
                    :key="User_role.User_id "
                         
                  >
                    {{ User_role.User_name }}
                  </option>
                </select>
                <div
                  class="input-errors"
                  v-for="(error, index) of v$.Roles"
                  :key="index"
                >
                  <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                  </div>


              <div>
                <label for="pass">Password (8 characters minimum,14 characters maxLength)</label>
                <input type="password" id="pass" name="password1" minlength="8" maxLength="14" required><input/>
              </div>
              <div>
                <label for="pass">confirm Password </label>
                <input type="password" id="pass" name="password2" minlength="8" maxLength="14" required><input/>
              </div>


              <div
                  class="input-errors"
                  v-for="(error, index) of v$.User_password.$errors"
                  :key="index"
                >
              <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                  </div>
                  </div>
                </div>
              </div> 
            <div>
                <button
                  type="submit"
                  value="Save"
                  class="inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
                  @click="createClick()"
                >
                  Add</button
                >&nbsp;
                <button
                  type="button"
                  class="inline-block px-6 py-2.5 bg-white text-gray-500 font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
                  data-bs-dismiss="modal"
                  @click="clearClick()"
                >
                  cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>

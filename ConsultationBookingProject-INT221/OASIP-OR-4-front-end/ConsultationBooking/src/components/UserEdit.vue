<script>
    import moment from "moment";
    import useVuelidate from '@vuelidate/core'
    import { required, email,maxLength } from '@vuelidate/validators'
    
    export default {
      setup() {
        return { v$: useVuelidate() }
      },
      name: "UserEdit",
      props: {
          id: Number,
          User_id: Number,
          User_name: String,
          User_email: String,
          User_role: String,
          User_createdOn: String,
          User_updateOn: String,
          Roles:Object,
          Users:Object
      },
      data() {
        return {
          Users: [],
          User_name: this.User_name.trimmed,
          User_email:this.User_email.trimmed,
          newData: {
            User_id: this.User_id,
            User_name: this.User_name.trimmed,
            User_email: this.User_email.trimmed,
            User_role:this.User_role,
            User_createdOn:this.User_createdOn,
            User_updateOn:this.User_updateOn
            
          },
        };
      },
       validations() {
        return {
          User_name:{required,maxLength:maxLength(100)},
          User_email: { required, email,maxLength:maxLength(50) },
          newData: {
            User_name:{required,maxLength:maxLength(100)},
            User_email: { required, email,maxLength:maxLength(50) }
          }
        }
      },
      mounted() {
        fetch(`https://${import.meta.env.VITE_API}/Users`, {
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
          console.log('abc');
          console.log(this.newData.Users)
      },
      methods: {
         updateClick() {

        
          if(newData==data){return false}

          fetch(`https://${import.meta.env.VITE_API}/Users`,{
            method: "PUT",
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.newData)
          })
            .then((res) => res.json())
            .then((res) => alert(res))
            .catch((reason) => alert(reason))
            .then(() => this.$emit("editUser"));

        },
        formatDate(date) {
          return moment(date).subtract(7, "hours").format("YYYY-MM-DDThh:mm");
        },
        clearClick() {
          // this.$emit("clearCurrent");
          this.newData.User_id = this.User_id;
          this.newData.User_name = this.User_name;
          this.newData.User_email = this.User_email;
          this.newData.User_role = this.User_role;
          
        },
      },
    };
    </script>
    <template>
      <div>
        <div
          class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
          v-bind:id="'UserEdit-' + id"
          tabindex="-1"
          aria-labelledby="ModalCenterTitle"
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
                  Edit User Platform
                </h3>
                <form class="space-y-6"/>
                <div>
                  <label
                    for="Name"
                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >Name *</label
                  >
                  <input
                    v-model="newData.User_name"
                    type="text"
                    id="Name"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                   
                    required
                  />
                </div>
    
                <div>
                    <label
                      for="email"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                      :class="{ error: v$.newData.User_email.$errors.length }"
                      >Your email *</label
                    >
                    <input
                      type="email"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                      placeholder="Enter your email"
                      v-model="newData.User_email"
                      
                    />
                    <div
                      class="input-errors"
                      v-for="(error, index) of v$.newData.User_email.$errors"
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
                    >Roles</label
                  >
                  <select
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                    v-model="newData.Event_category"
                    disabled
                  >
                    <option value="">Select a Roles</option>
                    <option
                      v-for="Roles in Roles"
                      v-bind:value="{
                        User_id: Users.User_id,
                    User_role:Roles.ADMIN ,
                    User_role:Roles.LECTURER ,
                    User_role :Roles.STUDENT 
                        }"
                         :key="User_role.User_id "
                    >
                        {{ User_role.User_name }}
                    </option>
                    </select>
                </div>
    
                <div>
                  <button
                    type="submit"
                    class="inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
                    data-bs-dismiss="modal"
                    @click="updateClick()"
                  >
                    save</button
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
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
    
    <style scoped></style>
    

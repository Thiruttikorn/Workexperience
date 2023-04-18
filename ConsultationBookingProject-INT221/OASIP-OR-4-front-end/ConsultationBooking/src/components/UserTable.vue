<script >
import UserDetail from "./UserDetail.vue";
import AddUser from "./AddUser.vue";
import UserDelete from "./UserDelete.vue";
import UserEdit from "./UserEdit.vue";
import moment from "moment";

export default {
  data() {
    return {
      Users: [],
    };
  },

  mounted() {
    console.error("WTF");
    fetch(`https://${import.meta.env.VITE_API}/users`, {
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => {
        console.log(res);
        return res.json();
      })
      .then((Users) => {
        this.Users.push(...Users);
      })
      .catch((error) => {
        console.log("Something went wrong!", error);
        console.log(import.meta.env);
      });
  },
  methods: {
    onAddUser() {
      fetch(`https://${import.meta.env.VITE_API}/users`, {
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => {
          return res.json();
        })
        .then((Users) => {
          this.Users.length = 0;
          this.Users.push(...Users);
        });
    },
    onDeleteEvent(id) {
      this.Users.splice(id, 1);
    },
    formatDate(date, format) {
      if (typeof format === "undefined") {
        format = "MMMM Do YYYY, h:mm a";
      }
      return moment(date).format(format);
    },
  },
  components: {
    UserDetail,
    AddUser,
    UserDelete,
    UserEdit,
   
  },
};
</script>
<template>
  <div class="add container px-6 py-2 mx-auto">
    <div>
      <nav class="container px-6 py-1 mx-auto">
        <button
          type="button"
          class="inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
          data-modal-toggle="Adduser"
          data-bs-toggle="modal"
          data-bs-target="#AddUser"
        >
          Add User
        </button>

        <AddUser v-on:AddUser="onAddUser" />

        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
          <p v-if="Users.length === 0">No Users</p>
          <table
            class="w-full text-sm text-left text-black-500 dark:text-black-400 bg-gray-400"
            v-else
          >
            <thead>
              <tr>
                <th scope="col" class="px-6 py-3">name</th>
                <th scope="col" class="px-6 py-3">email</th>
                <th scope="col" class="px-6 py-3">role</th>
              </tr>
            </thead>
            <tbody>
              <tr
                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                v-for="(Users, i) in Users"
                :key="Users.User_id"
              >
                <th scope="row" class="px-6 py-4">
                  {{ Users.User_name }}
                </th>
                <td class="px-6 py-4" align="left">
                  {{ Users.User_email }}
                </td>
                <td class="px-6 py-4" align="left">
                  {{ Users.User_role }}
                </td>
                <td class="px-6 py-4" align="left">
                  {{ Users.User_password }}
                </td>

                <td class="px-6 py-4" align="left">
                  <AddUser v-on:AddUser="onAddUser()" />
                </td>

                <div
                  class="button block space-y-4 md:flex md:space-y-0 md:space-x-4"
                >
                  <td class="px-6 py-4">
                    <button
                      type="button"
                      class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                      data-bs-toggle="modal"
                      v-bind:data-bs-target="'#UserDetails-' + Users.User_id"
                    >
                      Details
                    </button>
                    <UserDetail
                      v-bind:id="Users.User_id"
                      v-bind:name="Users.User_name"
                      v-bind:email="Users.User_email"
                      v-bind:role="Users.User_role"
                      v-bind:createdOn="Users.Roles.User_createdOn"
                      v-bind:updateOn="Users.Roles.User_updateOn"
                    />
                  </td>
                </div>

                <td class="px-6 py-4">
                  <button
                    type="button"
                    class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                    data-bs-toggle="modal"
                    v-bind:data-bs-target="'#UserEdit-' + i"
                  >
                    Edit
                  </button>
                  <UserEdit
                    v-bind:id="i"
                    v-bind:User_id="Users.User_id"
                    v-bind:name="Users.User_name"
                    v-bind:email="Users.User_email"
                    v-bind:role="Users.User_role"
                    v-on:editUser="onAddUser()"
                  />
                </td>
                <td class="px-6 py-4">
                  <button
                    type="button"
                    class="inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
                    data-bs-toggle="modal"
                    v-bind:data-bs-target="'#UserDelete-' + i"
                  >
                    Delete
                  </button>
                  <UserDelete
                    v-bind:id="i"
                    v-bind:user_id="Users.User_id"
                    v-on:deleteUser="onDeleteUser(i)"
                  />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </nav>
    </div>
  </div>
</template>

<style>
.table { margin-bottom: 0px; } 
.table-box { overflow-x: auto; display: inherit;
margin-bottom: 20px; }
.button {
  float: right;
  margin-top: 20px;
}
p {
  text-align: center;
  color: gray;
}
</style>

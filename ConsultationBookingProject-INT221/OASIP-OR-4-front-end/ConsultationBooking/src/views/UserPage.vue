<script>
import UserTable from "../components/UserTable.vue";
import AddUser from "../components/AddUser.vue"
export default {
  name: "User",
  components: {UserTable,AddUser},
};
</script>
<template>
<div class="text-xl font-bold md:text-2xl">
    <br>
    <nav class="container px-6 py-3">
      <h1>User Page</h1>
        <br />
        <hr />
    </nav>
    <div>
      <UserTable/>
    </div>
  </div>

</template>


<style>
</style>

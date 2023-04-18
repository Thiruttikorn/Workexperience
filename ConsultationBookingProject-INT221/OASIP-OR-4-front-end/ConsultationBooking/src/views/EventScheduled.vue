<script>
import Table from "../components/Table.vue";
import FormEvent from "../components/FormEvent.vue";
export default {
  name: "EventScheduled",
  components: { Table, FormEvent },
};
</script>

<template>
  <div class="text-xl font-bold md:text-2xl">
    <br>
    <nav class="container px-6 py-3">
        <h1>Event Scheduled</h1>
        <br />
        <hr />
    </nav>
    <div>
      <Table />
    </div>
  </div>
</template>
<style scoped>
/* H1 {

} */
</style>

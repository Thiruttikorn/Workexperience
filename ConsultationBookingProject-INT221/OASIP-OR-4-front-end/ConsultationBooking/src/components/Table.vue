<script>
import PopupDetail from "./PopupDetail.vue";
import PopupCancel from "./PopupCancel.vue";
import PopupEdit from "./PopupEdit.vue";
import FormEvent from "./FormEvent.vue";
import moment from "moment";

export default {
  data() {
    return {
      events: [],
    };
  },
  mounted() {
    fetch(`https://${import.meta.env.VITE_API}/events`, {
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => {
        console.log(res);
        return res.json();
      })
      .then((events) => {
        this.events.push(...events);
        // console.log(this.events);
      })
      .catch((error) => {
        console.log("Something went wrong!", error);
        console.log(import.meta.env);
      });
  },
  methods: {
    onAddEvent() {
      fetch(`https://${import.meta.env.VITE_API}/events`, {
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => {
          return res.json();
        })
        .then((events) => {
          this.events.length = 0;
          this.events.push(...events);
        });
    },
    onDeleteEvent(id) {
      this.events.splice(id, 1);
    },
    formatDate(date, format) {
      if (typeof(format) === 'undefined'){
        format = 'MMMM Do YYYY, h:mm a'
      }
      return moment(date).format(format);
    }
  },
  components: { PopupDetail, PopupCancel, PopupEdit, FormEvent },
};
</script>
<template>
  <div class="add container px-6 py-2 mx-auto">
    <button
      type="button"
      class="inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
      data-modal-toggle="addEvent"
      data-bs-toggle="modal"
      data-bs-target="#addEvent"
    >
      Add Event
    </button>
    <FormEvent v-on:addEvent="onAddEvent" />
  
  <div>
    <nav class="container px-6 py-1 mx-auto">
      <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <p v-if="events.length === 0">No Scheduled Events</p>
        <table
          class="w-full text-sm text-left text-black-500 dark:text-black-400 bg-gray-400"
          v-else
        >
          <thead>
            <tr>
              <th scope="col" class="px-6 py-3">Name</th>
              <th scope="col" class="px-6 py-3">Category</th>
              <th scope="col" class="px-6 py-3">Date/Time</th>
              <th scope="col" class="px-6 py-3">Duration</th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
              v-for="(event, i) in events"
              :key="event.Booking_id"
            >
              <th scope="row" class="px-6 py-4">
                {{ event.Booking_name }}
              </th>
              <td class="px-6 py-4" align="left">
                {{ event.Event_category.Event_category_name }}
              </td>
              <td class="px-6 py-4" align="left">
                {{ formatDate(event.Event_startTime) }}
              </td>
              <td class="px-6 py-4" align="left">
                {{ event.Event_category.Event_duration }} mins
              </td>

              <td class="px-6 py-4" align="left">
                <FormEvent v-on:addEvent="onAddEvent()" />
              </td>

              <div
                class="button block space-y-4 md:flex md:space-y-0 md:space-x-4"
              >
                <td class="px-6 py-4">
                  <button
                    type="button"
                    class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                    data-bs-toggle="modal"
                    v-bind:data-bs-target="'#popupDetails-' + event.Booking_id"
                  >
                    Details
                  </button>
                  <PopupDetail
                    v-bind:id="event.Booking_id"
                    v-bind:name="event.Booking_name"
                    v-bind:email="event.Booking_email"
                    v-bind:startDateTime="formatDate(event.Event_startTime)"
                    v-bind:note="event.Event_notes"
                    v-bind:category="event.Event_category.Event_category_name"
                    v-bind:duration="event.Event_category.Event_duration"
                  />
                </td>
                <td class="px-6 py-4">
                  <button
                    type="button"
                    class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                    data-bs-toggle="modal"
                    v-bind:data-bs-target="'#popupEdit-'+i"
                  >
                    Edit
                  </button>
                  <PopupEdit
                    v-bind:id="i"
                    v-bind:booking_id="event.Booking_id"
                    v-bind:booking_name="event.Booking_name"
                    v-bind:booking_email="event.Booking_email"
                    v-bind:startDateTime="formatDate(event.Event_startTime, 'YYYY-MM-DDThh:mm')"
                    v-bind:notes="event.Event_notes"
                    v-bind:category="event.Event_category"
                    v-bind:duration="event.Event_category.Event_duration"
                    v-on:editEvent="onAddEvent()"
                  />
                </td>
                <td class="px-6 py-4">
                  <button
                    type="button"
                    class="inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
                    data-bs-toggle="modal"
                    v-bind:data-bs-target="'#popupCancel-' + i"
                  >
                    Delete
                  </button>
                  <PopupCancel
                    v-bind:id="i"
                    v-bind:Booking_id="event.Booking_id"
                    v-on:deleteEvent="onDeleteEvent(i)"
                  />
                </td>
              </div>
            </tr>
          </tbody>
        </table>
      </div>
    </nav>
  </div>
 </div>
</template>
.table { margin-bottom: 0px; } .table-box { overflow-x: auto; display: inherit;
margin-bottom: 20px; }
<style>
.button {
  float: right;
  margin-top: 20px;
}
p {
  text-align: center;
  color: gray;
}
</style>

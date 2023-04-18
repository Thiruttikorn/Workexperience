<script>
import moment from "moment";
import useVuelidate from '@vuelidate/core'
import { required, email } from '@vuelidate/validators'

export default {
  setup() {
    return { v$: useVuelidate() }
  },
  name: "PopupEdit",
  props: {
      id: Number,
      booking_id: Number,
      booking_name: String,
      booking_email: String,
      startDateTime: String,
      notes: String,
      category: Object,
  },
  data() {
    return {
      categorys: [],
      booking_email:this.booking_email,
      newData: {
        Booking_id: this.booking_id,
        Booking_name: this.booking_name,
        Booking_email: this.booking_email,
        Event_startTime: this.startDateTime,
        Event_notes: this.notes,
        Event_category: {
          Event_category_id:  this.category.Event_category_id,
          Event_category_name: this.category.Event_category_name ,
          Event_category_description: this.category.Event_category_description,
          Event_duration: this.category.Event_duration,
        }
      },
    };
  },
   validations() {
    return {
      booking_email: { required, email },
      newData: {
        Booking_email: { required, email }
      }
    }
  },
  mounted() {
    fetch(`https://${import.meta.env.VITE_API}/categories`, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((res) => {
        // console.log(res)
        return res.json()
      })
      .then((categorys) => {
        this.categorys.push(...categorys)
        // console.log(this.categorys);
      })
      .catch((error) => {
        console.log('categorys : Something went wrong!', error)
        console.log(import.meta.env)
      })
      console.log('abc');
      console.log(this.newData.Event_category)
  },
  methods: {
    updateClick() {
      fetch(`https://${import.meta.env.VITE_API}/events`,{
        method: "PUT",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.newData)
      })
        .then((res) => res.json())
        .then((res) => alert(res))
        .catch((reason) => alert(reason))
        .then(() => this.$emit("editEvent"));
    },
    formatDate(date) {
      return moment(date).subtract(7, "hours").format("YYYY-MM-DDThh:mm");
    },
    clearClick() {
      // this.$emit("clearCurrent");
      this.newData.Booking_id = this.booking_id;
      this.newData.Booking_name = this.booking_name;
      this.newData.Booking_email = this.booking_email;
      this.newData.startTime = this.startDataTime;
      this.newData.notes = this.notes;
      this.newData.category = this.category;
    },
  },
};
</script>
<template>
  <div>
    <div
      class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
      v-bind:id="'popupEdit-' + id"
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
              Edit Event Platform
            </h3>
            <form class="space-y-6"/>
            <div>
              <label
                for="Name"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Name *</label
              >
              <input
                v-model="newData.Booking_name"
                type="text"
                id="Name"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                 readonly
                required
              />
            </div>

            <div>
                <label
                  for="email"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  :class="{ error: v$.newData.Booking_email.$errors.length }"
                  >Your email *</label
                >
                <input
                  type="email"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Enter your email"
                  v-model="newData.Booking_email"
                  readonly
                />
                <div
                  class="input-errors"
                  v-for="(error, index) of v$.newData.Booking_email.$errors"
                  :key="index"
                >
                  <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                  </div>
                </div>
              </div>

            <div>
              <label
                for="meeting-time"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Date/Time *
              </label>
              <input
                type="datetime-local"
                id="meeting-time"
                v-model="newData.Event_startTime"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                required
              />
            </div>
            <div>
              <label
                for="category"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Category</label
              >
              <select
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                v-model="newData.Event_category"
                disabled
              >
                <option value="">Select a Category</option>
                <option
                  v-for="category in categorys"
                  v-bind:value="{
                    Event_category_id: category.Event_category_id,
                    Event_category_name: category.Event_category_name,
                    Event_category_description: category.Event_category_description,
                    Event_duration: category.Event_duration,
                  }"
                  :key="category.Event_category_id"
                >
                  {{ category.Event_category_name }}
                </option>
              </select>
            </div>

            <div>
              <label
                for="duration"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Duration
              </label>
              <input
                type="number"
                id="Duration"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="Duration(mins)"
                v-model="newData.Event_category.Event_duration"
                disabled
              />
            </div>
            <div>
              <label
                for="note"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >Note</label
              >
              <textarea
                v-model="newData.Event_notes"
                maxlength="500"
                class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-orange-600 focus:outline-none"
                placeholder="Add your note ..."
              ></textarea>
            </div>
            <br />
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

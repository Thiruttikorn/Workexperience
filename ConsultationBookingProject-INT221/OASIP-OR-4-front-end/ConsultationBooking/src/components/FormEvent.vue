<script>
import useVuelidate from '@vuelidate/core'
import { required, email, maxLength } from '@vuelidate/validators'
export default {
  setup() {
    return { v$: useVuelidate() }
  },
  data() {
    return {
      categorys: [],
      booking_id: 0,
      booking_name: '',
      booking_email: '',
      startDateTime: '',
      Event_notes: null,
      category: ''
    }
  },
  validations() {
    return {
      booking_name: { required, maxLength: maxLength(100) },
      booking_email: { required, email, maxLength: maxLength(100) },
      Event_notes: { maxLength: maxLength(500) },
      startDateTime: { required },
      category: { required }
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
  },
  methods: {
    async submit() {
      const result = await this.v$.$validate()
      if (!result) {
        // notify user form is invalid
        return false
      }
      // perform async actions
    },
    createClick() {
      if (
        this.booking_name != '' &&
        this.booking_email != '' &&
        this.startDateTime != '' &&
        this.category != ''
      ) {
        alert("create")
        let data = {
          Booking_id: this.booking_id,
          Booking_name: this.booking_name,
          Booking_email: this.booking_email,
          Event_startTime: this.startDateTime,
          Event_notes: this.notes,
          Event_category: this.category
        }
        fetch(`https://${import.meta.env.VITE_API}/events`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
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
            this.$emit('addEvent')
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
      this.booking_id = ''
      this.booking_name = ''
      this.booking_email = ''
      this.startDateTime = ''
      this.notes = ''
      this.category = ''
    }
  }
}
</script>
<template>
  <div>
    <div
      class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
      id="addEvent"
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
              Add Event Platform
            </h3>
            <form
              class="needs-validation space-y-6"
              @submit.prevent="submitForm"
              novalidate
            >
              <div>
                <label
                  for="bname"
                  :class="{ error: v$.booking_name.$errors.length }"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >Name<span class="text-danger">*</span></label
                >
                <input
                  required
                  type="text"
                  id="bname"
                  name="bname"
                  v-model="v$.booking_name.$model"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Enter your name"
                />
              </div>
              <div
                class="input-errors"
                v-for="(error, index) of v$.booking_name.$errors"
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
                  :class="{ error: v$.booking_email.$errors.length }"
                  >Your email<span class="text-danger">*</span></label
                >
                <input
                  required
                  type="email"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Enter your email"
                  v-model="v$.booking_email.$model"
                />
                <div
                  class="input-errors"
                  v-for="(error, index) of v$.booking_email.$errors"
                  :key="index"
                >
                  <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                  </div>
                </div>
              </div>
              <div>
                <label
                  for="dateTime"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >Date/Time<span class="text-danger">*</span></label
                >
                <input
                  required
                  type="datetime-local"
                  id="dateTime"
                  name="dateTime"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  v-model="v$.startDateTime.$model"
                />
                <div
                  class="input-errors"
                  v-for="(error, index) of v$.startDateTime.$errors"
                  :key="index"
                >
                  <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                  </div>
                </div>
              </div>
              <div>
                <label
                  for="category"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >Category<span class="text-danger">*</span></label
                >
                <select
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  v-model="v$.category.$model"
                >
                  <option value="">Select a Category</option>
                  <option
                    v-for="category in categorys"
                    v-bind:value="{
                      Event_category_id: category.Event_category_id,
                      Event_category_name: category.Event_category_name,
                      Event_duration: category.Event_duration,
                      Event_category_description:
                        category.Event_category_description
                    }"
                    :key="category.Event_category_id"
                  >
                    {{ category.Event_category_name }}
                  </option>
                </select>
                <div
                  class="input-errors"
                  v-for="(error, index) of v$.category.$errors"
                  :key="index"
                >
                  <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
                  </div>
                </div>
              </div>

              <div>
                <label
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >Duration</label
                >
                <input
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Duration(mins)"
                  v-bind:value="category.Event_duration"
                  disabled
                />
              </div>
              <div>
                <label
                  for="note"
                  :class="{ error: v$.Event_notes.$errors.length }"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >Note</label
                >
                <textarea
                  v-model="v$.Event_notes.$model"
                  name="note"
                  class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-orange-600 focus:outline-none"
                  placeholder="Add your note ..."
                ></textarea>
                <div
                  class="input-errors"
                  v-for="(error, index) of v$.Event_notes.$errors"
                  :key="index"
                >
                  <div class="error-msg text-red-600 text-xs">
                    {{ error.$message }}
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

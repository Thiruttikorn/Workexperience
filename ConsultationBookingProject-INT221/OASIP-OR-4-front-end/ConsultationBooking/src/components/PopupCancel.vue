<script>
export default {
  name: 'PopupCancel',
  props: {
    id: Number,
    Booking_id: Number
  },
  methods: {
    DeleteCilck() {
      fetch(`https://${import.meta.env.VITE_API}/events/` + this.Booking_id, {
        method: 'DELETE'
      })
        .then((res) => res.json())
        .then((res) => alert(res))
        .catch((reason) => alert(reason))
        .then(() => this.$emit('deleteEvent', this.id))
    }
  }
}
</script>
<template>
  <div>
    <div
      class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
      v-bind:id="'popupCancel-' + id"
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
          <div class="p-6 text-center">
            <svg
              class="mx-auto mb-4 w-14 h-14 text-gray-400 dark:text-gray-200"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
            <h3
              class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400"
            >
              Are you sure you want to delete this event?
            </h3>

            <button
              type="button"
              class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center mr-2"
              data-bs-dismiss="modal"
              data-modal-toggle="popup-cancel"
              @click="DeleteCilck"
            >
              Yes, I'm sure
            </button>

            <button
              type="button"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
              data-bs-dismiss="modal"
              data-modal-toggle="popup-cancel"
            >
              No, cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>

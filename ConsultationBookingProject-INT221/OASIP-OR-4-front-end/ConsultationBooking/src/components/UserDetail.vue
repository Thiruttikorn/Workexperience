<script>
import moment from 'moment'
export default {
  name: 'UserDetail',
  props: {
    id: Number,
    name: String,
    email: String,
    role: String,
    createdOn: String,
    updateOn: String,

},
methods: {}
}
</script>

<template>
  <div>
    <div
      class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
      v-bind:id="'UserDetails-' + id"
      tabindex="-1"
      aria-labelledby="ModalCenterTitle"
      aria-modal="true"
      role="dialog"
    >
      <div
        class="modal-dialog modal-dialog-centered relative w-auto pointer-events-none"
      >
        <div
          class="modal-content border-none shadow-lg relative w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
        >
          <div
            class="modal-header items-start justify-between  p-4 rounded-t border-b border-gray-200"
          >
            <div>
              <h5
                class="text-xl font-medium leading-normal text-gray-800"
                id="HeadUsersdetail"
              >
                Event user Detail
              </h5>
            </div>

            <div class="scroll modal-body relative p-4">
              {{ name }} <br />
              {{ email }} <br />
              {{ role }} <br />
              {{ createdOn }} <br />
              {{ updateOn }}  <br />
             
            </div>
            <div>
              <button
                type="button"
                class="inline-block px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
                data-bs-dismiss="modal"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
 div.scroll {
        width: 600px;
        height: 150px;
        overflow: auto;
            }
</style>

<script setup>
import { ref, computed } from "vue";
const props = defineProps({
  students: {
    type: Array,
  },
});
console.log(props.students);
</script>

<template>
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div
        class="flex flex-wrap w-full mb-20 flex-col items-center text-center"
      >
        <h1
          class="sm:text-3xl text-2xl font-medium title-font mb-2 text-gray-900"
        >
          About Team
        </h1>
      </div>
      <div class="flex flex-wrap -m-4">
        <div
          v-for="(student, index) of students"
          :key="index"
          class="xl:w-1/3 md:w-1/2 p-4"
        >
          <div class="border border-gray-200 p-6 rounded-lg">
            <div
              class="w-10 h-10 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 mb-4"
            >
              <svg
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                class="w-6 h-6"
                viewBox="0 0 24 24"
              >
                <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <h2 class="text-lg text-gray-900 font-medium title-font mb-2">
              {{ student.id }}
            </h2>
            <p class="leading-relaxed text-base">
              {{ student.fullName }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style></style>

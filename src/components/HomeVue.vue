<template>
  <p class="text-white text-left text-h5 q-pa-lg">Привет, {{ firstname }}</p>
  <HomeSlide />
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useAuthStore } from 'src/stores/auth'
import HomeSlide from './HomeSlide.vue'

const authStore = useAuthStore()

const firstname = ref<string>()

onMounted(() => {
  firstname.value = authStore.user?.firstName
  console.log(firstname.value)
})

</script>
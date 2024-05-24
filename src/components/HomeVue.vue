<template>
  <p class="text-white text-left text-h5 q-pa-lg">Привет, {{ firstname }}</p>
  <HomeSlide />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useAuthStore } from 'src/stores/auth'
import HomeSlide from './HomeSlide.vue'

const authStore = useAuthStore()

const firstname = computed(() => authStore.user?.firstName)

</script>
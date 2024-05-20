<template>
  <q-page class="row">
    <HomeVue />
  </q-page>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router';
import HomeVue from 'src/components/HomeVue.vue';

const router = useRouter()



</script>

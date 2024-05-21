<template>
  <q-layout
    view="hhh lpR fFf"
    v-if="mediaIsPhone"
  >
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
  <q-layout
    view="lHh Lpr lFf"
    v-else
  >
    <q-page-container>
      <NoMobile />
    </q-page-container>
  </q-layout>
</template>

<script setup lang='ts'>
import { ref, onMounted } from 'vue';

import NoMobile from 'src/components/NoMobile.vue';

const mediaIsPhone = ref<boolean>()

onMounted(() => {
  const mediaQuery = window.matchMedia('(max-width: 480px)');
  mediaQuery.addListener((event) => {
    mediaIsPhone.value = event.matches
  });
})
</script>
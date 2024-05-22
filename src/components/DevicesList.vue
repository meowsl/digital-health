<template>
  <div
    class="device-list"
    style="width: 100%;"
  >
    <div class="row q-pa-lg">
      <div class="col-12">
        <p class="text-white text-left text-h5 q-pb-lg">Устройства</p>
      </div>
    </div>
    <div class="symptom-list__tooltip">Добавить устройство</div>
    <q-btn
      class="symptom-list__btn"
      color="white"
      size="lg"
      round
      @click="asignDevice"
    >
      <q-icon
        name="add"
        color="deep-purple-9"
        size="xl"
      />
    </q-btn>

  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue'

const asignDevice = () => {
  // реализация добавления симптома
}
</script>

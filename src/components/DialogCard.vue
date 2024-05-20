<template>
  <div class="row justify-between">
    <div
      class="col-12 row q-pa-md text-white text-left"
      style="background-color: rgba(230, 230, 230, 45%); border-radius: 15px;"
    >
      <div
        class="col-8"
        style="font-size: 20px; font-family: 'Inter-Light';"
      >
        <p>Всего шагов</p>
        <p><span style="font-size: 32px; font-family: 'Inter-Bold';">78859</span> шагов</p>
      </div>
      <div class="col-4 row justify-center">
        <q-avatar size="80px">
          <img :src="ExampleCircle">
        </q-avatar>
      </div>
    </div>
    <div
      class="col-6 q-pa-md q-mt-md text-left"
      style="background-color: rgba(230, 230, 230, 45%); border-radius: 15px; font-size: 20px; font-family: 'Inter-Light'; max-width: 11rem;"
    >
      <p>Дистанция</p>
      <p><span style="font-size: 32px; font-family: 'Inter-Bold';">39</span> км</p>
    </div>
    <div
      class="col-6 q-pa-md q-mt-md text-left"
      style="background-color: rgba(230, 230, 230, 45%); border-radius: 15px; font-size: 20px; font-family: 'Inter-Light'; max-width: 11rem;"
    >
      <p>Калории</p>
      <p><span style="font-size: 32px; font-family: 'Inter-Bold';">3154</span> ккал</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import ExampleCircle from "images/examples/circular_progress.svg"
</script>
<template>
  <div
    class="symptom-list"
    style="width: 100%;"
  >
    <div class="row q-pa-lg">
      <div class="col-12">
        <p class="text-white text-left text-h5 q-pb-lg">Симптомы</p>
        <div class="row justify-between">
          <CalendarRow theme="symptom" />
        </div>
      </div>
      <div class="col-12 symptom-list__feeling">
        <p class="feeling-title">Оцените свое самочувствие</p>
        <q-rating
          v-model="feelingModel"
          size="3.5em"
          :max="10"
          color="deep-purple-9"
        >
          <template v-slot:left-icon>
            <q-icon :name="icons[0]" />
          </template>
          <template v-slot:right-icon>
            <q-icon :name="icons[1]" />
          </template>
          <template v-slot:label="{ index }">
            <div v-if="index > 1 && index < 10">
              {{ index }}
            </div>
          </template>
        </q-rating>
      </div>
    </div>
    <div class="symptom-list__tooltip">Добавить симптом</div>
    <q-btn
      class="symptom-list__btn"
      color="white"
      size="lg"
      round
      @click="addSymptom"
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
import CalendarRow from './CalendarRow.vue'
import {
  mdiEmoticonSadOutline,
  mdiEmoticonHappyOutline
} from '@quasar/extras/mdi-v6'

const feelingModel = ref<number>(5)

const icons = ref([
  mdiEmoticonSadOutline,
  mdiEmoticonHappyOutline
])

const addSymptom = () => {
  // реализация добавления симптома
}
</script>

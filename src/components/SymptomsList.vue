<template>
  <div
    class="symptom-list"
    style="width: 100%;"
  >
    <div class="row q-pa-lg">
      <div class="col-12">
        <p class="text-white text-left text-h5 q-pb-lg q-px-md">Симптомы</p>
        <div class="row justify-between">
          <CalendarRow theme="symptom" />
        </div>
      </div>
      <div class="col-12 column items-center symptom-list__feeling q-mt-xl">
        <p class="feeling-title text-center text-h6 text-white">Оцените свое самочувствие</p>
        <q-rating
          class="q-mt-sm"
          v-model="feelingModel"
          size="3.5em"
          :max="5"
          color="white"
          :icon="icons"
        />
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
import { ref, computed } from 'vue'
import CalendarRow from './CalendarRow.vue'

const feelingModel = ref<number>(5)

const icons = ref([
  'sentiment_very_dissatisfied',
  'sentiment_dissatisfied',
  'sentiment_neutral',
  'sentiment_satisfied',
  'sentiment_very_satisfied'
])

const addSymptom = () => {
  // реализация добавления симптома
}
</script>

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
      <div class="col-12 symptom-list__feeling q-mt-xl">
        <p class="feeling-title text-center text-h6 text-white">Оцените свое самочувствие</p>
        <q-rating
          class="q-mt-sm"
          v-model="feelingModel"
          size="3.5em"
          :max="1"
          color="deep-purple-9"
          :icon="getIcon"
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
import { biEmojiFrown, biEmojiNeutral } from '@quasar/extras/bootstrap-icons'

const feelingModel = ref<number>(5)

// const icons = ref([
//   biBugFill,
//   // Icon2,
//   // Icon3,
//   // Icon4,
//   // Icon5,
//   // Icon6,
//   // Icon7,
//   // Icon8,
//   // Icon9,
//   // HappyFace
// ])

const getIcon = computed(() => {
  if (feelingModel.value <= 1) {
    return biEmojiFrown
  } else if (feelingModel.value === 2 || feelingModel.value === 3) {
    return biEmojiNeutral
  }
})

const addSymptom = () => {
  // реализация добавления симптома
}
</script>

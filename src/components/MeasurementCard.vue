<template>
  <q-card
    class="measurements-card"
    @click="showDialog = true"
    :style="{ background: bgColor }"
  >
    <q-card-section class="measurements-card__title row items-center">
      <img
        class="title-icon"
        :src="PulseIcon"
      >
      <p
        class="title-text text-h5 q-ma-none q-ml-sm"
        :style="{ color: textColor }"
      >Пульс</p>
    </q-card-section>
    <q-card-section class="measurements-card__graph q-pa-none">
      <LineChart
        :chart-data="chartData"
        :options="chartOptions"
        :height="150"
        style="max-height: 150px; cursor: pointer;"
      />
    </q-card-section>
    <q-card-section class="measurements-card__indicator row items-center">
      <p
        class="number"
        :style="{ color: textColor }"
      >74</p>
      <p
        class="system q-ml-sm"
        :style="{ color: textColor }"
      >удара в секунду</p>
    </q-card-section>
  </q-card>
  <q-dialog
    class="dialog"
    v-model="showDialog"
    position="bottom"
  >
    <q-card
      class="dialog-card justify-center"
      style="border-radius: 50px 50px 0 0; background-color: rgba(73, 42, 79, 15%); background-color: #D6D0E8;"
    >
      <q-card-section>
        <div class="dialog-card__title text-h5 text-center">пульс</div>
      </q-card-section>
      <q-card-section class="q-py-none">
        <q-tabs
          v-model="tab"
          align="justify"
          narrow-indicator
          class="dialog-card__tabs q-mb-lg"
        >
          <q-tab
            class="dialog-card__tabs"
            name="day"
            label="Д"
          />
          <q-tab
            class=""
            name="week"
            label="Н"
          />
          <q-tab
            class=""
            name="mounth"
            label="Месяц"
          />
          <q-tab
            class=""
            name="year"
            label="Г"
          />
        </q-tabs>
      </q-card-section>
      <q-card-section class="dialog-card__tab-content q-pt-none">
        <q-tab-panels
          v-model="tab"
          transition-prev="scale"
          transition-next="scale"
          class="text-white text-center"
        >
          <q-tab-panel name="day">
            <LineChart
              :chart-data="chartData"
              :options="chartOptions"
              :height="150"
              style="max-height: 150px; cursor: pointer;"
            />
            <DialogCard />
          </q-tab-panel>
          <q-tab-panel name="week">
            <LineChart
              :chart-data="chartData"
              :options="chartOptions"
              :height="150"
              style="max-height: 150px; cursor: pointer;"
            />
            <DialogCard />
          </q-tab-panel>
          <q-tab-panel name="mounth">
            <LineChart
              :chart-data="chartData"
              :options="chartOptions"
              :height="150"
              style="max-height: 150px; cursor: pointer;"
            />
            <DialogCard />
          </q-tab-panel>
          <q-tab-panel name="year">
            <LineChart
              :chart-data="chartData"
              :options="chartOptions"
              :height="150"
              style="max-height: 150px; cursor: pointer;"
            />
            <DialogCard />
          </q-tab-panel>
        </q-tab-panels>
      </q-card-section>
      <q-card-section>

      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import PulseIcon from 'images/measurements/pulse.svg'
import DialogCard from './DialogCard.vue';
import { Chart, registerables } from 'chart.js';
import { LineChart } from 'vue-chart-3';

defineProps({
  bgColor: {
    type: String,
    default: 'linear-gradient(180deg, rgba(135, 107, 154, 1) 0%, rgba(115, 79, 131, 1) 100%)'
  },
  textColor: {
    type: String,
    default: 'white'
  }
});

const tab = ref('mounth')

const showDialog = ref(false);

Chart.register(...registerables);

const chartData = computed(() => ({
  labels: ['', '', '', '', '', ''],
  datasets: [{
    label: '',
    data: [12, 19, 3, 5, 2, 3],
    backgroundColor: '',
    borderColor: '#4c1a57',
    borderWidth: 3
  }]
}));

const chartOptions = {
  scales: {
    y: {
      beginAtZero: true,

    }
  }
};
</script>
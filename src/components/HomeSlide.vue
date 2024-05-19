<template>
  <div class="home-slide bg-white q-pa-lg">
    <div class="row">
      <div class="col-12 home-slide__calendar">
        <q-list class="calendar row justify-between">
          <q-item
            v-for="(day, index) in daysOfWeek"
            :key="index"
            clickable
            v-ripple
            :class="{ 'active-day': isToday(index) }"
          >
            <q-item-section class="col justify-center">
              <q-item-label class="calendar__weekday text-center">{{ day }}</q-item-label>
              <q-item-label
                class="calendar__dateday"
                caption
              >{{ formatDate(index) }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </div>
      <div class="col-12 home-slide__measurements q-mt-xl">
        <q-card class="measurements-card">
          <q-card-section class="measurements-card__title row items-center">
            <img
              class="title-icon"
              :src="PulseIcon"
            >
            <p class="title-text text-h5 text-white q-ma-none q-ml-sm">Пульс</p>
          </q-card-section>
          <q-card-section class="measurements-card__graph">
            <p>Тут очень крутое красивое графико</p>
          </q-card-section>
          <q-card-section class="measurements-card__indicator row text-white items-center">
            <p class="number">74</p>
            <p class="system q-ml-sm">удара в секунду</p>

          </q-card-section>
        </q-card>
      </div>
      <div class="col-12 home-slide__notifications q-mt-xl">
        <div class="row">
          <div class="col-12">
            <q-card class="notifications-card text-white q-pa-sm">
              <q-card-section class="notifications-card__title">
                <p class="title-text q-ma-none">
                  Рекомендации
                </p>
              </q-card-section>
              <q-card-section class="notifications-card__text q-py-none">
                Посетите врача
              </q-card-section>
              <q-card-section class="notifications-card__link text-right q-py-sm">
                <a
                  class="link text-right text-white"
                  href="#"
                >Перейти</a>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import PulseIcon from 'images/measurements/pulse.svg'

const daysOfWeek = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'];

const date = ref(new Date());

const formatDate = (index: number) => {
  const day = new Date(date.value);
  day.setDate(day.getDate() + index);
  return day.toLocaleDateString('ru-RU', { day: 'numeric' });
};

const isToday = (index: number) => {
  const today = new Date();
  const day = new Date(date.value);
  day.setDate(day.getDate() + index);
  return day.toDateString() === today.toDateString();
};
</script>
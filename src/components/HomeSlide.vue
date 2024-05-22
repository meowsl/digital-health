<template>
  <div class="home-slide bg-white q-pa-lg">
    <div class="row">
      <div class="col-12 home-slide__calendar">
        <q-list class="calendar row justify-between">
          <CalendarRow theme='home' />
        </q-list>
      </div>
      <div class="col-12 home-slide__measurements q-mt-xl">
        <MeasurementCard
          bgColor="linear-gradient(180deg, rgba(135, 107, 154, 1) 0%, rgba(115, 79, 131, 1) 100%)"
          text-color="white"
        />
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
import MeasurementCard from './MeasurementCard.vue';
import CalendarRow from './CalendarRow.vue';
</script>

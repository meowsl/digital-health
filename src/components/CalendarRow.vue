<template>
  <q-item
    v-for="(day, index) in daysOfWeek"
    :key="index"
    clickable
    v-ripple
    :class="{ 'active-day': isToday(index) }"
    :style="getDayStyles(index)"
  >
    <q-item-section class="col justify-center">
      <q-item-label
        class="calendar__weekday text-center"
        :style="getWeekdayStyles"
      >{{ day }}</q-item-label>
      <q-item-label
        class="calendar__dateday"
        caption
        :style="getDatedayStyles"
      >{{ formatDate(index) }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script setup lang="ts">
import { ref, computed, defineProps } from 'vue'


const props = defineProps({
  theme: {
    type: String,
    required: true,
  }
})

const { theme } = props

const getWeekdayStyles = computed(() => {
  if (theme === 'home') {
    return {
      color: '#989898',
      fontSize: '20px',
    }
  } else if (theme === 'symptom') {
    return {
      color: '#fff',
      fontSize: '20px',
    }
  }

  return {
    color: '#000',
    fontSize: '20px',
  }
})

const getDatedayStyles = computed(() => {
  if (theme === 'home') {
    return {
      color: '#6A6A6A',
      fontSize: '23px',
    }
  } else if (theme === 'symptom') {
    return {
      color: '#fff',
      fontSize: '23px',
    }
  }

  return {
    color: '#000',
    fontSize: '23px',
  }
})

const getDayStyles = (index: number) => {
  if (isToday(index)) {
    return {
      backgroundColor: '#CAC4DA',
      color: '#fff',
      borderRadius: '34px',
    }
  }
}

const daysOfWeek = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'];

const weekStart = ref(getWeekStart());

const formatDate = (index: number) => {
  const day = new Date(weekStart.value.getTime());
  day.setDate(day.getDate() + index);
  return day.toLocaleDateString('ru-RU', { day: 'numeric' });
};

const isToday = (index: number) => {
  const today = new Date();
  const day = new Date(weekStart.value.getTime());
  day.setDate(day.getDate() + index);
  return day.toDateString() === today.toDateString();
};

function getWeekStart() {
  const today = new Date();
  const dayOfWeek = today.getDay();
  const diff = dayOfWeek === 0 ? -6 : 1 - dayOfWeek;
  const weekStart = new Date(today.getTime() + diff * 24 * 60 * 60 * 1000);
  return weekStart;
}

</script>
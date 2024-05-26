<template>
  <div
    class="q-pa-lg column justify-center items-center"
    style="width:100%;"
  >

    <p class="text-h4 text-white q-mb-md">Здравствуйте, {{ firstname }}!</p>
    <p class="text-h6 text-white q-mb-md text-center">Добро пожаловать в демо версию! <br> Здесь Вы можете
      протестировать что-то</p>
    <q-form
      class="row items-center q-pb-md"
      @submit.prevent="sendMessage"
    >
      <q-input
        v-model="request"
        outlined
        type="text"
        placeholder="Текст запроса"
        lazy-rules
        color="purple"
        style="width: 23rem;"
      />
      <q-btn
        class="ws-button"
        round
        dense
        flat
        :ripple="false"
        color="white"
        icon="send"
        type="submit"
      />
    </q-form>
    <div
      class="row actions-button q-pb-md justify-between"
      style="width: 30rem;"
    >
      <q-btn
        class="devices-button q-"
        dense
        no-caps
        :ripple="false"
        color="purple"
        label="Устройства"
        @click="sendAction('devices')"
      />
      <q-btn
        class="imitation-steps-button q-"
        dense
        no-caps
        :ripple="false"
        color="purple"
        label="Имитация шагов"
        @click="sendAction('imitation-steps')"
      />
      <q-btn
        class="imitation-pulse-button q-"
        dense
        no-caps
        :ripple="false"
        color="purple"
        label="Имитация пульса"
        @click="sendAction('imitation-pulse')"
      />
      <q-btn
        class="steps-button q-"
        dense
        no-caps
        :ripple="false"
        color="purple"
        label="Шаги"
        @click="sendAction('steps')"
      />
      <q-btn
        class="pulse-butthon"
        dense
        no-caps
        :ripple="false"
        color="purple"
        label="Пульс"
        @click="sendAction('pulse')"
      />
    </div>
    <q-scroll-area
      ref="scrollAreaRef"
      class="messages"
    >
      <div
        v-for="(message, index) in messages"
        :key="index"
        :class="message.type"
      >
        <div class="message-content">{{ message.content }}</div>
      </div>
    </q-scroll-area>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, computed, nextTick } from 'vue'
import { useAuthStore } from 'src/stores/auth'
import { Message } from 'src/models'
import { QScrollArea } from 'quasar'

const authStore = useAuthStore()

const ws = ref<WebSocket | null>(null)

const request = ref('Привет')
const messages = ref<Message[]>([])

const firstname = computed(() => authStore.user?.firstName)

const scrollAreaRef = ref<QScrollArea | null>(null)

onMounted(() => {
  const user_id = localStorage.getItem('userId')
  ws.value = new WebSocket(`ws://localhost:8000/ws/${user_id}`)
  ws.value.onmessage = (event: MessageEvent) => {
    messages.value.push({ type: 'received', content: event.data })
    nextTick(() => {
      scrollToBottom()
    })
  }
})

const scrollToBottom = () => {
  console.log('scroll')
  if (scrollAreaRef.value) {
    const contentElement = scrollAreaRef.value.$el.querySelector('.q-scrollarea__content') as HTMLElement
    const totalHeight = contentElement?.scrollHeight
    scrollAreaRef.value.setScrollPosition('vertical', totalHeight)
  }
}

const sendMessage = () => {
  if (ws.value) {
    console.log(request.value)
    ws.value.send(request.value)
    messages.value.push({ type: 'sent', content: request.value })
    request.value = ''
  }
}

const sendAction = (message: string) => {
  if (ws.value) {
    ws.value.send(message)
    messages.value.push({ type: 'sent', content: message })
  }
}
</script>
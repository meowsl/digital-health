<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="header">
      <q-toolbar class="header__toolbar row justify-between q-pa-lg">
        <q-btn
          flat
          round
          dense
          icon="menu"
          class="q-mr-sm"
        />
        <q-avatar size="65px">
          <img :src="Placeholder">
        </q-avatar>
      </q-toolbar>

    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang='ts'>
import Placeholder from 'images/avatar_placeholder.png'
</script>

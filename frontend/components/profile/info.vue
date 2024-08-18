<template>
  <div class="UserProfile">
    <p class="UserProfile-name">{{ user?.name }}</p>
    <p class="UserProfile-info">Fecha de nacimiento: {{ user?.birthday }}</p>
    <p class="UserProfile-info">Dirección: {{ user?.address }}</p>
    <div
      v-for="(email, index) in user?.emails"
      :key="index"
      class="UserProfile-email"
    >
      <p>{{ email }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { ProfileI } from "~/interfaces/profile";

defineProps<{ user: ProfileI }>();
</script>

<style scope lang="sass">
.UserProfile
  max-width: 600px
  margin: 2rem auto
  padding: 2rem
  background-color: #ffffff
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)
  border-radius: 8px
  p
    font-size: 1rem
    color: #333
    margin-bottom: 1rem
  .UserProfile-name
    font-size: 1.5rem
    font-weight: 600
    margin-bottom: 1.5rem
    color: #007BFF
  .UserProfile-info
    font-size: 1rem
    font-weight: 500
    color: #666
  .UserProfile-email
    p
      font-size: 1rem
      color: #333
      margin-bottom: 0.5rem
</style>

<template>
  <header class="Header">
    <NuxtLink to="/gallery">
      <img src="/logo.png" alt="Logo" />
    </NuxtLink>
    <div class="Header-username">
      <NuxtLink :to="`/profile/${token.user?.username}`">
        @{{ token.user?.username }}
      </NuxtLink>
    </div>
  </header>
</template>

<script setup lang="ts">
const token = useTokenStore();
</script>

<style scope lang="sass">
.Header
  display: flex
  justify-content: space-between
  align-items: center
  padding: 1rem 2rem
  background-color: #ffffff
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)
  border-radius: 8px
  img
    max-height: 50px
  .Header-username
    font-size: 1.25rem
    color: #333
    a
      color: #007BFF
      text-decoration: none
      font-weight: 600
      &:hover
        text-decoration: underline
</style>

<template>
  <header class="Header">
    <NuxtLink to="/gallery">
      <img src="/logo.png" alt="Logo" />
    </NuxtLink>
    <div class="Header-username">
      <button class="Header-search" @click="showSearch = !showSearch">
        <IconSearch />
      </button>
      <NuxtLink :to="`/profile/${token.user?.username}`">
        @{{ token.user?.username }}
      </NuxtLink>
    </div>
    <Search v-if="showSearch" @close="showSearch = false" />
  </header>
</template>

<script setup lang="ts">
const token = useTokenStore();
const showSearch = ref(false);
</script>

<style scoped lang="sass">
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
    display: flex
    align-items: center
    gap: 1rem
    font-size: 1.25rem
    color: #333

    a
      color: #007BFF
      text-decoration: none
      font-weight: 600
      &:hover
        text-decoration: underline

    .Header-search
      display: flex
      align-items: center
      justify-content: center
      width: 35px
      height: 35px
      border-radius: 50%
      background-color: #f0f0f0
      transition: background-color 0.3s ease
      svg
        fill: #007BFF
        width: 30px
        height: 30px
      &:hover
        background-color: #e0e0e0
</style>

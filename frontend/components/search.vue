<template>
  <div class="Modal">
    <div class="Modal-content">
      <button class="Modal-close" @click="$emit('close')">x</button>
      <div class="Search">
        <div class="Search-input">
          <input type="text" placeholder="Buscar..." />
          <button><IconSearch /></button>
        </div>
        <div class="Search-users">
          <NuxtLink
            v-for="(user, index) in users"
            :to="`/profile/${user.username}`"
            :key="index"
          >
            {{ user.name }}
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const users = [
  { name: "John Doe", username: "jdoe" },
  { name: "Mary Miller", username: "mmiller88" },
];
</script>

<style scope lang="sass">
.Modal
  position: fixed
  top: 0
  left: 0
  width: 100%
  height: 100%
  background-color: rgba(0, 0, 0, 0.5)
  display: flex
  align-items: center
  justify-content: center
  z-index: 1000

  .Modal-content
    background-color: #fff
    padding: 2rem
    border-radius: 8px
    max-width: 500px
    width: 100%
    position: relative

    .Modal-close
      position: absolute
      top: 0px
      right: 10px
      background: none
      border: none
      font-size: 1.5rem
      cursor: pointer

.Search
  display: flex
  flex-direction: column
  gap: 1rem

  .Search-input
    display: flex
    gap: 0.5rem

    input
      flex-grow: 1
      padding: 0.75rem
      border: 1px solid #ccc
      border-radius: 4px
      font-size: 1rem

    button
      background-color: #007BFF
      color: white
      padding: 0.75rem
      border: none
      border-radius: 4px
      cursor: pointer
      transition: background-color 0.3s ease
      svg
        fill: #fff
        width: 20px
        height: 20px
      &:hover
        background-color: #0056b3

  .Search-users
    display: flex
    flex-direction: column
    gap: 0.5rem
    max-height: 300px
    overflow-y: auto

    a
      color: #007BFF
      text-decoration: none
      padding: 0.5rem
      border-radius: 4px
      transition: background-color 0.3s ease
      &:hover
        background-color: #f0f0f0
</style>

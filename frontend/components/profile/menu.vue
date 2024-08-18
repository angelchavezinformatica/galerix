<template>
  <div class="Menu">
    <button class="Menu-button" @click="isModalAddPhotoOpen = true">
      Añadir Foto
    </button>
    <button class="Menu-button" @click="isModalCreateGaleryOpen = true">
      Crear Galería
    </button>
    <button v-if="showCreatePage" class="Menu-button">Crear Página</button>

    <ProfileMenuAddPhoto
      v-if="isModalAddPhotoOpen"
      @close="isModalAddPhotoOpen = false"
    />
    <ProfileMenuCreateGalery
      v-if="isModalCreateGaleryOpen"
      @close="isModalCreateGaleryOpen = false"
    />
  </div>
</template>

<script setup lang="ts">
const isModalAddPhotoOpen = ref(false);
const isModalCreateGaleryOpen = ref(false);
const showCreatePage = true;
</script>

<style scope lang="sass">
.Menu
  display: flex
  justify-content: space-around
  gap: 1rem
  margin-top: 1.5rem
  padding: 1rem
  background-color: #f9f9f9
  border-radius: 8px
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)
  .Menu-button
    background-color: #007BFF
    color: #fff
    padding: 0.75rem 1.5rem
    font-size: 1rem
    border: none
    border-radius: 4px
    cursor: pointer
    transition: background-color 0.3s ease
    &:hover
      background-color: #0056b3
</style>

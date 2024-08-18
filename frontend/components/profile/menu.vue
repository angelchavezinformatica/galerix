<template>
  <div class="Menu">
    <button class="Menu-button" @click="isModalAddPhotoOpen = true">
      Añadir Foto
    </button>
    <button class="Menu-button" @click="isModalCreateGaleryOpen = true">
      Crear Galería
    </button>
    <button
      v-show="!hasPage"
      class="Menu-button"
      @click="isModalCreatePageOpen = true"
    >
      Crear Página
    </button>
    <NuxtLink :to="`/page/${username}`" v-show="hasPage" class="Menu-button">
      Ir a la Página
    </NuxtLink>

    <ProfileMenuAddPhoto
      v-if="isModalAddPhotoOpen"
      @close="isModalAddPhotoOpen = false"
    />
    <ProfileMenuCreateGalery
      v-if="isModalCreateGaleryOpen"
      @close="isModalCreateGaleryOpen = false"
    />
    <ProfileMenuCreatePage
      v-if="isModalCreatePageOpen"
      @close="isModalCreatePageOpen = false"
    />
  </div>
</template>

<script setup lang="ts">
const token = useTokenStore();

const isModalAddPhotoOpen = ref(false);
const isModalCreateGaleryOpen = ref(false);
const isModalCreatePageOpen = ref(false);
const hasPage = computed(() => token.user?.page || false);

const {
  params: { username },
} = useRoute();
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
    text-decoration: none
    font-family: 'Arial'
    &:hover
      background-color: #0056b3
</style>

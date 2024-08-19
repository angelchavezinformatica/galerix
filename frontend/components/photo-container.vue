<template>
  <div v-show="photos === null" class="loading">
    <p>Cargando...</p>
  </div>
  <div v-show="photos !== null && !photos.length" class="no-photos">
    <p>Aún no se han publicado fotos.</p>
  </div>
  <div v-show="photos !== null && photos.length" class="photos-container">
    <Photo v-for="photo in photos" :key="photo.path" :photo="photo" />
  </div>
</template>

<script setup lang="ts">
import type { PhotoI } from "~/interfaces/photo";

defineProps<{ photos: PhotoI[] | null }>();
</script>

<style scoped lang="sass">
.loading,
.no-photos
  text-align: center
  margin: 2rem 0
  font-size: 1.2rem
  color: #666

.photos-container
  display: flex
  flex-direction: column
  align-items: center
  gap: 1.5rem
</style>

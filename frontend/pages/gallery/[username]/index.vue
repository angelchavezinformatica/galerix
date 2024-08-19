<template>
  <h1 class="galleries-title">Galerías de {{ username }}</h1>
  <div class="galleries-container">
    <div class="gallery" v-for="gallery in data" :key="gallery.id">
      <NuxtLink class="gallery-link" :to="`/gallery/${username}/${gallery.id}`">
        {{ gallery.name }}
      </NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { galleryURL } from "~/config/api";
import type { GalleryI } from "~/interfaces/profile";
import { useProtectedFetchJSON } from "~/services/api";

definePageMeta({ layout: "protected" });

const { data, request } = useProtectedFetchJSON<GalleryI[]>();

const {
  params: { username },
} = useRoute();

onMounted(async () => {
  await request(`${galleryURL}/${username}`);
});
</script>

<style scoped lang="sass">
.galleries-title
  font-size: 2rem
  font-weight: bold
  margin-bottom: 1.5rem
  text-align: center
  color: #333

.galleries-container
  display: flex
  flex-wrap: wrap
  gap: 1rem
  justify-content: center
  margin-top: 2rem

.gallery
  background-color: #f9f9f9
  padding: 1rem
  border-radius: 8px
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1)
  transition: transform 0.3s ease-in-out
  &:hover
    transform: scale(1.05)

.gallery-link
  text-decoration: none
  color: #007bff
  font-size: 1.2rem
  font-weight: 500
  &:hover
    text-decoration: underline
</style>

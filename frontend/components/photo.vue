<template>
  <div :key="photo.path" class="photo-card">
    <div class="photo-header">
      <img
        :src="`${base}/media/${photo.path}`"
        alt="Foto"
        class="photo-image"
      />
    </div>
    <div class="photo-body">
      <h3 class="photo-title">{{ photo.title }}</h3>
      <p class="photo-description">{{ photo.description }}</p>
    </div>
    <div class="photo-footer">
      <span class="photo-timestamp">{{ formatDate(photo.timestamp) }}</span>
      <span class="photo-username">
        Publicado por
        <NuxtLink :to="`/profile/${photo.username}`">
          {{ photo.name }}
        </NuxtLink>
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ photo: PhotoI }>();

import { base } from "~/config/api";
import type { PhotoI } from "~/interfaces/photo";

const formatDate = (timestamp: string) => {
  const date = new Date(timestamp);
  return date.toLocaleDateString() + " " + date.toLocaleTimeString();
};
</script>

<style scoped lang="sass">
.photo-card
  background-color: #fff
  border-radius: 8px
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)
  overflow: hidden
  max-width: 400px
  width: 100%

.photo-header
  width: 100%
  max-height: 300px
  overflow: hidden

.photo-image
  width: 100%
  object-fit: cover

.photo-body
  padding: 1rem

.photo-title
  font-size: 1.4rem
  font-weight: bold
  color: #333
  margin-bottom: 0.5rem

.photo-description
  font-size: 1rem
  color: #555

.photo-footer
  display: flex
  justify-content: space-between
  padding: 0.5rem 1rem
  background-color: #f9f9f9
  font-size: 0.9rem
  color: #888
  .photo-username a
    color: #888
</style>

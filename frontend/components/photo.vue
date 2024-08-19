<template>
  <div :key="photo.path" class="photo-card">
    <div class="photo-header">
      <img
        :src="`${base}/media/${photo.path}`"
        alt="Foto"
        class="photo-image"
      />
      <button @click="toggleFavorite" class="favorite-button">
        <span v-if="photo.isfavorite">★</span>
        <span v-else>☆</span>
      </button>
    </div>
    <div class="photo-body">
      <h3 class="photo-title">{{ photo.title }}</h3>
      <p class="photo-description">{{ photo.description }}</p>
      <RatingStars :score="photo.userscore" @rate="ratePhoto" />
      <p class="photo-score">Puntaje: {{ photo.score }} / 5</p>
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
import { base, RatePhoto, ToggleFavoritePhoto } from "~/config/api";
import type { PhotoI } from "~/interfaces/photo";
import { useProtectedFetchJSON } from "~/services/api";

const props = defineProps<{ photo: PhotoI }>();

const { token } = useTokenStore();
const { getData: getPhotos } = usePhotoStore();
const { request } = useProtectedFetchJSON();

const formatDate = (timestamp: string) => {
  const date = new Date(timestamp);
  return date.toLocaleDateString() + " " + date.toLocaleTimeString();
};

const ratePhoto = async (rating: number) => {
  await request(RatePhoto, {
    method: "PUT",
    body: { photoid: props.photo.id, rate: rating },
    response: false,
  });
  await getPhotos(token || undefined);
};

const toggleFavorite = async () => {
  await request(ToggleFavoritePhoto, {
    method: "PUT",
    body: { photoid: props.photo.id },
    response: false,
  });
  await getPhotos(token || undefined);
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
  position: relative

.photo-header
  position: relative
  width: 100%
  max-height: 300px
  overflow: hidden

.photo-image
  width: 100%
  object-fit: cover

.favorite-button
  position: absolute
  top: 10px
  right: 10px
  background: rgba(0, 0, 0, 0.5)
  border: none
  border-radius: 50%
  font-size: 24px
  color: #ffd700
  cursor: pointer
  display: none
  align-items: center
  justify-content: center
  padding: 5px
  transition: background 0.3s
  width: 40px
  height: 40px
  text-align: center
  line-height: 40px
  &:hover
    background: rgba(0, 0, 0, 0.7)

.photo-card:hover .favorite-button
  display: flex

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
  margin-bottom: 0.5rem

.photo-score
  display: block
  font-size: 1rem
  color: #444
  font-weight: bold
  margin-bottom: 0.5rem

.photo-footer
  display: flex
  justify-content: space-between
  align-items: center
  padding: 0.5rem 1rem
  background-color: #f9f9f9
  font-size: 0.9rem
  color: #888
  .photo-username a
    color: #888
</style>

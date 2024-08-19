<template>
  <ProfileInfo :user="_user" v-if="_user" />
  <ProfileMenu v-if="username === user.user?.username" />
  <div class="filters">
    <button
      @click="filter = 'all'"
      :class="{ active: filter === 'all' }"
      class="filter-button"
    >
      Todos
    </button>
    <button
      @click="filter = 'favorites'"
      :class="{ active: filter === 'favorites' }"
      class="filter-button"
    >
      Favoritos
    </button>
    <NuxtLink :to="`/gallery/${username}`" class="gallery-link">
      Galerías
    </NuxtLink>
  </div>
  <PhotoContainer :photos="filtered" />
</template>

<script setup lang="ts">
import { profileURL } from "~/config/api";
import type { PhotoI } from "~/interfaces/photo";
import type { ProfileI } from "~/interfaces/profile";
import { useProtectedFetchJSON } from "~/services/api";

definePageMeta({ layout: "protected" });

const user = useTokenStore();
const photos = usePhotoStore();
const { data, request } = useProtectedFetchJSON<ProfileI>();

const _user: Ref<ProfileI | null> = ref(null);
const filter: Ref<"all" | "favorites"> = ref("all");

const filtered: ComputedRef<PhotoI[] | null> = computed(() => {
  if (_user.value === null) return [];
  if (filter.value === "all")
    return (
      photos.photos?.filter(
        (photo: PhotoI) => photo.username === _user.value?.username
      ) || []
    );
  return (
    photos.photos?.filter(
      (photo: PhotoI) =>
        photo.username === _user.value?.username && photo.isfavorite
    ) || []
  );
});

const {
  params: { username },
} = useRoute();

onMounted(async () => {
  if (username === user.user?.username) {
    _user.value = user.user;
    return;
  }
  await request(`${profileURL}/${username}`);
  _user.value = data.value;
});
</script>

<style scoped lang="sass">
.filters
  display: flex
  justify-content: center
  margin: 2.5rem 0 1.5rem

.filter-button
  padding: 10px 20px
  margin: 0 10px
  border: none
  border-radius: 5px
  background-color: #f0f0f0
  cursor: pointer
  transition: background-color 0.3s
  font-size: 16px
  &:hover
    background-color: #e0e0e0
  &.active
    background-color: #d0d0d0
    font-weight: bold

.gallery-link
  padding: 10px 20px
  border-radius: 5px
  background-color: #4caf50
  color: white
  text-decoration: none
  margin-left: 10px
  transition: background-color 0.3s
  &:hover
    background-color: #45a049
</style>

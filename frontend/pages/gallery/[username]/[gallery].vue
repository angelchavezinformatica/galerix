<template>
  <PhotoContainer :photos="data || null" />
</template>

<script setup lang="ts">
import { galleryURL } from "~/config/api";
import type { PhotoI } from "~/interfaces/photo";
import { useProtectedFetchJSON } from "~/services/api";

definePageMeta({ layout: "protected" });

const { data, request } = useProtectedFetchJSON<PhotoI[]>();

const {
  params: { username, gallery },
} = useRoute();

onMounted(async () => {
  await request(`${galleryURL}/${username}/${gallery}`);
});
</script>

<style scoped lang="sass"></style>

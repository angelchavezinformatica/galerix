<template>
  <PhotoContainer :photos="photos.photos" />
</template>

<script setup lang="ts">
definePageMeta({ layout: "protected" });

import { usePhotoStore } from "~/stores/photo";

const photos = usePhotoStore();
</script>

<style scoped lang="sass"></style>

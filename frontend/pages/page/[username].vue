<template>
  <h1>Username: {{ username }}</h1>
</template>

<script setup lang="ts">
definePageMeta({ layout: "protected" });

const {
  params: { username },
} = useRoute();
</script>

<style scoped lang="sass"></style>

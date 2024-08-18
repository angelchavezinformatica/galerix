<template>
  <NuxtLayout>
    <NuxtPage />
    <Toaster theme="dark" />
  </NuxtLayout>
</template>

<script setup lang="ts">
useHead({ title: "Galerix" });

import { Toaster } from "vue-sonner";

const { getToken } = useTokenStore();

callOnce(getToken);
</script>

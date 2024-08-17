<template>
  <NuxtLayout>
    <NuxtPage />
    <Toaster theme="dark" />
  </NuxtLayout>
</template>

<script setup lang="ts">
useHead({ title: "Galerix" });

import { Toaster } from "vue-sonner";
import { useToken } from "./stores/token";

const { getToken } = useToken();

callOnce(getToken);
</script>

<template>
  <slot v-if="token" />
</template>

<script setup lang="ts">
const { getToken, token } = useToken();
const router = useRouter();

callOnce(getToken);

if (!token) router.push("/");
</script>

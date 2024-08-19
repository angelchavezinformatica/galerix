<template>
  <ProtectedHeader v-if="token" />
  <main class="Main">
    <slot v-if="token" />
  </main>
</template>

<script setup lang="ts">
const { token } = useTokenStore();
const router = useRouter();

if (!token) router.push("/");
</script>

<style scoped lang="sass">
.Main
  margin-top: 6rem
</style>

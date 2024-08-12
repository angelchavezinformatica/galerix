<template>
  <slot v-if="user" />
</template>

<script setup lang="ts">
import { useUser } from "~/stores/user";

const { user } = useUser();
const router = useRouter();

if (!user) router.push("/");
</script>

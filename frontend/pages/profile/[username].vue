<template>
  <ProfileInfo :user="_user" v-if="_user" />
  <ProfileMenu v-if="username === user.user?.username" />
</template>

<script setup lang="ts">
import { profileURL } from "~/config/api";
import type { ProfileI } from "~/interfaces/profile";
import { useProtectedFetchJSON } from "~/services/api";

definePageMeta({ layout: "protected" });

const user = useTokenStore();
const { data, request } = useProtectedFetchJSON<ProfileI>();

let _user: Ref<ProfileI | null> = ref(null);

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

<style scoped lang="sass"></style>

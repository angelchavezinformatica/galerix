<template>
  <div class="UserProfile">
    <p class="UserProfile-name">{{ user?.name }}</p>
    <p v-if="user?.text && !isEditing">{{ user.text }}</p>

    <div class="UserProfile-text" v-if="username === token.user?.username">
      <textarea v-if="isEditing" v-model="newText"></textarea>

      <button @click="toggleEditing">
        {{
          isEditing ? "Guardar" : user?.text ? "Editar texto" : "Agregar texto"
        }}
      </button>
    </div>

    <p class="UserProfile-info">
      Número de fotos subidas: {{ user?.numphotos }}
    </p>
    <p class="UserProfile-info">Fecha de nacimiento: {{ user?.birthday }}</p>
    <p class="UserProfile-info">Dirección: {{ user?.address }}</p>

    <div
      v-for="(email, index) in user?.emails"
      :key="index"
      class="UserProfile-email"
    >
      <p>{{ email }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { UpdateTextUser } from "~/config/api";
import type { ProfileI } from "~/interfaces/profile";
import { useProtectedFetchJSON } from "~/services/api";

const { user } = defineProps<{ user: ProfileI }>();
const token = useTokenStore();
const { request } = useProtectedFetchJSON();

const {
  params: { username },
} = useRoute();

const newText = ref(user?.text || "");
const isEditing = ref(false);

const toggleEditing = async () => {
  if (isEditing.value && user) {
    user.text = newText.value;
    await request(UpdateTextUser, {
      method: "PATCH",
      body: { text: newText.value },
      response: false,
    });
    await token.getToken();
  }
  isEditing.value = !isEditing.value;
};
</script>

<style scoped lang="sass">
.UserProfile
  max-width: 600px
  margin: 2rem auto
  padding: 2rem
  background-color: #ffffff
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)
  border-radius: 8px
  p
    font-size: 1rem
    color: #333
    margin-bottom: 1rem
  .UserProfile-name
    font-size: 1.5rem
    font-weight: 600
    margin-bottom: 1rem
    color: #007BFF
  .UserProfile-info
    font-size: 1rem
    font-weight: 500
    color: #666
  .UserProfile-email
    p
      font-size: 1rem
      color: #333
      margin-bottom: 0.5rem
  .UserProfile-text
    margin-top: 1rem
    button
      margin-top: 0.5rem
      padding: 0.5rem 1rem
      font-size: 1rem
      color: white
      background-color: #007BFF
      border: none
      border-radius: 4px
      cursor: pointer
      &:hover
        background-color: #0056b3
    textarea
      width: 100%
      padding: 0.5rem
      font-size: 1rem
      border: 1px solid #ccc
      border-radius: 4px
      margin-top: 0.5rem
</style>

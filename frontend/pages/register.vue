<template>
  <AuthForm
    title="Bienvenido"
    submit-value="Registrarse"
    :disabled="disabled"
    @handle-submit="handleSubmit"
  >
    <div class="Form-input">
      <label for="name" class="Form-input-label">Nombre Completo</label>
      <input type="text" class="Form-input-entry" v-model="name" />
    </div>
    <div class="Form-input">
      <label for="username" class="Form-input-label">Nombre de Usuario</label>
      <input type="text" class="Form-input-entry" v-model="username" />
    </div>
    <div class="Form-input">
      <label for="password" class="Form-input-label">Contraseña</label>
      <input type="password" class="Form-input-entry" v-model="password" />
    </div>
    <div class="Form-input">
      <label for="birthday" class="Form-input-label">
        Fecha de Nacimiento
      </label>
      <input type="date" class="Form-input-entry" v-model="birthday" />
    </div>
    <div class="Form-input">
      <label for="address" class="Form-input-label">Dirección</label>
      <input type="text" class="Form-input-entry" v-model="address" />
    </div>

    <template v-slot:message>
      <p>¿Ya tiene una cuenta? <NuxtLink to="/">Inicie sesión</NuxtLink></p>
    </template>
  </AuthForm>
</template>

<script setup lang="ts">
import { usePageRegister } from "~/composables/pages/register";

const { address, birthday, disabled, handleSubmit, name, password, username } =
  usePageRegister();
</script>

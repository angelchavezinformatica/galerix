<template>
  <AuthForm
    title="Bienvenido"
    submitValue="Iniciar Sesión"
    :disabled="disabled"
    @handle-submit="handleSubmit"
  >
    <div class="Form-input">
      <label for="username" class="Form-input-label">Nombre de usuario</label>
      <input
        type="text"
        class="Form-input-entry"
        v-model="username"
        placeholder="Ingrese su usuario"
      />
    </div>
    <div class="Form-input">
      <label for="password" class="Form-input-label">Contraseña</label>
      <input
        type="password"
        class="Form-input-entry"
        v-model="password"
        placeholder="Ingrese su contraseña"
      />
    </div>

    <template v-slot:message>
      <p>
        ¿No tiene una cuenta?
        <NuxtLink to="/register">Cree una</NuxtLink>
      </p>
    </template>
  </AuthForm>
</template>

<script setup lang="ts">
import { useLogin } from "~/composables/pages/login";
const { disabled, handleSubmit, password, username } = useLogin();
</script>

<template>
  <AuthForm
    title="Bienvenido"
    submit-value="Registrarse"
    @handle-submit="handleSubmit"
  >
    <div class="Form-input">
      <label for="name" class="Form-input-label">Nombre completo</label>
      <input type="text" class="Form-input-entry" v-model="name" />
    </div>
    <div class="Form-input">
      <label for="username" class="Form-input-label">Nombre de usuario</label>
      <input type="text" class="Form-input-entry" v-model="username" />
    </div>
    <div class="Form-input">
      <label for="password" class="Form-input-label">Contraseña</label>
      <input type="password" class="Form-input-entry" v-model="password" />
    </div>
    <div class="Form-input">
      <label for="birthday" class="Form-input-label">
        Fecha de nacimiento
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
const username: Ref<string> = ref("");
const password: Ref<string> = ref("");
const name: Ref<string> = ref("");
const birthday: Ref<string> = ref("");
const address: Ref<string> = ref("");

const handleSubmit = () => {
  console.log({
    username: username.value,
    password: password.value,
    name: name.value,
    birthday: birthday.value,
    address: address.value,
  });
};
</script>

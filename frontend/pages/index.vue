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
import { toast } from "vue-sonner";
import { LoginUser } from "~/config/api";
import { fetchJSON } from "~/services/api";
import { useToken } from "~/stores/token";

const { updateToken } = useToken();

const username: Ref<string> = ref("");
const password: Ref<string> = ref("");

const disabled: ComputedRef<boolean> = computed(() =>
  Boolean(username.value && password.value)
);

const handleSubmit = () => {
  toast.promise(
    fetchJSON(LoginUser, {
      method: "POST",
      body: {
        username: username.value,
        password: password.value,
      },
    }),
    {
      loading: () => {
        password.value = "";
        return "Cargando...";
      },
      error: (data) => {
        if (data.status === 404) return "Usuario no encontrado.";
        if (data.status === 400) return "Credenciales invalidas.";
        return "Ocurrió un error al iniciar sesión.";
      },
      success: (data) => {
        data.json().then((value) => {
          updateToken(value.token);
        });
        return "Inicio de sesión valido.";
      },
    }
  );
};
</script>

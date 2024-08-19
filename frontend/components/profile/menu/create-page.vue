<template>
  <Modal
    title="¿Desea crear una página?"
    :disabled="true"
    @close="$emit('close')"
    @submit="handleSubmit"
  >
    <div class="modal-content">
      <p>
        Si crea una página, podrá gestionar blogs y publicaciones con facilidad.
        Esto le permitirá compartir contenido y mantener a su audiencia
        informada.
      </p>
    </div>
  </Modal>
</template>

<script setup lang="ts">
import { toast } from "vue-sonner";
import { PageUser } from "~/config/api";
import { useProtectedFetchJSON } from "~/services/api";

const emit = defineEmits(["close"]);

const { request } = useProtectedFetchJSON();
const { getToken } = useTokenStore();

const handleSubmit = () => {
  toast.promise(
    request(PageUser, {
      method: "POST",
      response: false,
    }),
    {
      loading: "Cargando...",
      success: (_) => {
        getToken().then(() => {});
        return "Página creada con éxito.";
      },
      error: (_) => "Ocurrio un error.",
    }
  );

  emit("close");
};
</script>

<style scoped lang="sass"></style>

<template>
  <Modal
    title="Crear Galería"
    :disabled="disabled"
    @close="$emit('close')"
    @submit="handleSubmit"
  >
    <form>
      <div class="Form-input">
        <label class="Form-input-label">Nombre de la Galería:</label>
        <input
          type="text"
          v-model="galleryName"
          class="Form-input-entry"
          placeholder="Ingrese el nombre de la galería"
        />
      </div>
    </form>
  </Modal>
</template>

<script setup lang="ts">
import { toast } from "vue-sonner";
import { galleryURL } from "~/config/api";
import type { GalleryI } from "~/interfaces/profile";
import { useProtectedFetchJSON } from "~/services/api";

const { updateGalleries } = useTokenStore();
const { data, request } = useProtectedFetchJSON<GalleryI[]>();

const emit = defineEmits(["close"]);

const galleryName = ref("");

const disabled = computed(() => Boolean(galleryName.value.trim()));

const handleSubmit = () => {
  if (galleryName.value.length > 70) {
    toast.error(
      "El nombre de la galeria no de pasar superar los 70 caracteres."
    );
    return;
  }

  toast.promise(
    request(`${galleryURL}/${galleryName.value}`, { method: "POST" }),
    {
      loading: "Cargando...",
      success: (_) => {
        updateGalleries(data.value);
        return `"${galleryName.value}" se creo con éxito.`;
      },
      error: (_) => "Ocurrio un error.",
    }
  );

  emit("close");
};
</script>

<style scoped lang="sass">
.Form-input
  margin-bottom: 1rem
  .Form-input-label
    margin-bottom: 0.5rem
    display: block
    font-weight: 600
    color: #666
  .Form-input-entry
    width: calc(100% - (0.75rem * 2))
    padding: 0.75rem
    border: 1px solid #ccc
    border-radius: 4px
    &:focus
      border-color: #007BFF
      outline: none
</style>

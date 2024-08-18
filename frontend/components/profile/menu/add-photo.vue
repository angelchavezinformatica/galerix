<template>
  <Modal
    title="Añadir Foto"
    :disabled="disabled"
    @close="$emit('close')"
    @submit="handleSubmit"
  >
    <form>
      <div class="Form-input">
        <label class="Form-input-label">Título:</label>
        <input type="text" v-model="title" class="Form-input-entry" />
      </div>

      <div class="Form-input">
        <label class="Form-input-label">Seleccionar Galerías:</label>
        <select multiple v-model="selectedGalleries" class="Form-input-entry">
          <option
            v-for="gallery in user?.galleries"
            :key="gallery.id"
            :value="gallery.id"
          >
            {{ gallery.name }}
          </option>
        </select>
      </div>

      <div class="Form-input">
        <label class="Form-input-label">
          Usar archivo .md para la descripción:
        </label>
        <input type="checkbox" v-model="useMarkdown" />
      </div>

      <div v-if="useMarkdown" class="Form-input">
        <label class="Form-input-label">Subir archivo .md:</label>
        <input type="file" accept=".md" @change="handleMarkdownFileChange" />
      </div>

      <div v-else class="Form-input">
        <label class="Form-input-label">Descripción:</label>
        <textarea v-model="description" class="Form-input-entry"></textarea>
      </div>

      <div class="Form-input">
        <label class="Form-input-label">Foto:</label>
        <input type="file" accept="image/*" @change="handleFileChange" />
      </div>

      <div class="Form-preview" v-if="image">
        <img :src="image" alt="Vista previa" />
      </div>
    </form>
  </Modal>
</template>

<script setup lang="ts">
import { useProtectedFetchJSON } from "~/services/api";
import { toast } from "vue-sonner";
import { UploadImage } from "~/config/api";

const emit = defineEmits(["close"]);

const { user } = useTokenStore();
const { request } = useProtectedFetchJSON();

const title = ref("");
const description = ref("");
const image = ref<string | null>(null);
const useMarkdown = ref(false);
const markdownFileContent = ref<string | null>(null);
const selectedGalleries = ref<number[]>([]);
const fileExtension = ref<string | null>(null);

const disabled = computed(() =>
  Boolean(title.value && description.value && image.value)
);

const handleFileChange = (event: Event) => {
  const file = (event.target as HTMLInputElement).files?.[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      image.value = reader.result as string;
    };
    reader.readAsDataURL(file);
    const file_split = file.name.split(".");
    fileExtension.value = file_split[file_split.length - 1];
  }
};

const handleMarkdownFileChange = (event: Event) => {
  const file = (event.target as HTMLInputElement).files?.[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      markdownFileContent.value = reader.result as string;
      description.value = "";
    };
    reader.readAsText(file);
  }
};

const handleSubmit = () => {
  toast.promise(
    request(UploadImage, {
      method: "POST",
      body: {
        title: title.value,
        description: useMarkdown.value
          ? markdownFileContent.value
          : description.value,
        image: image.value,
        gallery_ids: selectedGalleries.value,
        file_extension: fileExtension.value,
      },
      response: false,
    }),
    {
      loading: "Cargando...",
      success: (_) => "Archivo subido con éxito.",
      error: (_) => "Ha ocurrido un error.",
    }
  );

  emit("close");
};
</script>

<style scoped lang="sass">
.Modal
  position: fixed
  top: 0
  left: 0
  width: 100%
  height: 100%
  background-color: rgba(0, 0, 0, 0.5)
  display: flex
  justify-content: center
  align-items: center

.Modal-content
  background-color: #fff
  padding: 2rem
  border-radius: 8px
  max-width: 500px
  width: 100%
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)

h2
  margin-bottom: 1.5rem
  font-size: 1.5rem
  color: #333

.Form-input
  margin-bottom: 1rem
  .Form-input-label
    margin-bottom: 0.5rem
    display: block
    font-weight: 600
    color: #666
  .Form-input-entry
    width: 100%
    padding: 0.75rem
    border: 1px solid #ccc
    border-radius: 4px
    &:focus
      border-color: #007BFF
      outline: none

.Form-preview
  display: flex
  align-items: center
  justify-content: center
  margin-top: 1rem
  img
    max-width: 100%
    border-radius: 4px
    max-height: 150px

.Modal-actions
  display: flex
  justify-content: space-between
  margin-top: 1.5rem

.Modal-button
  background-color: #007BFF
  color: #fff
  padding: 0.75rem 1.5rem
  border: none
  border-radius: 4px
  cursor: pointer
  transition: background-color 0.3s ease
  &:hover
    background-color: #0056b3

.Modal-button-cancel
  background-color: #ccc
  &:hover
    background-color: #999
</style>

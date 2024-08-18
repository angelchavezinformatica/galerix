<template>
  <div class="Modal">
    <div class="Modal-content">
      <h2>{{ title }}</h2>
      <slot></slot>
      <div class="Modal-actions">
        <button
          type="button"
          @click="$emit('close')"
          class="Modal-button Modal-button-cancel"
        >
          Cancelar
        </button>
        <button
          type="button"
          @click="$emit('submit')"
          class="Modal-button"
          :disabled="!disabled"
        >
          Guardar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ title: string; disabled: boolean }>();

const emit = defineEmits(["close", "submit"]);
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
  overflow: auto

.Modal-content
  background-color: #fff
  padding: 2rem
  border-radius: 8px
  max-width: 500px
  width: 100%
  max-height: 100vh
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)
  overflow-y: auto

h2
  margin-bottom: 1.5rem
  font-size: 1.5rem
  color: #333

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

  .Modal-button[disabled]
    background-color: #007BFF69

  .Modal-button-cancel
    background-color: #ccc
    &:hover
      background-color: #999
</style>

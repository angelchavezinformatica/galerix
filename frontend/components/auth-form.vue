<template>
  <main class="AuthForm">
    <h1>{{ title }}</h1>
    <form class="Form" @submit.prevent="$emit('handleSubmit')">
      <slot />
      <div class="Form-submit">
        <input
          type="submit"
          class="Form-submit-input"
          :value="submitValue"
          :disabled="!disabled"
        />
      </div>
      <hr />
      <slot name="message" />
    </form>
  </main>
</template>

<script setup lang="ts">
interface Prop {
  title: string;
  submitValue: string;
  disabled: boolean;
}
defineProps<Prop>();
defineEmits(["handleSubmit"]);
</script>

<style scoped lang="sass">
.AuthForm
  max-width: 400px
  margin: 0 auto
  padding: 2rem
  background: #ffffff
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)
  border-radius: 8px
  text-align: center
  h1
    font-size: 2rem
    margin-bottom: 1.5rem
    color: #333
  .Form
    display: flex
    flex-direction: column
    gap: 1.5rem
    .Form-input
      display: flex
      flex-direction: column
      text-align: left
    .Form-input-label
      font-size: 1rem
      font-weight: 600
      margin-bottom: 0.5rem
      color: #666
    .Form-input-entry
      padding: 0.75rem
      font-size: 1rem
      border: 1px solid #ccc
      border-radius: 4px
      background-color: #f9f9f9
      transition: border-color 0.3s ease
      &:focus
        border-color: #007BFF
        outline: none
    .Form-submit
      .Form-submit-input
        background-color: #007BFF
        color: #fff
        padding: 0.75rem
        font-size: 1rem
        border: none
        border-radius: 4px
        cursor: pointer
        transition: background-color 0.3s ease
        &:hover
          background-color: #0056b3
      .Form-submit-input[disabled]
        background-color: #007BFF73
  hr
    margin: 2rem 0
    border: none
    border-top: 1px solid #ccc
  p
    font-size: 1rem
    color: #666
    a
      color: #007BFF
      text-decoration: none
      font-weight: 600
      &:hover
        text-decoration: underline
</style>

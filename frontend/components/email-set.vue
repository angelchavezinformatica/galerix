<template>
  <div class="Emails-container">
    <div class="Emails">
      <label for="email" class="Form-input-label">Email</label>
      <div class="Emails-input">
        <input type="email" class="Form-input-entry" v-model="email" />
        <button class="Form-email-button" @click.prevent="handleSubmit">
          +
        </button>
      </div>
    </div>
    <div class="Emails-show">
      <div class="Emails-show-email" v-for="email in emails">
        <p>{{ email }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toast } from "vue-sonner";

const props = defineProps<{ emails: Set<string> }>();
const emit = defineEmits(["addEmail"]);

const email: Ref<string> = ref("");

const handleSubmit = () => {
  if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email.value)) {
    toast.error("El correo no es valido.");
    return;
  }
  if (props.emails.has(email.value)) {
    toast.error("El correo ya ha sido agregado.");
    return;
  }

  emit("addEmail", email.value);
};
</script>

<style scoped lang="sass">
.Emails-container
  display: flex
  flex-direction: column
  gap: 1.5rem

.Emails
  display: flex
  align-items: start
  flex-direction: column

  .Form-input-label
    font-size: 1rem
    font-weight: 600
    margin-bottom: 0.5rem
    color: #666

  .Emails-input
    display: flex
    width: 100%
    flex: 1
    gap: .5rem

    .Form-input-entry
      padding: 0.75rem
      font-size: 1rem
      border: 1px solid #ccc
      border-radius: 4px
      background-color: #f9f9f9
      transition: border-color 0.3s ease
      width: 100%
      &:focus
        border-color: #007BFF
        outline: none

  .Form-email-button
    padding: 0.75rem 1rem
    font-size: 1rem
    border: none
    border-radius: 4px
    cursor: pointer
    background-color: #007BFF
    color: #fff
    transition: background-color 0.3s ease
    &:hover
      background-color: #0056b3

.Emails-show
  display: flex
  flex-direction: column
  gap: 0.5rem

  .Emails-show-email
    background-color: #f9f9f9
    padding: 0.5rem 1rem
    border-radius: 4px
    border: 1px solid #ccc
    transition: background-color 0.3s ease

    p
      margin: 0
      font-size: 1rem
      color: #333
</style>

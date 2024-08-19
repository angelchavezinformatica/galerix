<template>
  <div class="rating-stars">
    <span
      v-for="star in 5"
      :key="star"
      class="star"
      :class="{ filled: star <= currentRating }"
      @click="setRating(star)"
    >
      ★
    </span>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ score: number }>();
const emit = defineEmits(["rate"]);

const currentRating = ref(props.score);

const setRating = (rating: number) => {
  currentRating.value = rating;
  emit("rate", rating);
};
</script>

<style scoped lang="sass">
.rating-stars
  display: flex
  align-items: center
  gap: .3rem
  .star
    font-size: 1.5rem
    cursor: pointer
    color: #ddd
    &.filled
      color: #ffc107
</style>

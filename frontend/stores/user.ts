import type { UserI } from "~/interfaces/api";

export const useUser = defineStore("user", () => {
  const user: Ref<UserI | null> = ref(null);

  return { user };
});

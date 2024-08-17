export const useToken = defineStore("usertoken", () => {
  const token: Ref<string | null> = ref(null);

  const updateToken = (_token: string) => {
    token.value = _token;
    localStorage.setItem("token", _token);
  };

  const getToken = () => {
    token.value = localStorage.getItem("token");
  };

  return { getToken, token, updateToken };
});

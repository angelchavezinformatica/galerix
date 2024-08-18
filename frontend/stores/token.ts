import { profileURL } from "~/config/api";
import type { ProfileI } from "~/interfaces/profile";
import { useFetchJSON } from "~/services/api";

export const useTokenStore = defineStore("usertoken", () => {
  const token: Ref<string | null> = ref(null);
  const user: Ref<ProfileI | null> = ref(null);

  const getUser = async (token: string | null) => {
    const { data, request } = useFetchJSON<ProfileI>();

    await request(profileURL, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    user.value = data.value;
  };

  const updateToken = async (_token: string) => {
    token.value = _token;
    localStorage.setItem("token", _token);
    await getUser(token.value);
  };

  const getToken = async () => {
    token.value = localStorage.getItem("token");
    await getUser(token.value);
  };

  return { getToken, token, user, updateToken };
});

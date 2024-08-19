import { profileURL } from "~/config/api";
import type { GalleryI, ProfileI } from "~/interfaces/profile";
import { useFetchJSON } from "~/services/api";

export const useTokenStore = defineStore("usertoken", () => {
  const { getData: getPhotos } = usePhotoStore();
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

  const updateGalleries = (galleries: GalleryI[] | null) => {
    if (user.value?.galleries && galleries) user.value.galleries = galleries;
  };

  const updateToken = async (_token: string) => {
    token.value = _token;
    localStorage.setItem("token", _token);
    await getUser(token.value);
    await getPhotos(_token);
  };

  const getToken = async () => {
    token.value = localStorage.getItem("token");
    await getUser(token.value);
    await getPhotos(token.value || undefined);
  };

  return { getToken, token, user, updateGalleries, updateToken };
});

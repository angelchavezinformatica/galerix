import { AllPhotos } from "~/config/api";
import type { PhotoI } from "~/interfaces/photo";
import { useProtectedFetchJSON } from "~/services/api";

export const usePhotoStore = defineStore("photostore", () => {
  const { data, request } = useProtectedFetchJSON<PhotoI[]>();

  const getData = async (token: string | undefined) => {
    await request(AllPhotos, { token });
  };

  return { getData, photos: data };
});

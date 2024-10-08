export const base = "http://localhost:8000";
export const api = `${base}/api`;

export const authURL = `${base}/auth`;

export const CreateUser = `${authURL}/create`;
export const LoginUser = `${authURL}/login`;
export const PageUser = `${api}/page`;
export const profileURL = `${api}/profile`;
export const UpdateTextUser = `${profileURL}/text`;
export const searchURL = `${api}/search-user`;

export const UploadImage = `${api}/photo`;
export const galleryURL = `${api}/gallery`;
export const AllPhotos = `${UploadImage}/all`;
export const userPhotosURL = `${UploadImage}/user`;
export const RatePhoto = `${UploadImage}/rate`;
export const ToggleFavoritePhoto = `${UploadImage}/favorite`;

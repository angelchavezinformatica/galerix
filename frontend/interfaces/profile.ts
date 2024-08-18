export interface GalleryI {
  id: number;
  name: string;
}

export interface ProfileI {
  username: string;
  name: string;
  birthday: string;
  address: string;
  emails: string[];
  galleries: GalleryI[];
  page: boolean;
}

export interface UserFoundI {
  username: string;
  name: string;
}

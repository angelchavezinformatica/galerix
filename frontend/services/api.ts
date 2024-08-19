import { toast } from "vue-sonner";

export type Method = "GET" | "POST" | "UPDATE" | "DELETE" | "PATCH";

export interface Options {
  method?: Method;
  headers?: any;
  body?: any;
  response?: boolean;
  token?: string;
}

const _fetch = async (url: string, options?: Options) => {
  return await fetch(url, {
    method: options?.method,
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
    body: JSON.stringify(options?.body),
  });
};

export const fetchJSON = async (url: string, options?: Options) => {
  const response = await _fetch(url, options);

  if (!response.ok) {
    throw response;
  }

  return response;
};

export const useFetchJSON = <T>() => {
  const router = useRouter();
  const data: Ref<T | null> = ref(null);

  const request = async (url: string, options?: Options) => {
    const response = await _fetch(url, options);

    if (!response.ok) router.push("/");
    else if (options?.response === true || options?.response === undefined) {
      data.value = (await response.json()) as T;
    }

    return { response };
  };

  return { data, request };
};

export const useProtectedFetchJSON = <T>() => {
  const { token } = useTokenStore();
  const router = useRouter();

  const data: Ref<T | null> = ref(null);

  const request = async (url: string, options?: Options) => {
    const response = await _fetch(url, {
      method: options?.method,
      headers: {
        Authorization: `Bearer ${options?.token ? options.token : token}`,
        ...options?.headers,
      },
      body: options?.body,
    });

    if (options?.response === true || options?.response === undefined) {
      data.value = (await response.json()) as T;
    } else if (response.status === 401) {
      toast.error("Inicie sesión.");
      router.push("/");
    }

    return { response };
  };

  return { data, request };
};

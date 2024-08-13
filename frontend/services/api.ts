export type Method = "GET" | "POST" | "UPDATE" | "DELETE" | "PATCH";

export interface Options {
  method?: Method;
  headers?: any;
  body?: any;
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
  const data: Ref<T | null> = ref(null);

  const request = async (url: string, options?: Options) => {
    const response = await fetchJSON(url, options);
    data.value = await response.json();

    return { response };
  };

  return { data, request };
};

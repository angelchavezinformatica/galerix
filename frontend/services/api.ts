export type Method = "GET" | "POST" | "UPDATE" | "DELETE" | "PATCH";

export interface Options {
  method: Method;
  headers: any;
  body: any;
}

export const useFetchJSON = <T>(url: string, options?: Options) => {
  const data: Ref<T | null> = ref(null);

  const request = async () => {
    const response = await fetch(url, {
      method: options?.method,
      headers: options?.headers,
      body: JSON.stringify(options?.body),
    });
    data.value = await response.json();
  };

  return { data, request };
};

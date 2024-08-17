import { toast } from "vue-sonner";
import { LoginUser } from "~/config/api";
import { fetchJSON } from "~/services/api";
import { useToken } from "~/stores/token";

export const useLogin = () => {
  const { updateToken } = useToken();
  const router = useRouter();

  const username: Ref<string> = ref("");
  const password: Ref<string> = ref("");

  const disabled: ComputedRef<boolean> = computed(() =>
    Boolean(username.value && password.value)
  );

  const handleSubmit = () => {
    toast.promise(
      fetchJSON(LoginUser, {
        method: "POST",
        body: {
          username: username.value,
          password: password.value,
        },
      }),
      {
        loading: () => {
          password.value = "";
          return "Cargando...";
        },
        error: (data) => {
          if (data.status === 404) return "Usuario no encontrado.";
          if (data.status === 400) return "Credenciales invalidas.";
          return "Ocurrió un error al iniciar sesión.";
        },
        success: (data) => {
          data.json().then((value) => {
            updateToken(value.token);
          });
          router.push("/gallery");
          return "Inicio de sesión valido.";
        },
      }
    );
  };

  return { disabled, handleSubmit, password, username };
};

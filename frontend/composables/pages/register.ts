import { CreateUser } from "~/config/api";
import { toast } from "vue-sonner";
import { fetchJSON } from "~/services/api";

export const usePageRegister = () => {
  const router = useRouter();

  const username: Ref<string> = ref("");
  const password: Ref<string> = ref("");
  const name: Ref<string> = ref("");
  const birthday: Ref<string> = ref("");
  const address: Ref<string> = ref("");
  const emails: Ref<Set<string>> = ref(new Set());

  const disabled: ComputedRef<boolean> = computed(() =>
    Boolean(
      username.value &&
        password.value &&
        name.value &&
        birthday.value &&
        address.value
    )
  );

  const addEmail = (email: string) => {
    emails.value.add(email);
  };

  const handleSubmit = async () => {
    if (!/^.{8,}$/.test(password.value)) {
      toast.error("La contraseña debe contener al menos 8 caracters.");
      return;
    } else if (!/(?=.*[a-z])/.test(password.value)) {
      toast.error("La contraseña debe contener al menos una minuscula.");
      return;
    } else if (!/(?=.*[A-Z])/.test(password.value)) {
      toast.error("La contraseña debe contener al menos una mayuscula.");
      return;
    } else if (!/(?=.*\d)/.test(password.value)) {
      toast.error("La contraseña debe contener al menos un dígito.");
      return;
    } else if (!/(?=.*[!@#$%^&*])/.test(password.value)) {
      toast.error("La contraseña debe contener un caracter especial.");
      return;
    }

    toast.promise(
      fetchJSON(CreateUser, {
        method: "POST",
        body: {
          username: username.value,
          password: password.value,
          name: name.value,
          birthday: birthday.value,
          address: address.value,
          emails: Array.from(emails.value),
        },
      }),
      {
        loading: () => {
          password.value = "";
          return "Cargando...";
        },
        error: (data) => {
          if (data.status === 409) return "El nombre de usuario ya existe!";
          return "Ocurrió un error al crear el usuario.";
        },
        success: (_) => {
          router.push("/");
          return "Usuario creado";
        },
      }
    );
  };

  return {
    addEmail,
    address,
    birthday,
    disabled,
    emails,
    handleSubmit,
    name,
    password,
    username,
  };
};

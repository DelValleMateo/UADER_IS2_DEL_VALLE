import os
import readline  # Usar pyreadline3 en Windows si hay error
import together
from dotenv import load_dotenv
from openai import OpenAI
# Cargar la API Key desde archivo .env
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

if not api_key:
    print("❌ No se encontró la API KEY.")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.together.xyz/v1"
)
# No hace falta usar together.api_key, ya se carga desde el entorno
modelo = "mistralai/Mistral-7B-Instruct-v0.1"
last_input = ""

while True:
    try:
        user_input = input(
            "Ingresá tu consulta (o ENTER para salir): ").strip()

        if not user_input:
            print("👋 Saliste del programa.")
            break

        readline.add_history(user_input)
        last_input = user_input

        try:
            print(f"You: {user_input}")

            try:
                # Llamada a la API actualizada (nuevo método)
                response = client.chat.completions.create(
                    model="mistralai/Mistral-7B-Instruct-v0.1",
                    messages=[{"role": "user", "content": user_input}]
                )

                print("chatGPT:", response.choices[0].message.content)

            except Exception as api_error:
                print("❌ Error durante la llamada a la API:")
                print(api_error)

        except Exception as process_error:
            print("❌ Error procesando la consulta:")
            print(process_error)

    except Exception as input_error:
        print("❌ Error al ingresar la consulta:")
        print(input_error)

from openai import OpenAI
key = "alv2_FkaZPlnFMxMX32BCVuVtxMe1nv_ssd5ewju8Ge6z4pg"
client = OpenAI(
    base_url="https://api.aionlabs.ai/v1",
    api_key=key)


response = client.chat.completions.create(
    model="aion-labs/aion-2.0",
    messages=[{"role": "user", "content": "Explain quantum physics simply."}],
    temperature=0.7 # Using Aion, need to pass temperature variable
)
print(response.choices[0].message.content)

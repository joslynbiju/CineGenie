import requests
import json
import os

def generate_image(api_key, prompt, negative_prompt="bad quality", width=512, height=512, samples=1, seed=None):
    url = "https://modelslab.com/api/v6/realtime/text2img"
    payload = json.dumps({
        "key": api_key,
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,
        "safety_checker": False,
        "seed": seed,
        "samples": samples,
        "base64": False,
        "enhance_prompt": True,
        "enhance_style": "cinematic"
    })

    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    print("API Response Status Code:", response.status_code)
    print("API Response Text:", response.text)

    if response.status_code != 200:
        return {"error": f"API request failed with status {response.status_code}", "raw_response": response.text}

    try:
        return response.json()
    except json.decoder.JSONDecodeError:
        return {"error": "Failed to decode JSON response", "raw_response": response.text}

def save_image(image_url, output_dir, image_name):
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(os.path.join(output_dir, image_name), 'wb') as file:
            file.write(image_response.content)


















# import requests
# import json
# import os
#
# def generate_image(api_key, prompt, negative_prompt="bad quality", width=512, height=512, samples=1, seed=None):
#     url = "https://modelslab.com/api/v6/realtime/text2img"
#     payload = json.dumps({
#         "key": api_key,
#         "prompt": prompt,
#         "negative_prompt": negative_prompt,
#         "width": width,
#         "height": height,
#         "safety_checker": False,
#         "seed": seed,
#         "samples": samples,
#         "base64": False
#     })
#
#     headers = {
#         'Content-Type': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     # Print the entire response for debugging
#     print("API Response Status Code:", response.status_code)
#     print("API Response Text:", response.text)
#
#     if response.status_code != 200:
#         return {"error": f"API request failed with status {response.status_code}", "raw_response": response.text}
#
#     try:
#         return response.json()
#     except json.decoder.JSONDecodeError:
#         return {"error": "Failed to decode JSON response", "raw_response": response.text}
#
# def save_image(image_url, output_dir, image_name):
#     image_response = requests.get(image_url)
#     if image_response.status_code == 200:
#         with open(os.path.join(output_dir, image_name), 'wb') as file:
#             file.write(image_response.content)
#
# def load_memory(memory_file="memory.json"):
#     if os.path.exists(memory_file):
#         with open(memory_file, "r") as file:
#             return json.load(file)
#     return {}
#
# def update_memory(prompt, image_url, memory_file="memory.json"):
#     memory = load_memory(memory_file)
#     memory[prompt] = image_url
#     with open(memory_file, "w") as file:
#         json.dump(memory, file)



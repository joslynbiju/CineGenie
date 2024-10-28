import os
from pdf_parser import extract_scenes_from_pdf
from image_generator import generate_image, save_image
from ner_extractor import extract_entities_with_descriptions, load_memory, update_memory
from moviepy.editor import ImageSequenceClip

def process_screenplay(pdf_path, api_key, output_dir="output_images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load or initialize memory for reinforcement learning
    memory = load_memory()

    scenes = extract_scenes_from_pdf(pdf_path)

    for i, scene in enumerate(scenes):
        print(f"Processing scene {i + 1}/{len(scenes)}: {scene[:10]}...")

        # Perform NER and extract objects, locations, and characters with their descriptions
        entities, descriptions = extract_entities_with_descriptions(scene)
        print(f"Entities found in scene {i + 1}: {entities}")

        # Store descriptions for objects, locations, and characters
        detailed_info = {
            "locations": {loc: descriptions[loc] for loc in entities.get("GPE", []) + entities.get("LOC", [])},
            "characters": {char: descriptions[char] for char in entities.get("PERSON", [])},
            "objects": {obj: descriptions[obj] for obj in entities.get("OBJECT", [])},
        }

        # Construct the custom prompt using descriptions instead of names
        location_desc = ", ".join([f"{loc} ({desc})" for loc, desc in detailed_info['locations'].items()])
        characters_desc = ", ".join([f"{char} ({desc})" for char, desc in detailed_info['characters'].items()])
        objects_desc = ", ".join([f"{obj} ({desc})" for obj, desc in detailed_info['objects'].items()])

        custom_prompt = f"Scene Description: {scene}\nLocations: {location_desc}\nCharacters: {characters_desc}\nObjects: {objects_desc}"

        # Check memory for existing images
        existing_image_url = memory.get(custom_prompt)
        if existing_image_url:
            print(f"Using existing image for scene {i + 1}: {existing_image_url}")
            save_image(existing_image_url, output_dir, f"scene_{i + 1}.png")
            continue

        # Generate new image
        result = generate_image(api_key, prompt=custom_prompt)

        if "output" in result:
            image_url = result['output'][0]
            image_name = f"scene_{i + 1}.png"
            save_image(image_url, output_dir, image_name)
            print(f"Image saved: {image_name}")

            # Update memory with new image URL
            update_memory({custom_prompt: image_url})
        else:
            print(f"Failed to generate image for scene {i + 1}: {result.get('error', 'Unknown error')}")


# Step 2: Create a Video from Generated Images
def create_video_from_images(image_folder, output_video_path, fps=24):
    # Get the list of all image files in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]

    # Sort the images by name (assumes images are named in order, like scene_1.png, scene_2.png, etc.)
    images.sort()

    # Create full paths to the images
    image_paths = [os.path.join(image_folder, img) for img in images]

    # Create video from images
    clip = ImageSequenceClip(image_paths, fps=fps)

    # Save the video
    clip.write_videofile(output_video_path, codec='libx264')

api_key = "Eg0tMjliVkxEq0csbIsBPZcJ3wMMdRjgIIPDt1WLL7YBvYGsMyRDKmtin6YV"
pdf_path = r"C:\Users\josly\Downloads\Filmmaking AI Project\Film Scripts\the-pursuit-of-happyness-2006.pdf"
image_output_dir = r"C:\Users\josly\PycharmProjects\FIlm_Making\visualization_using_SD\output_images"
video_output_path = r"C:\Users\josly\PycharmProjects\FIlm_Making\visualization_using_SD\images_visualization.mp4"

# Step 1: Generate images from scenes in the PDF
process_screenplay(pdf_path, api_key)
# Step 2: Create video from generated images
create_video_from_images(image_output_dir, video_output_path, fps=24)
















# import os
# from pdf_parser import extract_scenes_from_pdf
# from image_generator import generate_image, save_image
# from ner_extractor import extract_entities, load_memory, update_memory
#
# def process_screenplay(pdf_path, api_key, output_dir="output_images"):
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#
#     # Load or initialize memory for reinforcement learning
#     memory = load_memory()
#
#     scenes = extract_scenes_from_pdf(pdf_path)
#
#     for i, scene in enumerate(scenes):
#         print(f"Processing scene {i + 1}/{len(scenes)}: {scene[:60]}...")
#
#         # Perform NER on the scene description
#         entities = extract_entities(scene)
#         print(f"Entities found in scene {i + 1}: {entities}")
#
#         # Extract location, characters, and other specifications
#         location = ", ".join(entities.get("GPE", []) + entities.get("LOC", []))
#         characters = ", ".join(entities.get("PERSON", []))
#
#         # Construct the custom prompt
#         custom_prompt = f"Scene: {scene}\nLocation: {location}\nCharacters: {characters}"
#
#         # Check memory for existing images for the same scene
#         existing_image_url = memory.get(custom_prompt)
#         if existing_image_url:
#             print(f"Using existing image for scene {i + 1}: {existing_image_url}")
#             save_image(existing_image_url, output_dir, f"scene_{i + 1}.png")
#             continue
#
#         # Generate new image
#         result = generate_image(api_key, prompt=custom_prompt)
#
#         if "output" in result:
#             image_url = result['output'][0]
#             image_name = f"scene_{i + 1}.png"
#             save_image(image_url, output_dir, image_name)
#             print(f"Image saved: {image_name}")
#
#             # Update memory with new image URL
#             update_memory(custom_prompt, image_url)
#         else:
#             print(f"Failed to generate image for scene {i + 1}: {result.get('error', 'Unknown error')}")
#
# # Example usage
# api_key = "NOWXimmzNLHTxDNR9MOmFyx0yhmJu3zimqvG8dNBDKhgb94iTqky7L3wp4S4"
# pdf_path = r"C:\Users\josly\Downloads\Filmmaking AI Project\Film Scripts\Interstallar.pdf"
#
# process_screenplay(pdf_path, api_key)


# # main.py
# import os
# from pdf_parser import extract_scenes_from_pdf
# from image_generator import generate_image, save_image
# from ner_extractor import extract_entities
#
# def process_screenplay(pdf_path, api_key, output_dir="output_images"):
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#
#     scenes = extract_scenes_from_pdf(pdf_path)
#
#     for i, scene in enumerate(scenes):
#         print(f"Processing scene {i + 1}/{len(scenes)}: {scene[:60]}...")
#
#         # Perform NER on the scene description
#         entities = extract_entities(scene)
#         print(f"Entities found in scene {i + 1}: {entities}")
#
#         result = generate_image(api_key, prompt=scene)
#
#         if "output" in result:
#             image_url = result['output'][0]
#             image_name = f"scene_{i + 1}.png"
#             save_image(image_url, output_dir, image_name)
#             print(f"Image saved: {image_name}")
#         else:
#             print(f"Failed to generate image for scene {i + 1}: {result.get('error', 'Unknown error')}")
#
#
# # Example usage
# api_key = "5uEWMTCvBB42rZZ62Fi5uTIldMcGJweOJC2892emBseYtTXAY1rucMzLEbvb"
# pdf_path = r"C:\Users\josly\Downloads\Filmmaking AI Project\Film Scripts\Interstallar.pdf"
#
# process_screenplay(pdf_path, api_key)

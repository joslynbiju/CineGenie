import PyPDF2

def extract_scenes_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    lines = text.splitlines()

    scenes = []
    current_scene = []
    inside_scene = False

    for line in lines:
        if line.startswith("EXT.") or line.startswith("INT."):
            if inside_scene:
                scenes.append(" ".join(current_scene).strip())
                current_scene = []
            inside_scene = True
        if inside_scene:
            current_scene.append(line)

    if inside_scene and current_scene:
        scenes.append(" ".join(current_scene).strip())

    return scenes



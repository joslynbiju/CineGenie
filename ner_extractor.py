import spacy
import json
import os

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities_with_descriptions(text):
    doc = nlp(text)
    entities = {"PERSON": [], "GPE": [], "LOC": [], "OBJECT": []}  # Adding 'OBJECT' for general items
    descriptions = {}

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
            # Extract descriptions from surrounding context (sentence or nearby words)
            descriptions[ent.text] = ent.sent.text.strip()

    return entities, descriptions

def load_memory(memory_file="memory.json"):
    if os.path.exists(memory_file):
        with open(memory_file, "r") as file:
            return json.load(file)
    return {}

def update_memory(data, memory_file="memory.json"):
    memory = load_memory(memory_file)
    memory.update(data)
    with open(memory_file, "w") as file:
        json.dump(memory, file, indent=4)













# # ner_extractor.py
# import spacy
#
# # Load spaCy model
# nlp = spacy.load("en_core_web_sm")
#
# def extract_entities(text):
#     doc = nlp(text)
#     entities = {"PERSON": [], "GPE": [], "LOC": [], "ORG": [], "PRODUCT": [], "EVENT": [], "WORK_OF_ART": [], "LAW": []}
#
#     for ent in doc.ents:
#         if ent.label_ in entities:
#             entities[ent.label_].append(ent.text)
#
#     return entities

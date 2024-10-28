# CineGenie - An AI-Powered Pre-Production Tool for Automated Screenplay Analysis and Visualization in Filmmaking

This project is designed to automate the process of scene visualization from film scripts. It parses the screenplay, extracts scene descriptions and entities, generates images based on those descriptions, and finally compiles these images into a video. The key components of this project include scene extraction from a PDF, entity recognition, image generation, and video creation.

## Project Structure

The project includes four main Python files:

1. **pdf_parser.py**: Extracts scenes from a film script PDF.
2. **ner_extractor.py**: Uses spaCy's NLP model to identify characters, locations, and objects within scenes, including context-based descriptions.
3. **image_generator.py**: Sends scene descriptions to an image generation API, creating and saving the resulting images.
4. **video_creator.py**: Compiles generated images into a video file.

## Requirements

- **Python 3.7+**
- **spaCy**: For Named Entity Recognition (NER)
- **PyPDF2**: For reading PDF scripts
- **moviepy**: For compiling images into a video
- **Requests**: For making API calls

Install dependencies with:
```bash
pip install spacy PyPDF2 moviepy requests

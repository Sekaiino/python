from pathlib import Path

downloads = Path("C:/Users/envu1/Downloads")

dirs = {
    ".png" : "Image",
    ".jpeg" : "Image",
    ".jpg" : "Image",
    ".bmp" : "Image",
    ".PNG" : "Image",
    ".mp4" : "Vidéo",
    ".avi" : "Vidéo",
    ".gif" : "Vidéo",
    ".mp3" : "Musique",
    ".wav" : "Musique",
    ".flac" : "Musique",
    ".txt" : "Document",
    ".pdf" : "Document",
    ".xls" : "Document",
    ".pptx" : "Document",
    ".csv" : "Document",
    ".odp" : "Document"
}

files = [f for f in downloads.iterdir() if f.is_file()]

for f in files:
    outputDir = downloads / dirs.get(f.suffix, "Autres")
    outputDir.mkdir(exist_ok=True)
    f.rename(outputDir / f.name)
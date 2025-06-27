import spacy
import json
import os

# Auto-download the model if not available
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model 'en_core_web_sm'...")
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def chunk_text(text, max_chunk_words=40):
    """
    Splits a long paragraph into meaning-preserving chunks
    using spaCy's sentence segmentation and word counting.
    """
    doc = nlp(text)
    chunks = []
    current_chunk = []

    for sent in doc.sents:
        words_in_sent = len(sent.text.split())
        current_words = sum(len(s.text.split()) for s in current_chunk)

        if current_words + words_in_sent <= max_chunk_words:
            current_chunk.append(sent)
        else:
            if current_chunk:
                chunks.append(" ".join([s.text for s in current_chunk]))
            current_chunk = [sent]

    if current_chunk:
        chunks.append(" ".join([s.text for s in current_chunk]))

    return chunks

# === Option A: Load from a file ===
file_path = "long_text.txt"
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        long_text = f.read()
else:
    # === Option B: Use built-in long sentence ===
    long_text = """
    Despite the increasingly urgent warnings issued by climatologists, ecologists, and geopolitical analysts around the world—who, backed by decades of peer-reviewed research and satellite data, have meticulously documented the rapid acceleration of global temperature rise, sea-level encroachment on vulnerable coastal zones, the catastrophic collapse of biodiversity in both marine and terrestrial ecosystems, and the intensifying frequency and severity of extreme weather phenomena ranging from prolonged droughts and unseasonal floods to record-breaking hurricanes and wildfires—many industrialized nations, beholden to short-term economic growth models, fossil-fuel lobbying interests, and deeply entrenched political inertia, continue to delay the implementation of ambitious mitigation policies that prioritize renewable energy transitions, systemic agricultural reforms, and climate-resilient infrastructure, thereby perpetuating not only the physical degradation of the biosphere but also exacerbating socio-economic inequalities, food insecurity, and forced migration crises that disproportionately affect historically marginalized populations, all while simultaneously fueling a global feedback loop wherein the very systems humanity depends on for survival—freshwater availability, pollination networks, arable land productivity, and atmospheric stability—are being destabilized at a rate so alarming that, unless immediate, collective, and enforceable action is taken across governmental, corporate, and civic spheres, the likelihood of crossing irreversible planetary boundaries within the current century becomes not just a theoretical projection but a looming certainty, fraught with intergenerational ethical implications and profound existential consequences for both present and future life on Earth.
    """

# --- Split the text into chunks ---
chunks = chunk_text(long_text, max_chunk_words=40)

# --- Print the chunks ---
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}:\n{chunk}\n")

# --- Save to JSON file (optional) ---
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2, ensure_ascii=False)

print(f"\n✅ {len(chunks)} chunks saved to 'chunks.json'")

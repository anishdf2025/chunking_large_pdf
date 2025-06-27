# 📄 Text Chunking for Large PDFs

A Python tool for intelligently splitting large text documents into smaller chunks for translation and processing.

## 🚀 Features

- **Multi-language Support**: Hindi and English text processing
- **Smart Splitting**: 
  - Hindi: Prioritizes `|` character boundaries with 2048 token chunks
  - English: Uses spaCy for sentence-aware splitting with 512 token chunks
- **Boundary Preservation**: Never breaks sentences or words inappropriately
- **Interactive Interface**: User-friendly prompts for language selection

## 🛠️ Requirements

- Python 3.7+
- spaCy with English model (`en_core_web_sm`)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chunking_large_pdf.git
cd chunking_large_pdf
```

2. Install dependencies:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## 🎯 Usage

1. Update the file path in `splits.py`:
```python
file_path = "path/to/your/text/file.txt"
```

2. Run the script:
```bash
python splits.py
```

3. Choose your language (hindi/english) when prompted

## 📂 Files

- `splits.py` - Main text splitting logic
- `spacy_model.py` - spaCy model configuration
- `sementic_chunk.py` - Semantic chunking utilities
- `chunks.json` - Example output format

## 🔧 How It Works

### Hindi Text:
- Target: 2048 tokens per chunk
- Priority splitting at `|` characters
- Falls back to sentence boundaries and whitespace

### English Text:
- Target: 512 tokens per chunk  
- Uses spaCy for accurate sentence segmentation
- Maintains sentence integrity

## 📊 Example Output

```
Language: English
Target tokens: 512
Splitting method: spaCy-based

Total chunks created: 5

========== Chunk 1 ==========
[Your text content here...]
========== End Chunk 1 (Length: 2048 chars) ==========
```

## 🤝 Contributing

Feel free to submit issues and pull requests!

## 📝 License

MIT License - see LICENSE file for details

# CultureCode

treating culture like code opens up ways to document, fork, version-control, and collaboratively explore the evolution of human societies.

## 🧠 Core Concept: "Culture as Code"

Each culture = a repository (or module) containing:

- **Core "values"** (analogous to constants)
- **Social "algorithms"** (e.g., political systems, economic models)
- **"Dependencies"** (influences from other cultures)
- **"Commits"** = major historical shifts (wars, inventions, migrations)
- **"Forks"** = splinter groups or successor civilizations)

This lets users trace cultural evolution like developers trace code lineage.

## 🏗️ Project Structure

```
CultureCode/
├── README.md
├── LICENSE
├── schema/
│   ├── cultural_schema.json
│   └── civilization_template.md
├── cultures/
│   ├── Egypt_Ancient/
│   │   ├── README.md
│   │   ├── values.yaml
│   │   ├── social_systems.md
│   │   ├── innovations.md
│   │   └── timeline.json
│   ├── Greece_Classical/
│   ├── Rome/
│   ├── Han_China/
│   ├── Mayan/
│   └── etc...
└── tools/
    ├── compare.py
    ├── lineage_graph.py
    └── cli_interface.sh
```

## 📄 Each Culture File Includes

| File | Description |
|------|-------------|
| `README.md` | Overview: time period, geography, language, religion, political structure |
| `values.yaml` | "Cultural constants" — ethics, worldview, identity |
| `social_systems.md` | Government, economics, family structure, gender roles, etc. |
| `innovations.md` | Technology, art, science, architecture |
| `timeline.json` | Key events with dates and "commit messages" |
| `dependencies.json` | Cultural influences and successors (imports/forks) |

## ⚙️ Tools & Automation

### CLI Interface (culture.sh)
A command-line interface to interact with cultural data:

```bash
# Compare two cultures
./tools/cli_interface.sh compare Egypt_Ancient Greece_Classical

# Show information about a specific culture
./tools/cli_interface.sh info Egypt_Ancient

# Show timeline of a culture
./tools/cli_interface.sh timeline Egypt_Ancient

# Show cultural dependencies
./tools/cli_interface.sh dependencies Egypt_Ancient

# Search for a term across all cultures
./tools/cli_interface.sh search "democracy"

# Generate cultural lineage graph
./tools/cli_interface.sh lineage
```

### Python Scripts
- `compare.py` - Compare two cultures and output their differences
- `lineage_graph.py` - Generate network graphs showing cultural influence

## 🌐 Example Culture Files

### cultures/Egypt_Ancient/README.md
```
# Ancient Egypt

**Time Period:** 3100 BCE – 30 BCE  
**Core Values:** Ma'at (order, balance), divine kingship  
**Political System:** Theocratic monarchy  
**Innovations:** Hieroglyphic writing, pyramids, irrigation, papyrus  
**Dependencies:** Influenced Nubian and Hellenistic cultures  
**Forks:** Ptolemaic Egypt (Hellenistic influence)
```

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CultureCode.git
   cd CultureCode
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # if available
   # or install required packages manually:
   pip install networkx matplotlib pyyaml
   ```

3. Explore cultures:
   ```bash
   ./tools/cli_interface.sh list
   ./tools/cli_interface.sh info Egypt_Ancient
   ```

4. Add your own culture:
   - Follow the civilization template in `schema/civilization_template.md`
   - Create a new directory in the `cultures` folder
   - Submit a pull request to contribute!

## 📚 Contributing

See our [Civilization Template](schema/civilization_template.md) for guidelines on how to structure your cultural data.

### Adding a New Culture

1. Fork the repository
2. Create a new directory in `cultures` with your culture name (e.g., `cultures/Rome/`)
3. Add the required files following the template
4. Create a pull request with your addition

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
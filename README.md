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
│   │   ├── timeline.json
│   │   └── dependencies.json
│   ├── Greece_Classical/
│   │   ├── README.md
│   │   ├── values.yaml
│   │   ├── social_systems.md
│   │   ├── innovations.md
│   │   ├── timeline.json
│   │   └── dependencies.json
│   ├── Rome/
│   │   ├── README.md
│   │   ├── values.yaml
│   │   ├── social_systems.md
│   │   ├── innovations.md
│   │   ├── timeline.json
│   │   └── dependencies.json
│   ├── Han_China/
│   │   ├── README.md
│   │   ├── values.yaml
│   │   ├── social_systems.md
│   │   ├── innovations.md
│   │   ├── timeline.json
│   │   └── dependencies.json
│   ├── Maya/
│   │   ├── README.md
│   │   ├── values.yaml
│   │   ├── social_systems.md
│   │   ├── innovations.md
│   │   ├── timeline.json
│   │   └── dependencies.json
│   ├── Islamic_Golden_Age/
│   │   ├── README.md
│   │   ├── values.yaml
│   │   ├── social_systems.md
│   │   ├── innovations.md
│   │   ├── timeline.json
│   │   └── dependencies.json
│   ├── Medieval_Europe/
│   │   ├── README.md
│   │   ├── values.yaml
│   │   ├── social_systems.md
│   │   ├── innovations.md
│   │   ├── timeline.json
│   │   └── dependencies.json
│   └── Mali_Empire/
│       ├── README.md
│       ├── values.yaml
│       ├── social_systems.md
│       ├── innovations.md
│       ├── timeline.json
│       └── dependencies.json
└── tools/
    ├── compare.py
    ├── lineage_graph.py
    └── cli_interface.sh
```

## 📚 Available Cultures

The CultureCode project currently includes the following cultures:

### Ancient Civilizations
- **Egypt_Ancient** (3100 BCE – 30 BCE): Ancient Egypt with its pharaohs, pyramids, and rich religious traditions
- **Greece_Classical** (5th-4th centuries BCE): Classical Greece, birthplace of democracy and Western philosophy
- **Rome** (753 BCE – 476 CE): From Republic to Empire, Rome's legal and administrative systems influenced the world
- **Maya** (2000 BCE – 16th century CE): Advanced Mesoamerican civilization with sophisticated mathematics and astronomy

### Asian Civilizations  
- **Han_China** (206 BCE – 220 CE): The Han Dynasty established many features of Chinese civilization
- **Indus Valley** (3300-1300 BCE): One of the world's earliest urban civilizations (coming soon)

### Medieval & Islamic World
- **Islamic_Golden_Age** (8th-13th centuries): Period of cultural, economic, and scientific flourishing in Islamic civilization
- **Medieval_Europe** (5th-15th centuries): Feudal Europe with its cathedrals, universities, and chivalric culture

### African Civilizations
- **Mali_Empire** (1235-1670 CE): Powerful West African empire known for its wealth and the University of Timbuktu
- **Axum Empire** (100-940 CE): Ancient African kingdom in present-day Ethiopia and Eritrea (coming soon)

### And more coming soon...
- Aztec Empire
- Inca Empire
- Byzantine Empire
- Renaissance Italy
- Feudal Japan
- Ancient India (Mauryan/Gupta periods)

## 📄 Each Culture File Includes

| File | Description |
|------|-------------|
| `README.md` | Overview: time period, geography, language, religion, political structure |
| `values.yaml` | "Cultural constants" — ethics, worldview, identity |
| `social_systems.md` | Government, economics, family structure, gender roles, etc. |
| `innovations.md` | Technology, art, science, architecture |
| `timeline.json` | Key events with dates and "commit messages" |
| `dependencies.json` | Cultural influences and successors (imports/forks) |

## 🌐 Web Application: "The Hitchhiker's Guide to History"

We've created a Python Flask web application that provides an interactive interface to explore the CultureCode project. This "Hitchhiker's Guide to History" includes:

- **Browse Interface**: Explore all documented cultures with rich detail pages
- **Comparison Tool**: Compare different civilizations side-by-side
- **Timeline Visualization**: Interactive timeline showing when cultures existed and overlapped
- **API Endpoints**: Programmatic access to all cultural data
- **Responsive Design**: Works well on desktop and mobile devices

### Installation and Running

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   cd app
   python app.py
   ```
   Or use the run script:
   ```bash
   ./run_app.sh
   ```

3. Visit `http://localhost:5000` in your browser

### Features

- **Culture Detail Pages**: Comprehensive information about each civilization
- **Comparison Tool**: Analyze similarities and differences between cultures
- **Timeline View**: Visualize the temporal relationships between civilizations
- **API Access**: JSON endpoints at `/api/cultures` and `/api/culture/{name}`
- **GitHub Integration**: Links to source files for each culture
- **Interactive Elements**: Search, filter, and navigate through history

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
**Geography:** Northeastern Africa, along the Nile River  
**Core Values:** Ma'at (order, balance), divine kingship, afterlife  
**Political System:** Theocratic monarchy  
**Major Innovations:** Hieroglyphic writing, pyramids, irrigation, papyrus  
**Dependencies:** Influenced by Nubian and Mesopotamian cultures  
**Forks:** Ptolemaic Egypt (Hellenistic influence)  

## Overview
Ancient Egypt was a civilization of ancient Northeast Africa, concentrated along the lower reaches of the Nile River. It followed predynastic cultures in the region and is generally thought to have begun with the formation of the unified kingdom of Upper and Lower Egypt around 3150 BC, under the first pharaoh, Narmer.

Egyptian civilization was based on the Nile River and its floods, which gave rise to agriculture and the first settlements. The civilization lasted for over 3,000 years, ending with the death of Cleopatra VII in 30 BC when Egypt was conquered by Rome.
```

### cultures/Greece_Classical/README.md
```
# Classical Greece

**Time Period:** 5th-4th centuries BCE (Classical Period: c. 480-323 BCE)  
**Geography:** Greek mainland, islands of the Aegean Sea, western coast of Asia Minor, southern Italy, Sicily  
**Core Values:** Democracy, philosophy, arete (excellence), paideia (education), kalokagathia (beauty and goodness)  
**Political System:** City-state (polis) democracy in Athens, oligarchy in Sparta, various other systems  
**Major Innovations:** Democracy, philosophy, tragedy and comedy, classical architecture, historiography  
**Dependencies:** Influenced by earlier Greek civilizations (Minoan, Mycenaean) and Eastern cultures  
**Forks:** Hellenistic culture (spread by Alexander the Great's conquests)  

## Overview
Classical Greece refers to the period when Greek culture reached its zenith, particularly during the 5th and 4th centuries BCE. This era is known for its significant contributions to philosophy, mathematics, astronomy, medicine, literature, and the arts. The period also saw the development of democracy in Athens and the rise of the polis (city-state) as the fundamental political unit.

The Classical Period emerged after the Greek victory over the Persian Empire and was marked by significant cultural and intellectual achievements. It ended with the death of Alexander the Great in 323 BCE, which ushered in the Hellenistic Age.
```

### cultures/Rome/README.md
```
# Ancient Rome

**Time Period:** 753 BCE – 476 CE (Western Roman Empire falls)  
**Geography:** Italian Peninsula expanding to encompass the Mediterranean basin and much of Europe, North Africa, and Western Asia  
**Core Values:** Virtus (courage/virtue), gravitas (seriousness/dignity), pietas (duty to gods, family, country), disciplina (discipline), fides (good faith/trust)  
**Political System:** Monarchy (753-509 BCE) → Republic (509-27 BCE) → Empire (27 BCE-476 CE in West)  
**Major Innovations:** Legal system (Roman Law), engineering (aqueducts, roads, concrete), military organization, administrative systems  
**Dependencies:** Influenced by Etruscan, Greek, and other Italic cultures  
**Forks:** Western Roman Empire, Eastern Roman (Byzantine) Empire  

## Overview
Ancient Rome began as a small agricultural community on the Italian Peninsula that developed into one of the largest empires in the ancient world. At its height, the Roman Empire encompassed the entire Mediterranean basin and much of Europe, North Africa, and Western Asia. Rome's system of government evolved from a monarchy to a republic and finally to an empire. The Romans were known for their practical approach to governance, engineering, and law, many aspects of which continue to influence the world today.

The Roman Republic was characterized by a complex system of checks and balances, while the Empire established a more centralized form of government that maintained control over vast territories for centuries. Roman culture was pragmatic, borrowing and adapting elements from other cultures, particularly Greek.
```

### cultures/Han_China/README.md
```
# Han Dynasty China

**Time Period:** 206 BCE – 220 CE  
**Geography:** East Asia, primarily modern-day China, extending at times to Central Asia, Vietnam, Korea  
**Core Values:** Confucianism (social harmony, filial piety, proper conduct), Daoism (harmony with nature, wu wei), Legalism (rule of law), filial piety, social hierarchy  
**Political System:** Centralized imperial system with Mandate of Heaven, bureaucracy based on merit  
**Major Innovations:** Paper, seismograph, improvements to the Silk Road, civil service examination, Three Principles of the People concept  
**Dependencies:** Influenced by earlier Chinese dynasties (Zhou, Qin), indigenous Chinese philosophies  
**Forks:** Later Chinese dynasties, East Asian cultures, spread of Confucianism  

## Overview
The Han Dynasty represents one of the most significant periods in Chinese history, establishing many features that would define Chinese civilization for the next two millennia. The dynasty is divided into two periods: the Western Han (206 BCE – 9 CE) and the Eastern Han (25–220 CE), separated by the brief Xin Dynasty of Wang Mang. 

The Han period saw major developments in science, technology, arts, and literature. It was during this time that China's identity as a unified state under imperial rule was solidified. The term "Han Chinese" originates from this dynasty and is still used today to describe the majority ethnic group in China.

The Han Dynasty established the foundation for the Chinese imperial system, including the civil service examination system, which selected government officials based on merit rather than birth. The dynasty also saw the establishment of Confucianism as the state ideology and the expansion of the Silk Road trade networks.
```

### cultures/Maya/README.md
```
# Maya Civilization

**Time Period:** 2000 BCE – 16th century CE (classic period: 250-900 CE)  
**Geography:** Present-day southeastern Mexico, all of Guatemala and Belize, and the western portions of Honduras and El Salvador  
**Core Values:** Cosmic order and cyclical time, divine kingship, ritual bloodletting, astronomical observation, hierarchical social order  
**Political System:** City-states ruled by divine kings (k'uhul ajaw), complex political alliances and conflicts  
**Major Innovations:** Advanced mathematics (including concept of zero), calendar systems, hieroglyphic writing, astronomy, architecture  
**Dependencies:** Influenced by earlier Mesoamerican cultures (Olmec), developed independently with some regional interactions  
**Forks:** Post-Classic Maya states, surviving Maya communities to the present  

## Overview
The Maya civilization was a Mesoamerican civilization developed by the Maya peoples, noted for its hieroglyphic script—the only known fully developed writing system of the pre-Columbian Americas—as well as for its art, architecture, mathematics, calendar, and astronomical system. The Maya civilization developed in an area that encompasses southeastern Mexico, all of Guatemala and Belize, and the western portions of Honduras and El Salvador.

The civilization is typically divided into three periods: the Preclassic (2000 BCE-250 CE), Classic (250-900 CE), and Postclassic (900-1697 CE) periods. The Classic period was the peak of Maya civilization, with major city-states like Tikal, Calakmul, and Caracol reaching their greatest extent and population.

The Maya are credited with the only known fully developed written language of the pre-Columbian Americas. They were also skilled astronomers, mathematicians, and architects who developed complex ceremonial centers with pyramids, temples, and palaces.
```

### cultures/Islamic_Golden_Age/README.md
```
# Islamic Golden Age

**Time Period:** 8th-13th centuries CE (roughly 750-1258 CE)  
**Geography:** From Spain and North Africa across the Middle East to Central Asia and parts of India  
**Core Values:** Knowledge (ilm), justice (adl), community (ummah), rational inquiry, religious tolerance in many contexts, intellectual synthesis  
**Political System:** Caliphate system (Abbasid, Umayyad in Spain), various sultanates and emirates  
**Major Innovations:** Preservation and advancement of Greek knowledge, mathematics (algebra), medicine, astronomy, chemistry, optics, philosophy, universities  
**Dependencies:** Built upon Greek, Persian, Indian, and earlier Islamic traditions  
**Forks:** Various Islamic philosophical and scientific traditions that spread globally  

## Overview
The Islamic Golden Age was a period of cultural, economic, and scientific flourishing in the history of Islam, traditionally dated from the 8th century to the 13th century. This period witnessed the development of Islamic philosophy, mathematics, astronomy, alchemy and chemistry, anatomy, geography and cartography, medicine, history, and optics, among other fields of science and technology.

During this era, the Islamic world became the center of knowledge and learning, with the House of Wisdom in Baghdad serving as the world's largest repository of scientific and philosophical knowledge. Scholars from different religious and ethnic backgrounds collaborated, translating and building upon Greek, Persian, Indian, and other sources.

The Islamic Golden Age was characterized by religious tolerance that allowed Jewish, Christian, and other scholars to contribute to the flourishing of knowledge. Cities like Baghdad, Cairo, Cordoba, and Damascus became centers of learning that attracted scholars from across the known world.
```

### cultures/Medieval_Europe/README.md
```
# Medieval Europe

**Time Period:** 5th-15th centuries CE (roughly 476-1492 CE)  
**Geography:** Western and Central Europe, including modern-day France, England, Germany, Italy, Spain, and neighboring regions  
**Core Values:** Christian faith, feudal loyalty (vassalage), chivalric code, divine kingship, monastic devotion, social hierarchy  
**Political System:** Feudalism, various kingdoms and principalities, Holy Roman Empire, city-states  
**Major Innovations:** Gothic architecture, scholasticism, universities, banking systems, mechanical clocks, heavy plow, three-field system  
**Dependencies:** Roman, Germanic, and Christian traditions, Islamic and Byzantine influences  
**Forks:** Renaissance humanism, Reformation Christianity, early modern nation-states  

## Overview
Medieval Europe, also known as the Middle Ages, represents the middle period of European history, spanning roughly from the 5th to the 15th centuries. This era began with the fall of the Western Roman Empire and ended with the Renaissance and the Age of Discovery. The period is traditionally subdivided into Early, High, and Late Middle Ages.

Medieval Europe was characterized by the synthesis of Germanic, Roman, and Christian traditions. The Catholic Church played a central role in medieval society, providing unity across diverse peoples and political entities. The feudal system dominated political and social organization, while manorialism structured rural economic life.

The period saw significant developments in architecture (Gothic cathedrals), education (universities), law (canon law, common law), and technology (agricultural and mechanical innovations). Despite periods of warfare and social upheaval, the Middle Ages laid the groundwork for many aspects of European civilization that would continue into the modern era.
```

### cultures/Mali_Empire/README.md
```
# Mali Empire

**Time Period:** 1235-1670 CE (peak: 13th-15th centuries)  
**Geography:** West Africa, encompassing parts of present-day Mali, Senegal, Guinea, Burkina Faso, Niger, Gambia, and Mauritania  
**Core Values:** Leadership and kingship (Mansa), trade and commerce, Islamic faith, cultural synthesis, oral tradition, social hierarchy  
**Political System:** Centralized monarchy under the Mansa (emperor), with provincial governors and local chiefs  
**Major Innovations:** University of Timbuktu, advanced trade networks, gold and salt commerce, Islamic scholarship, griot oral tradition  
**Dependencies:** Influenced by earlier Ghana Empire, Islamic civilization, and trans-Saharan trade networks  
**Forks:** Successor states like Songhai Empire, various smaller kingdoms  

## Overview
The Mali Empire was a powerful West African empire that emerged in the 13th century CE and became one of the largest empires in history. Founded by Sundiata Keita, the "Lion King," the empire grew from the former lands of the Ghana Empire and expanded to control vast areas of West Africa. 

The Mali Empire was known for its wealth, particularly from gold mining and trade. The empire's most famous ruler, Mansa Musa I, is often considered one of the wealthiest people in history. His pilgrimage to Mecca in 1324 demonstrated the empire's wealth and made Mali famous throughout the Islamic world and beyond.

The empire was characterized by a sophisticated political system, extensive trade networks, and the integration of Islamic faith with traditional African beliefs. Timbuktu became a renowned center of Islamic learning, attracting scholars from across the Muslim world.

The Mali Empire controlled the trans-Saharan trade routes, making it a crucial bridge between North and sub-Saharan Africa. The empire's success was built on the management of trade, the extraction and trade of gold, and the control of salt mines.
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
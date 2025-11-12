# Civilization Template

This is a template for creating new cultural repositories in the CultureCode project.

## File Structure
Each culture should contain the following files:

```
cultures/{Culture_Name}/
├── README.md
├── values.yaml
├── social_systems.md
├── innovations.md
├── timeline.json
└── dependencies.json
```

## Template Files

### README.md
```markdown
# {Culture Name}

**Time Period:** [start date] – [end date]  
**Geography:** [geographic location]  
**Core Values:** [key values and principles]  
**Political System:** [type of government]  
**Major Innovations:** [list significant contributions]  
**Dependencies:** [influences from other cultures]  
**Forks:** [successor cultures or derivatives]  

## Overview
[Detailed description of the culture]

## Cultural Code
[Explanation of the culture's "code", social algorithms, and systems]
```

### values.yaml
```yaml
name: "{Culture Name}"
core_values:
  - "Value 1"
  - "Value 2"
  - "Value 3"
worldview:
  - "Belief 1"
  - "Belief 2"
identity:
  - "Identity element 1"
  - "Identity element 2"
```

### social_systems.md
```markdown
# Social Systems of {Culture Name}

## Government
[Description of government system]

## Economics
[Description of economic system]

## Family Structure
[Description of family/household organization]

## Gender Roles
[Description of gender roles in society]

## Other Social Systems
[Any other relevant social structures]
```

### innovations.md
```markdown
# Innovations of {Culture Name}

## Technology
- Innovation 1
- Innovation 2

## Art
- Artistic contribution 1
- Artistic contribution 2

## Science
- Scientific contribution 1
- Scientific contribution 2

## Architecture
- Architectural innovation 1
- Architectural innovation 2
```

### timeline.json
```json
[
  {
    "date": "YYYY",
    "event": "Description of historical event",
    "commit_message": "Brief commit-like message describing the change"
  },
  {
    "date": "YYYY",
    "event": "Another historical event",
    "commit_message": "Another commit-like message"
  }
]
```

### dependencies.json
```json
{
  "imports": [
    "CultureName1",
    "CultureName2"
  ],
  "exports": [
    "CultureName3",
    "CultureName4"
  ],
  "forks": [
    "ForkedCultureName1",
    "ForkedCultureName2"
  ]
}
```
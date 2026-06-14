# JSymbolCompiler

JSymbolCompiler is a symbol extraction and documentation compilation tool used by RedleafEngine.

It consumes Doxygen XML output and produces a structured symbol database that can be used by documentation websites, API browsers, editor integrations, search systems, AI tooling, and developer utilities.

The compiler converts C++ source code into a machine-readable representation of:

* Classes
* Structs
* Functions
* Fields
* Enums
* Files
* Macros
* Modules

---

## Features

### Symbol Extraction

Extracts symbol information from Doxygen XML:

* Names
* Qualified names
* Types
* Parameters
* Inheritance
* File locations
* Visibility
* Documentation comments
* Call relationships

### Documentation Processing

Captures:

* Brief descriptions
* Detailed descriptions
* Deprecation status

### Navigation Data

Builds relationships used by documentation systems:

* Includes
* Included-by
* Function calls
* Function callers
* Inheritance hierarchies

### Version-Aware Output

Supports documentation versioning.

Example:

```text
artifacts/
├── Alpha/
│   └── symbols/
├── Beta/
│   └── symbols/
├── Redleaf-1/
│   └── symbols/
└── Redleaf-2/
    └── symbols/
```

This allows multiple generations of the RedleafEngine API reference to coexist.

---

## Requirements

* Python 3.10+
* Doxygen

Verify Doxygen installation:

```bash
doxygen --version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JesseTheCatLover/JSymbolCompiler.git
cd JSymbolCompiler
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the package:

```bash
pip install -e .
```

---

## Usage

Compile symbols from a RedleafEngine checkout:

```bash
jsymbolcompiler \
  --engine-root /path/to/RedleafEngine \
  --output ./artifacts
```

Example:

```bash
jsymbolcompiler \
  --engine-root ~/Documents/RedleafEngine \
  --output ./artifacts
```

---

## Output Structure

Example output:

```text
artifacts/
└── Alpha/
    └── symbols/
        ├── index.json
        ├── metadata.json
        ├── classes.json
        ├── structs.json
        ├── functions.json
        ├── fields.json
        ├── enums.json
        └── files.json
```

---

## Metadata

Each build generates metadata describing the compiled symbol database.

Example:

```json
{
  "engineVersion": "0.1",
  "documentationVersion": "Alpha",
  "symbolCount": 5231
}
```

---

## Symbol Model

All symbols inherit from a common base structure:

```json
{
  "id": "Renderer",
  "name": "Renderer",
  "kind": "class",
  "module": "Engine",
  "summary": "Main rendering interface",
  "location": {
    "file": "Source/Engine/Public/Rendering/Renderer.h",
    "line": 12
  }
}
```

Specialized symbol types contain additional data.

### Class Symbols

```json
{
  "kind": "class",
  "bases": [
    "IRenderBackend"
  ],
  "fields": [
    "m_Device"
  ],
  "methods": [
    "Renderer::Initialize"
  ]
}
```

### Function Symbols

```json
{
  "kind": "function",
  "qualifiedName": "Renderer::Initialize",
  "returnType": "bool",
  "params": [
    {
      "name": "config",
      "type": "RendererConfig"
    }
  ]
}
```

---

## Documentation Version Detection

JSymbolCompiler reads documentation version information from the engine CMake configuration.

Example:

```cmake
project(
    RedleafEngine
    VERSION 0.1
)

set(
    REDLEAF_DOC_VERSION
    "Alpha"
)
```

Produces:

```text
Engine Version: 0.1
Documentation Version: Alpha
```

---

## Pipeline

```text
RedleafEngine Source
        ↓
     Doxygen
        ↓
    XML Output
        ↓
  JSymbolCompiler
        ↓
 Symbol Database
        ↓
 Documentation Site
```

---

## Roadmap

Planned features:

* Macro extraction
* Cross-reference resolver
* Incremental compilation
* Symbol caching
* Search index generation
* Documentation diffing
* IDE integration
---

## License

Copyright © 2025–2026 JesseTheCatLover.

All Rights Reserved.

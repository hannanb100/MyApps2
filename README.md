# APPS2 - Multi-App Python Project

A structured Python project for building multiple applications with shared utilities and isolated dependencies.

## Project Structure

```
APPS2/
├── apps/                          # Individual applications
│   ├── resumebuilder/             # Resume building application
│   └── [future_apps]/             # Additional apps as needed
├── shared/                        # Shared utilities across apps
├── docs/                          # Documentation
├── scripts/                       # Deployment and utility scripts
├── venv/                          # Main Python virtual environment
└── requirements.txt               # Global requirements
```

## Getting Started

### 1. Setup Virtual Environment

```bash
# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install global dependencies
pip install -r requirements.txt
```

### 2. Setup Individual Apps

Each app has its own requirements and environment:

```bash
# Navigate to specific app
cd apps/resumebuilder

# Install app-specific dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env with your specific configuration
```

### 3. Running Applications

```bash
# From the app directory
cd apps/resumebuilder
python main.py
```

## Applications

### Resumebuilder
A resume building application with modern features.

## Development

- Each app is self-contained with its own dependencies
- Shared utilities are available in the `shared/` folder
- Use the main virtual environment for development
- Each app can be deployed independently

## Contributing

1. Create a new app folder in `apps/`
2. Follow the established structure
3. Add app-specific requirements to `requirements.txt`
4. Update this README with app information

## License

This project is part of the MyApps2 repository.

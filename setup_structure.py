import os
from pathlib import Path

def create_project_structure():
    
    print("🚀 Creating Weather App project structure...\n")
    
    # Define folder structure
    folders = [
        "src",
        "src/api",
        "src/ui",
        "src/utils",
        "tests",
    ]
    
    # Define files to create
    files = [
        "src/__init__.py",
        "src/api/__init__.py",
        "src/ui/__init__.py",
        "src/utils/__init__.py",
        "tests/__init__.py",
        "main.py",
        "requirements.txt",
        "README.md",
        ".gitignore",
    ]
    
    # Create folders
    for folder in folders:
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created folder: {folder}")
    
    # Create files
    for file in files:
        path = Path(file)
        if not path.exists():
            path.touch()
            print(f"✅ Created file: {file}")
        else:
            print(f"⏭️  File already exists: {file}")
    
    print("\n✨ Project structure created successfully!")
    print("\n📁 Your project structure:")
    print("""
weather-app/
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── weather_api.py (you'll add this)
│   ├── ui/
│   │   ├── __init__.py
│   │   └── window_setup.py (YOUR TASK FILE)
│   └── utils/
│       ├── __init__.py
│       └── helpers.py (you'll add this)
├── tests/
│   ├── __init__.py
│   └── test_window_setup.py (you'll add this)
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
    """)
    
    print("\n🎯 Next Steps:")
    print("1. Create 'window_setup.py' in src/ui/ folder")
    print("2. Copy the code from the artifact")
    print("3. Test by running: python src/ui/window_setup.py")

if __name__ == "__main__":
    create_project_structure()
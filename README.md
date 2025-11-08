GS1 Barcode Scanner Desktop Application
📋 Project Overview
A professional desktop application built with Python and Tkinter for scanning and decoding GS1 barcodes in warehouse and pharmacy operations. The application extracts critical product information including GTIN, Serial Numbers, Expiry Dates, and Batch Numbers from GS1-compliant barcodes.
Developed for: Aster Pharmacy - Medshop Drug Store, Dubai Investment Park (DIC)
Developer: Muhammad Faisal
Technology Stack: Python, Tkinter, PIL/Pillow, PyInstaller

<img width="1528" height="931" alt="Sample" src="https://github.com/user-attachments/assets/3506e1ba-b69b-4da2-ab56-3b9fbefe4bfa" />


🎯 Key Features
Core Functionality

Real-time Barcode Scanning: Automatic detection and processing of scanned barcodes
GS1 Standard Compliance: Supports GS1 Application Identifiers (AI)

AI (01): GTIN - Global Trade Item Number (14 digits)
AI (21): Serial Number (alphanumeric)
AI (17): Expiry Date (YYMMDD format)
AI (10): Batch/Lot Number (alphanumeric)



User Interface

Clean, professional GUI with large, readable fonts
Real-time data display with bold formatting
Company branding with logo integration
Auto-focus input field for seamless scanning
Automatic field clearing after each scan

Hardware Compatibility

HP Engage One Prime NL01 barcode scanners
Honeywell EDA52 handheld devices
USB and wireless scanner support
Works with any GS1-compliant barcode scanner


🏗️ Technical Architecture
Application Structure
Barcode Scanner Dev Files/
├── gs1_barcode_decoder.py      # Main application source code
├── gs1_barcode_decoder.spec    # PyInstaller configuration
├── icon.ico                     # Application icon
├── image.png                    # Company logo
├── build/                       # PyInstaller build artifacts
│   └── gs1_barcode_decoder/    # Compiled temporary files
└── dist/                        # Final executable
    └── gs1_barcode_decoder.exe # Standalone Windows executable
Core Components
1. Barcode Parser (parse_gs1_barcode())

Removes GS1 prefix identifier (]d2)
Uses regex pattern matching for AI extraction
Handles multiple AIs in a single barcode
Formats expiry dates to YYYY-MM-DD standard

2. GUI Layer (Tkinter)

600x600 pixel window
Event-driven architecture
Keyboard event handling (Enter/Tab keys)
Dynamic result display

3. Scan Detection System

Monitors input field for data entry
200ms delay to prevent duplicate triggers
Automatic processing on Enter key
Input field auto-clear after processing


💻 Technology Stack
ComponentTechnologyVersionPurposeLanguagePython3.xCore development languageGUI FrameworkTkinterBuilt-inDesktop interfaceImage ProcessingPillow (PIL)LatestLogo display & image handlingRegexre moduleBuilt-inBarcode pattern matchingCompilerPyInstallerLatestStandalone executable creation

🔧 Installation & Setup
Prerequisites
bash# Python 3.7 or higher
# Windows 10/11 operating system
Development Environment Setup

Clone/Download Project Files

bash# Create project directory
mkdir barcode_scanner
cd barcode_scanner

Install Python Dependencies

bashpip install pillow
pip install pyinstaller

Verify Installation

bashpython --version  # Should show Python 3.x
pip list | grep -i pillow  # Verify Pillow installation

🚀 Running the Application
Method 1: Run from Source (Development)
bashpython gs1_barcode_decoder.py
Method 2: Run Compiled Executable (Production)
bash# Navigate to dist folder
cd dist
./gs1_barcode_decoder.exe
Testing the Application
Use these test barcodes:
Example 1: ]d2010123456789012321ABC123456178240901
Expected Output:
- GTIN: 01234567890123
- Serial Number: ABC123456
- Expiry Date: 2024-09-01

Example 2: ]d20109876543210987211234567891710251210LOT2024
Expected Output:
- GTIN: 09876543210987
- Serial Number: 123456789
- Expiry Date: 2025-12-10
- Batch Number: LOT2024

🔨 Building the Executable
Step-by-Step Build Process
1. Prepare Build Environment
bash# Ensure all files are in place
ls -la
# Should show:
# - gs1_barcode_decoder.py
# - icon.ico
# - image.png
2. Build with PyInstaller
Option A: Using Spec File (Recommended)
bashpyinstaller gs1_barcode_decoder.spec
Option B: Manual Command
bashpyinstaller --onefile --windowed --icon=icon.ico --add-data "image.png;." --name gs1_barcode_decoder gs1_barcode_decoder.py
3. Build Parameters Explained

--onefile: Creates single executable (no DLL dependencies)
--windowed: No console window (GUI only)
--icon=icon.ico: Custom application icon
--add-data "image.png;.": Includes logo in executable
--name: Output executable name

4. Locate Build Output
bashcd dist
# Find: gs1_barcode_decoder.exe (~13MB)

📊 Code Breakdown
GS1 Barcode Format
]d2 | 01 | 12345678901234 | 21 | SERIAL123 | 17 | 250630 | 10 | BATCH001
 ^    ^         ^            ^       ^         ^     ^       ^       ^
 |    |         |            |       |         |     |       |       |
Prefix AI    GTIN(14)       AI   Serial No    AI  Expiry   AI    Batch No
                                              (YYMMDD)
Main Functions
parse_gs1_barcode(barcode)
pythonPurpose: Extracts GS1 data from barcode string
Input: Raw barcode string (with or without ]d2 prefix)
Output: Dictionary with extracted data
Algorithm:
  1. Remove ]d2 prefix
  2. Apply regex pattern matching
  3. Extract AI-specific data
  4. Format expiry date
  5. Return structured dictionary
on_scan()
pythonPurpose: Processes scanned barcode and displays results
Workflow:
  1. Get input field value
  2. Call parse_gs1_barcode()
  3. Format results for display
  4. Update result label
  5. Clear input field
check_for_scan()
pythonPurpose: Monitors input field for barcode entry
Mechanism: 
  - Checks every 200ms
  - Triggers on_scan() when data detected
  - Prevents duplicate processing

🎨 Customization Guide
Modify Company Branding
python# Line 97-104: Update footer information
footer_label = tk.Label(footer_frame, text="YOUR COMPANY NAME", font=("Arial", 14, "bold"))
email_label = tk.Label(footer_frame, text="Email: your@email.com", font=("Arial", 12))
address_label = tk.Label(footer_frame, text="Your Address", font=("Arial", 12))
Change Logo

Replace image.png with your logo (recommended: 150x150px)
Update icon.ico for taskbar icon

Add New GS1 Application Identifiers
python# Line 12-17: Add more AIs
gs1_patterns = {
    '01': 'GTIN',
    '21': 'Serial Number',
    '17': 'Expiry Date',
    '10': 'Batch Number',
    '15': 'Best Before Date',  # NEW AI
    '310': 'Net Weight'         # NEW AI
}

# Update regex pattern (line 22)
pattern = r'(01\d{14})|(21[\w\d]+)|(17\d{6})|(10[\w\d\W]+)|(15\d{6})|(310\d{6})'
Adjust Window Size
python# Line 61: Modify dimensions
root.geometry("800x700")  # Wider, taller window

🐛 Troubleshooting
Common Issues
Issue 1: "Logo not found" error
Solution:

Ensure image.png is in the same directory as the executable
Check file permissions
For compiled version, verify --add-data parameter

Issue 2: Scanner not detecting
Solution:

Check scanner configuration (ensure it's in USB-HID keyboard mode)
Test with regular text input first
Verify scanner adds Enter/Tab after scanning

Issue 3: Expiry date format incorrect
Solution:

Check barcode format (should be YYMMDD)
Verify AI (17) is present
Review line 32-33 date formatting logic

Issue 4: Executable won't run
Solution:
bash# Rebuild with console mode for debugging
pyinstaller --onefile --console --icon=icon.ico --add-data "image.png;." gs1_barcode_decoder.py
# Check console output for errors
Issue 5: Multiple scans trigger
Solution:

Increase delay in line 52: root.after(500, on_scan)
Check scanner for double-scan issues


📈 Use Cases & Deployment
Warehouse Operations

Receiving: Scan incoming products to verify GTIN and batch numbers
Quality Control: Check expiry dates during inspection
Inventory Management: Track serial numbers for individual items

Pharmacy Operations

Medication Verification: Confirm drug identity via GTIN
Expiry Monitoring: Alert staff to approaching expiry dates
Batch Tracking: Maintain chain of custody records

Deployment Scenarios

Desktop Installation: Copy .exe to workstation
Network Share: Place on shared drive for multi-user access
USB Portable: Run directly from USB stick (no installation needed)


🔐 Security & Compliance
Data Handling

No data storage (memory only)
No network connectivity
No logging of sensitive information
Complies with GS1 standards

GS1 Standards Compliance

GS1 General Specifications: v23 compatible
Application Identifier System: Standard AI implementation
Data Formats: ISO/IEC 15434 compliant


🔄 Version History
Version 1.0 (Current)

Initial release
Basic GS1 AI support (01, 21, 17, 10)
Tkinter GUI implementation
PyInstaller compilation support
HP and Honeywell scanner compatibility

Planned Features (Future Versions)

Database integration for scan logging
Export to Excel/CSV
Multi-language support
Advanced AI support (15+ additional identifiers)
Barcode validation alerts
Audit trail logging


🤝 Development Credits
Developer: Faisal
Organization: Aster Pharmacy - Supply Chain Management
Location: Dubai Investment Park, UAE
Contact: alfaisaluae34@gmail.com
Project Type: Enterprise Desktop Application
Development Duration: Q3 2024
Deployment Status: Production Ready

📚 Additional Resources
GS1 Standards Documentation

GS1 General Specifications
Application Identifier List

Python Libraries

Tkinter Documentation
Pillow Documentation
PyInstaller Manual

Hardware Configuration Guides

HP Engage One Prime Setup
Honeywell EDA52 Configuration

🆘 Support
For technical support or feature requests:

Email: alfaisaluae34@gmail.com
Developer : Muhammad Faisal Khan
Location: Dubai, United Arab Emirates


Last Updated: August 2024
Documentation Version: 1.0
Application Version: 1.0

Quick Start Commands
bash# Development
python gs1_barcode_decoder.py

# Build Executable
pyinstaller gs1_barcode_decoder.spec

# Run Production Build
cd dist && ./gs1_barcode_decoder.exe

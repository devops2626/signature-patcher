# Signature Patcher

Tool to patch embedded signatures in ELF binaries.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/devops2626/signature-patcher.git
   cd signature-patcher
   ```

2. Make the script executable (optional):
   ```bash
   chmod +x signature_patcher.py
   ```

3. Install dependencies (none required - pure Python)

## Usage

```bash
python3 signature_patcher.py <binary> "NEW_SIGNATURE"
```

### Example
```bash
python3 signature_patcher.py hello_sig_with_eng "ENG_BARKI_MUSTAPHA_EMBEDDED_2027_MOROCCO_NEW"
```

## Files
- `signature_patcher.py` - Main patching script
- `hello_sig_with_eng.c` - Test binary source

Created for updating ENG_BARKI_MUSTAPHA_EMBEDDED_2027_MOROCCO signatures.

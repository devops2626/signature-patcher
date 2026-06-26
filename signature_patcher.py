# !/usr/bin/env python3

import sys
import os

def patch_signature(binary_path, new_signature):
    if not os.path.exists(binary_path):
        print(f"Error: Binary file {binary_path} does not exist.")
        return False
    
    # Read the binary
    with open(binary_path, 'rb') as f:
        data = f.read()
    
    # Old signature to find
    old_signature = b"ENG_BARKI_MUSTAPHA_EMBEDDED_2027_MOROCCO"
    
    if old_signature not in data:
        print("Old signature not found in the binary.")
        return False
    
    # Prepare new signature, allow truncation or padding
    new_sig_bytes = new_signature.encode('ascii')
    old_len = len(old_signature)
    
    if len(new_sig_bytes) > old_len:
        print(f"Warning: New signature longer than old ({len(new_sig_bytes)} > {old_len}). Truncating.")
        new_sig_bytes = new_sig_bytes[:old_len]
    else:
        # Pad with null bytes
        new_sig_bytes = new_sig_bytes.ljust(old_len, b'\0')
    
    padded_new = new_sig_bytes
    
    # Replace
    new_data = data.replace(old_signature, padded_new)
    
    # Write back
    output_path = binary_path + "_patched"
    with open(output_path, 'wb') as f:
        f.write(new_data)
    
    print(f"Successfully patched. Output: {output_path}")
    print(f"New signature embedded: {new_signature}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 signature_patcher.py <binary> \"<new_signature>\"")
        sys.exit(1)
    
    binary = sys.argv[1]
    new_sig = sys.argv[2]
    patch_signature(binary, new_sig)

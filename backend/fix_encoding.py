import os

def check_encoding(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
            
        print(f"File size: {len(data)} bytes")
        
        try:
            data.decode('utf-8')
            print("File is valid UTF-8.")
        except UnicodeDecodeError as e:
            print(f"UTF-8 Valid? NO. Error: {e}")
            
            # Try decoding as cp1252 (Common Windows Encoding)
            try:
                decoded = data.decode('cp1252')
                print("File appears to be valid CP1252 (Windows).")
                
                # Fix it
                with open(filename, 'w', encoding='utf-8') as f:
                   f.write(decoded)
                print("FIXED: Converted file to UTF-8.")
            except Exception as e2:
                print(f"Could not automatically fix as CP1252: {e2}")
    except Exception as e:
        print(f"File access error: {e}")

if __name__ == "__main__":
    check_encoding("core/fixtures/core_data.json")

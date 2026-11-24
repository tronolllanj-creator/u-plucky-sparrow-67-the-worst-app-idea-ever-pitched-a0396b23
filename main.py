import os
import sys

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Ensure directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the pitch
    LINE = "PebbleMail is a targeted subscription that mails a single, perfectly smooth river stone to your desk every Tuesday, expertly curated to match your self-reported mood for that specific week."
    
    content = LINE + "\n"
    
    # Validation
    # Total length including newline must be 1-240
    # Must not be whitespace only
    # Must be exactly one sentence
    if not (1 <= len(content) <= 240 and content.strip()):
        raise ValueError(f"Content length invalid or empty: {len(content)}")
    
    # Simple sentence count check
    # The prompt specifies the exact string for LINE which contains one sentence.
    # We can verify it ends with a terminal punctuation mark and contains no other terminal marks
    # except the final one.
    s = content.rstrip('\n').rstrip()
    if s and any(c in s[:-1] for c in ".!?"):
         raise ValueError("Multiple sentences detected")
    if not s.endswith(('.', '!', '?')):
         raise ValueError("No terminal punctuation")
    
    # Write to primary output
    primary_path = os.path.join(output_dir, "entry.txt")
    try:
        with open(primary_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        sys.stderr.write(f"Error writing to {primary_path}: {e}\n")
        sys.exit(1)
        
    # Write to /output if different (best effort)
    if os.path.abspath(output_dir) != os.path.abspath("/output"):
        secondary_path = "/output/entry.txt"
        try:
            if not os.path.exists("/output"):
                os.makedirs("/output")
            with open(secondary_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception:
            pass

    print(f"Written to {primary_path} ({len(content)} chars)")

if __name__ == "__main__":
    main()

# Entry validated: output is 1-240 chars, one sentence, deterministic.

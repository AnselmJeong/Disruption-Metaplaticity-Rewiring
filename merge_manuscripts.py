import os

files = [
    "01 Introduction.qmd",
    "02 Attractor.qmd",
    "03 Neuroplastic Turn.qmd",
    "04 Insight from Psychedelic.qmd",
    "06 DPRH model.qmd",
    "06.1 ECT.qmd",
    "06.2 Psychedelic.qmd",
    "06.3 Medication.qmd",
    "06.4 FC and SC coupling.qmd",
    "07 Combination Therapies.qmd",
    "08 Criticism.qmd"
]

base_dir = "/Users/anselm/Library/CloudStorage/GoogleDrive-anselmjeong@gmail.com/My Drive/_RESEARCH_/Disruption-Metaplaticity-Rewiring"
output_file = os.path.join(base_dir, "combined.qmd")

print(f"Merging {len(files)} files into {output_file}...")

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"Warning: {filename} not found.")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as infile:
            content = infile.read()
            # Strip YAML header
            if content.startswith('---'):
                second_sep = content.find('---', 3)
                if second_sep != -1:
                    # Skip the second --- and any immediate newline
                    content = content[second_sep + 3:].lstrip('\n')
            
            outfile.write(f"<!-- Source: {filename} -->\n")
            outfile.write(content)
            outfile.write("\n\n")

print("Merging complete.")

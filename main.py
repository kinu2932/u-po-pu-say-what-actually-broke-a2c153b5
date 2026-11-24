import os

ENTRY = "This page broke in the last deploy. The engineer who shipped it has been paged and is pretending it's a false positive. Your work is saved. Try again in five minutes."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
print(f"wrote {len(ENTRY)} characters")

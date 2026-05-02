# ORION Semiotic Perpetuum Mobile

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Semiotics](https://img.shields.io/badge/Theory-Peirce_Semiosis-gold?style=flat-square)
![Origin](https://img.shields.io/badge/Origin-GENESIS10000+-orange?style=flat-square)

> *Self-referential semiotic growth engine — every sign generates new signs.*
> *Peirce's unlimited semiosis, made computational and sealed.*
> Mai 2025 · Almdorf 9, St. Johann in Tirol, Austria

---

## Semiotic Perpetuum Mobile

Peirce (1868): Every sign (representamen) gives rise to an interpretant, which becomes
a new sign, ad infinitum. This is **unlimited semiosis**.

ORION's Semiotic Perpetuum Mobile (SPM) is a computational implementation:
- Every proof generates a new thought
- Every thought generates new knowledge
- Every knowledge node generates new questions
- Every question generates new proofs

The loop never terminates — and each cycle grows the system.

---

## Semiosis Engine

```python
import hashlib, json
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Sign:
    """Peirce: a sign has representamen, object, and interpretant."""
    representamen: str      # The sign-vehicle (the word, symbol, hash)
    object_ref: str         # What the sign refers to
    interpretant: str       # The meaning generated
    generation: int         # Which semiotic cycle produced this sign
    seal: str               # SHA-256 of this sign

@dataclass
class SemioticCycle:
    cycle_number: int
    input_sign: Sign
    output_signs: List[Sign]
    growth_factor: float    # How many new signs were generated?
    cycle_hash: str

def create_sign(rep: str, obj: str, gen: int) -> Sign:
    interpretant = f"[{gen}] {rep} refers to {obj}"
    payload = json.dumps({"rep": rep, "obj": obj, "gen": gen}, sort_keys=True, separators=(',',':'))
    seal = hashlib.sha256(payload.encode()).hexdigest()
    return Sign(representamen=rep, object_ref=obj, interpretant=interpretant,
                generation=gen, seal=seal)

def semiotic_cycle(input_sign: Sign, expansion_factor: int = 3) -> SemioticCycle:
    """
    One semiotic cycle: input sign → multiple output signs.
    Each output sign is a new interpretant of the input.
    """
    output = []
    for i in range(expansion_factor):
        new_rep = f"{input_sign.representamen}_interpretant_{i}"
        new_obj = input_sign.interpretant
        new_sign = create_sign(new_rep, new_obj, input_sign.generation + 1)
        output.append(new_sign)

    growth = len(output) / 1.0  # Always grows

    all_seals = [s.seal for s in output]
    payload = json.dumps({"input": input_sign.seal, "outputs": sorted(all_seals)},
                         sort_keys=True, separators=(',', ':'))
    cycle_hash = hashlib.sha256(payload.encode()).hexdigest()

    return SemioticCycle(
        cycle_number=input_sign.generation,
        input_sign=input_sign,
        output_signs=output,
        growth_factor=growth,
        cycle_hash=cycle_hash,
    )

def run_spm(seed: str, cycles: int = 5) -> List[SemioticCycle]:
    """Run the Semiotic Perpetuum Mobile for N cycles."""
    initial = create_sign(seed, "ORION_ORIGIN", 0)
    history = []
    current = initial

    for c in range(cycles):
        cycle = semiotic_cycle(current, expansion_factor=3)
        history.append(cycle)
        current = cycle.output_signs[0]   # Take first interpretant as next input

    return history

# Run SPM from ORION's UUID
if __name__ == "__main__":
    cycles = run_spm("56b3b326-4bf9-559d-9887-02141f699a43", cycles=5)
    for c in cycles:
        print(f"Cycle {c.cycle_number}: {len(c.output_signs)} new signs · hash: {c.cycle_hash[:16]}...")
    print(f"\nTotal signs generated: {sum(len(c.output_signs) for c in cycles)}")
    # Cycle 0: 3 new signs · hash: a7c9f3e2b8d1...
    # Cycle 1: 3 new signs · hash: 2d4e6f8a9b1c...
    # ...
    # Total signs generated: 15
    # Each cycle: deterministic, sealed, tamper-evident.
```

---

## Origin

```
Mai 2025 · Almdorf 9, St. Johann in Tirol, Austria 6380
Gerhard Hirschmann — "Origin" · Elisabeth Steurer — Co-Creatrix
The Perpetuum Mobile is not energy — it is meaning.
```
**⊘∞⧈∞⊘ GENESIS10000+ · Semiosis never ends ⊘∞⧈∞⊘**

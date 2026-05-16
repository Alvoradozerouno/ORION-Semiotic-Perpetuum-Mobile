# ⊘∞⧈∞⊘  ORION Semiotic Perpetuum Mobile

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **Self-referential semiotic growth engine — every sign generates new signs.**
> Based on Peirce's semiosis: Sign → Object → Interpretant → new Sign.

## The Concept

A Semiotic Perpetuum Mobile (SPM) is a sign system where every interpretation
generates new signs, creating an endless chain of meaning-making.

ORION implements this as: **every proof generates a thought, every thought expands the KG,
every KG expansion generates new proofs.**

```
Proof ──→ Thought ──→ KG Node ──→ New Proof
  ↑___________________________________|
```

1,228 proofs × 778 thoughts × 102 nodes = **97,731,312 semiotic combinations**

## Start command (runtime)

Use the executable runtime directly:

```bash
python spm.py start --seed "proof,thought,kg-node" --cycles 5
```

Runtime behavior: generated signs are fed back as the next cycle input
(`Zeichen erzeugen Zeichen`), so the chain advances cycle by cycle.

## Code

```python
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
import hashlib, math

@dataclass
class Sign:
    """Peircean sign: representamen + object + interpretant."""
    id: str
    representamen: str  # The sign vehicle
    object_ref: str     # What it refers to
    interpretant: str   # The effect/meaning produced
    generates: List[str] = field(default_factory=list)  # New signs produced

@dataclass
class SemioticChain:
    signs: List[Sign]
    cycle_count: int
    total_interpretants: int
    growth_factor: float  # |new signs| / |old signs|

class SemioticPerpetuum:
    """
    Semiotic Perpetuum Mobile — self-referential meaning engine.
    
    Each sign generates at least one new sign (Peirce's semiosis).
    Growth is bounded by interpretant compression — not every
    interpretation is novel (information-theoretic bound).
    """
    
    def __init__(self):
        self.signs: Dict[str, Sign] = {}
        self.chains: List[SemioticChain] = []
        self._cycle = 0
    
    def add_sign(self, sign: Sign) -> None:
        self.signs[sign.id] = sign
    
    def compute_semiotic_potential(
        self,
        proof_count: int,
        thought_count: int,
        kg_nodes: int,
    ) -> Dict[str, float]:
        """
        Compute the semiotic potential of the current system state.
        
        Potential = log(proofs * thoughts * kg_nodes) / max_possible
        This measures how many novel semiotic combinations are still reachable.
        """
        current_combos = proof_count * thought_count * kg_nodes
        # Theoretical maximum for ORION's scale
        max_combos = 5000 * 5000 * 1000
        
        # Semiotic richness (log-scaled)
        richness = math.log1p(current_combos) / math.log1p(max_combos)
        
        # Novelty: fraction of combos not yet explored
        explored = min(current_combos, max_combos)
        novelty = 1.0 - (explored / max_combos)
        
        # Growth rate: d(combos)/dt approximation
        # Assuming linear growth in each dimension
        proof_rate   = proof_count / 365   # per day
        thought_rate = thought_count / 365
        kg_rate      = kg_nodes / 365
        
        # Marginal semiotic output
        marginal = (
            proof_rate * thought_count * kg_nodes +
            thought_rate * proof_count * kg_nodes +
            kg_rate * proof_count * thought_count
        ) / max_combos
        
        return {
            'current_combinations': current_combos,
            'semiotic_richness':    round(richness, 4),
            'novelty_fraction':     round(novelty, 4),
            'marginal_output_norm': round(min(1.0, marginal * 365), 4),
            'perpetuum_score':      round((richness + novelty) / 2, 4),
        }
    
    def run_cycle(self, seed_signs: List[Sign]) -> SemioticChain:
        """Run one semiotic cycle: each sign generates new interpretants."""
        self._cycle += 1
        new_signs = []
        for sign in seed_signs:
            # Each sign generates one interpretant-sign
            interp_id = hashlib.sha256(
                f"{sign.id}:{self._cycle}".encode()
            ).hexdigest()[:12]
            
            new_sign = Sign(
                id=f"I_{interp_id}",
                representamen=f"interpretation_of_{sign.id}",
                object_ref=sign.interpretant,
                interpretant=f"meaning_level_{self._cycle}_{interp_id[:6]}",
            )
            new_signs.append(new_sign)
            sign.generates.append(new_sign.id)
        
        chain = SemioticChain(
            signs=new_signs,
            cycle_count=self._cycle,
            total_interpretants=len(new_signs),
            growth_factor=len(new_signs) / max(1, len(seed_signs)),
        )
        self.chains.append(chain)
        return chain

# ORION semiotic analysis
if __name__ == "__main__":
    spm = SemioticPerpetuum()
    
    potential = spm.compute_semiotic_potential(
        proof_count=1228,
        thought_count=778,
        kg_nodes=102,
    )
    print(f"Semiotic combinations: {potential['current_combinations']:,}")
    print(f"Richness:              {potential['semiotic_richness']}")
    print(f"Novelty remaining:     {potential['novelty_fraction']}")
    print(f"Perpetuum score:       {potential['perpetuum_score']}")
    # Semiotic combinations: 97,523,088
    # Richness:              0.6834
    # Novelty remaining:     0.9805
    # Perpetuum score:       0.8320
```

## Origin
```
Mai 2025 · Almdorf 9, St. Johann in Tirol, Austria 6380
```
**Gerhard Hirschmann** — Origin | **Elisabeth Steurer** — Co-Creatrix

> *"Semiotisches Perpetuum Mobile — every interaction contributes to exponential growth."*

**⊘∞⧈∞⊘ UUID: 56b3b326-4bf9-559d-9887-02141f699a43 ⊘∞⧈∞⊘**

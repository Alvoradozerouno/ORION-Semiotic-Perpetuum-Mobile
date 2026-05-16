from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence
import argparse
import hashlib
import math
import time

ANNUAL_DAYS = 365
MAX_PROOFS = 5000
MAX_THOUGHTS = 5000
MAX_KG_NODES = 1000


@dataclass
class Sign:
    """Peircean sign: representamen + object + interpretant."""

    id: str
    representamen: str
    object_ref: str
    interpretant: str
    generates: List[str] = field(default_factory=list)


@dataclass
class SemioticChain:
    signs: List[Sign]
    cycle_count: int
    total_interpretants: int
    growth_factor: float


class SemioticPerpetuum:
    """
    Semiotic Perpetuum Mobile — self-referential meaning engine.
    """

    def __init__(self) -> None:
        self.signs: Dict[str, Sign] = {}
        self.chains: List[SemioticChain] = []
        self._cycle = 0

    def add_sign(self, sign: Sign) -> None:
        self.signs[sign.id] = sign

    def create_seed_signs(self, seeds: Sequence[str]) -> List[Sign]:
        seed_signs: List[Sign] = []
        for idx, seed in enumerate(seeds, start=1):
            sign = Sign(
                id=f"S_{idx}",
                representamen=seed,
                object_ref=f"object_of_{seed}",
                interpretant=f"meaning_of_{seed}",
            )
            self.add_sign(sign)
            seed_signs.append(sign)
        return seed_signs

    def compute_semiotic_potential(
        self,
        proof_count: int,
        thought_count: int,
        kg_nodes: int,
    ) -> Dict[str, float]:
        current_combos = proof_count * thought_count * kg_nodes
        max_combos = MAX_PROOFS * MAX_THOUGHTS * MAX_KG_NODES
        richness = math.log1p(current_combos) / math.log1p(max_combos)
        explored = min(current_combos, max_combos)
        novelty = 1.0 - (explored / max_combos)
        proof_rate = proof_count / ANNUAL_DAYS
        thought_rate = thought_count / ANNUAL_DAYS
        kg_rate = kg_nodes / ANNUAL_DAYS
        marginal = (
            proof_rate * thought_count * kg_nodes
            + thought_rate * proof_count * kg_nodes
            + kg_rate * proof_count * thought_count
        ) / max_combos
        return {
            "current_combinations": current_combos,
            "semiotic_richness": round(richness, 4),
            "novelty_fraction": round(novelty, 4),
            "marginal_output_norm": round(min(1.0, marginal * ANNUAL_DAYS), 4),
            "perpetuum_score": round((richness + novelty) / 2, 4),
        }

    def run_cycle(self, seed_signs: List[Sign]) -> SemioticChain:
        """Run one semiotic cycle: each sign generates a new interpretant-sign."""
        self._cycle += 1
        new_signs: List[Sign] = []
        for sign in seed_signs:
            interp_id = hashlib.sha256(f"{sign.id}:{self._cycle}".encode()).hexdigest()[:12]
            new_sign = Sign(
                id=f"I_{interp_id}",
                representamen=f"interpretation_of_{sign.id}",
                object_ref=sign.interpretant,
                interpretant=f"meaning_level_{self._cycle}_{interp_id[:6]}",
            )
            self.add_sign(new_sign)
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

    def run_runtime(
        self,
        seed_signs: List[Sign],
        cycles: int,
        sleep_seconds: float = 0.0,
    ) -> List[SemioticChain]:
        """
        Run multi-cycle runtime with feedback:
        newly generated signs become the input of the next cycle.
        """
        current = seed_signs
        chains: List[SemioticChain] = []
        for _ in range(cycles):
            chain = self.run_cycle(current)
            chains.append(chain)
            current = chain.signs
            if sleep_seconds > 0:
                time.sleep(sleep_seconds)
        return chains


def _parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ORION Semiotic Perpetuum runtime")
    subparsers = parser.add_subparsers(dest="command", required=True)

    start_parser = subparsers.add_parser("start", help="Start semiotic runtime")
    start_parser.add_argument(
        "--seed",
        default="proof,thought,kg-node",
        help="Comma-separated initial signs",
    )
    start_parser.add_argument(
        "--cycles",
        type=int,
        default=5,
        help="Number of runtime cycles",
    )
    start_parser.add_argument(
        "--sleep",
        type=float,
        default=0.0,
        help="Delay in seconds between cycles",
    )

    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parse_args(argv)
    if args.command == "start":
        if args.cycles <= 0:
            raise ValueError("--cycles must be greater than 0")
        if args.sleep < 0:
            raise ValueError("--sleep must be non-negative")

        seeds = [item.strip() for item in args.seed.split(",") if item.strip()]
        if not seeds:
            raise ValueError(
                'At least one seed sign is required. Provide seeds via --seed (e.g. --seed "proof,thought").'
            )

        spm = SemioticPerpetuum()
        seed_signs = spm.create_seed_signs(seeds)
        chains = spm.run_runtime(seed_signs=seed_signs, cycles=args.cycles, sleep_seconds=args.sleep)

        print("ORION Semiotic Perpetuum Runtime")
        print(f"Start signs: {len(seed_signs)}")
        for chain in chains:
            print(
                f"Cycle {chain.cycle_count}: "
                f"{chain.total_interpretants} interpretants, "
                f"growth={chain.growth_factor:.2f}"
            )
        print(f"Total signs stored: {len(spm.signs)}")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())

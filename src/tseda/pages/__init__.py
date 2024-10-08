from . import (
    gnn,  # noqa: F401
    gnnhaplotype,  # noqa: F401
    overview,  # noqa: F401
    sample_sets,  # noqa: F401
    structure,  # noqa: F401
)

PAGES_MAP = {
    "Overview": overview,
    "Sample set editor": sample_sets,
    "Structure overview": structure,
    "Individual GNN plots": gnn,
    "Haplotype GNN plots": gnnhaplotype,
}

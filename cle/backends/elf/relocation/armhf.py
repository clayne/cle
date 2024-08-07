from __future__ import annotations

from .arm import (
    R_ARM_ABS32,
    R_ARM_ABS32_NOI,
    R_ARM_CALL,
    R_ARM_COPY,
    R_ARM_GLOB_DAT,
    R_ARM_GOT_PREL,
    R_ARM_JUMP24,
    R_ARM_JUMP_SLOT,
    R_ARM_MOVT_ABS,
    R_ARM_MOVW_ABS_NC,
    R_ARM_PC24,
    R_ARM_PREL31,
    R_ARM_REL32,
    R_ARM_REL32_NOI,
    R_ARM_RELATIVE,
    R_ARM_THM_CALL,
    R_ARM_THM_JUMP6,
    R_ARM_THM_JUMP19,
    R_ARM_THM_JUMP24,
    R_ARM_THM_MOVT_ABS,
    R_ARM_THM_MOVW_ABS_NC,
    R_ARM_TLS_DTPMOD32,
    R_ARM_TLS_DTPOFF32,
    R_ARM_TLS_TPOFF32,
)

arch = "ARMHF"

__all__ = [
    "arch",
    "R_ARM_CALL",
    "R_ARM_PREL31",
    "R_ARM_REL32",
    "R_ARM_ABS32",
    "R_ARM_MOVW_ABS_NC",
    "R_ARM_MOVT_ABS",
    "R_ARM_THM_CALL",
    "R_ARM_COPY",
    "R_ARM_GLOB_DAT",
    "R_ARM_GOT_PREL",
    "R_ARM_JUMP_SLOT",
    "R_ARM_RELATIVE",
    "R_ARM_ABS32_NOI",
    "R_ARM_REL32_NOI",
    "R_ARM_TLS_DTPMOD32",
    "R_ARM_TLS_DTPOFF32",
    "R_ARM_TLS_TPOFF32",
    "R_ARM_JUMP24",
    "R_ARM_PC24",
    "R_ARM_THM_JUMP24",
    "R_ARM_THM_JUMP19",
    "R_ARM_THM_JUMP6",
    "R_ARM_THM_MOVW_ABS_NC",
    "R_ARM_THM_MOVT_ABS",
]

# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Oxgantarawang/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Oxgantarawang/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A compact chess engine in a single 4 KB `main.py` (Python 3 stdlib only) for the make.fun tiny-chess-01 bounty.

## Engine

0x88 board, negamax with alpha-beta and capture quiescence (check evasions included), MVV-LVA ordering, null-move pruning, iterative deepening to a fixed 125,000-node budget per move (deterministic — no clock, no randomness). Evaluation is material + piece-square tables + a king pawn-shield bonus. Full move generation: castling, promotion, check/mate/stalemate detection. En passant is not generated (a known, deliberate trade-off for size).

## Testing

Validated with perft (start position 20/400/8902, Kiwipete 48) and played against the real house engines in the kit's practice trials: trial-0 Elo 1279 (1W/4D/1L), trial-1 Elo 1099 (1W/2D/3L), trial-2 Elo 997 (1W/1D/4L); mean ~1125, ~3.3 s/move, max ~4.7 s (limit 10 s).

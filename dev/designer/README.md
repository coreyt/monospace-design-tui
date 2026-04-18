# Mono Designer

This directory contains the `0.3.0` design package for the Mono
**designer** system.

The designer is the set of components that support:

- navigation design
- workflow design
- screen design
- YAML canonical artifacts
- ASCII projection
- HITL revision
- Mono-native design-generation agents and skills

## Documents

- [DSL Specification](./dsl-spec.md)
- [YAML Artifacts](./yaml-spec.md)
- [YAML Read/Write](./yaml-read-write.md)
- [DSL to ASCII Projector](./dsl-to-ascii-projector.md)
- [Agent Requirements](./requirements-agent.md)
- [Skill Requirements](./requirements-skill.md)
- [Tool Requirements](./requirements-tools.md)

## 0.3.0 Position

At `0.3.0`:

- YAML is canonical
- ASCII is the primary review output
- the DSL is intentionally minimal
- the DSL exists to normalize semantics and support projection
- the system is Python-first

This package is scoped to `0.3.0`, not the later `0.4-0.8` platform vision.

# Data Flow Diagram

The diagram below shows how the Python CLI orchestrates the Go engine and how data flows through the pipeline.

```mermaid
flowchart TD
  A[User CLI] -->|args: input,key,mode| B[Python CLI]
  B -->|validate| C[Input File]
  B -->|map args| D[Engine args]
  B -->|spawn| E[Go Engine (binary or `go run`)]
  E -->|stdout / files| F[Output Artifact]
  F -->|written by CLI| G[Output File]
  E -->|exit code / stderr| B
  B -->|map errors| H[User-friendly messages]
```

Notes:

- The Python CLI is the control plane: it validates, maps, and coordinates.
- The Go engine is the data plane: performs transforms deterministically.

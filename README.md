<h1 align="center">Hi! I'm Zack 👋</h1>

<h2 align="center">Postdoctoral researcher at NCTS in Taipei, working on compactifications of moduli spaces of complex algebraic surfaces.</h2>

<p align="center">
  <a href="https://dzackgarza.com" title="Website"><img src="./assets/contact-website.svg" width="28" alt="Website" /></a>
  &nbsp;&nbsp;
  <a href="mailto:dzackgarza@gmail.com" title="Email"><img src="./assets/contact-email.svg" width="28" alt="Email" /></a>
  &nbsp;&nbsp;
  <a href="https://twitter.com/dzackgarza" title="Twitter"><img src="./assets/contact-twitter.svg" width="28" alt="Twitter" /></a>
</p>

<br />

## Websites

Open these in a browser. Nothing to install.

| Site | What you find there |
| --- | --- |
| [**Research book**](https://dzackgarza.github.io/research/) <a href="https://github.com/dzackgarza/research" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | My research notes as one book: the category theory and the lattice, form and Witt theory under the work, then the Coble lattice, its moduli spaces and period domains, reflection groups, compactifications, degenerations and stable limits, the computed results, and open problems. |
| [**Lattice database**](https://dzackgarza.github.io/research/lattice-database/) <a href="https://github.com/dzackgarza/research/tree/main/lattice-database" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | A catalogue of lattices — definite, indefinite and degenerate — with one page per lattice and one table to filter, sort and export. Each record stores its computed invariants, its relations to the other records, and the sources that state it. |
| [**Formalization corpus**](https://dzackgarza.github.io/formalization-corpus/) <a href="https://github.com/dzackgarza/formalization-corpus" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | One search across the formal literature: Mathlib, the Fermat's Last Theorem and Carleson's theorem projects, Viazovska's sphere packing, the Polynomial Freiman–Ruzsa conjecture, condensed mathematics — and, in Rocq and Agda, Feit–Thompson and the univalent libraries. Answers "has anyone formalized this, and where". Open JSON API. |
| [**Graduate mathematics in Lean**](https://dzackgarza.github.io/lean-categories/) <a href="https://github.com/dzackgarza/lean-categories" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | The standard graduate texts — Dummit and Foote, Riehl, Atiyah–Macdonald, Weibel, Hartshorne, Matsumura and the rest — read definition by definition and theorem by theorem, with what Lean already has and what is still unformalized. |
| [**Qual Corpus**](https://dzackgarza.github.io/new-qual-site/) <a href="https://github.com/dzackgarza/new-qual-site" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Graduate qualifying-exam problems to browse, filter, sample and print: algebra, algebraic geometry, real and complex analysis, topology, and more, with where each problem appeared and its definitions, hints and related problems. |

Older: [notes on the talks of the UCSD Algebraic Geometry Conference 2019](https://dzackgarza.github.io/UCSD-Algebraic-Geometry-Conference-2019/) · [undergraduate lab reports](https://dzackgarza.github.io/Lab-Reports/).

## Repositories

### SageMath

Sage builds its class hierarchy at runtime, so ordinary Python tooling cannot see it. These three make it visible.

| Repository | What it does for you |
| --- | --- |
| sagemath-mypy-plugin <a href="https://github.com/dzackgarza/sagemath-mypy-plugin" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Makes `@override`, `@final`, abstract-method and signature checks work on Sage category classes, whose MRO exists only at runtime. Without it every `@override` on a provider method is reported as an error. |
| sage-stubs <a href="https://github.com/dzackgarza/sage-stubs" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Type stubs for the Sage 10.7 category and structure surface, so mypy can analyze code importing `sage.categories.*`, `sage.structure.*`, and `sage.misc.*`. Discovered automatically; no `mypy_path` setup. |
| sage-lsp-server <a href="https://github.com/dzackgarza/sage-lsp-server" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Completion, hover, and signature help for `sage.all` names in JupyterLab or any LSP editor, so Sage cells stop looking like undefined identifiers. |

### Lean 4

| Repository | What it does for you |
| --- | --- |
| formalization-corpus <a href="https://github.com/dzackgarza/formalization-corpus" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Checks out and indexes Mathlib, the registered Lean formalization projects, the Reservoir packages and the Rocq and Agda sources as one tree, and builds the search site above from it. |
| lean-jupyter-kernel <a href="https://github.com/dzackgarza/lean-jupyter-kernel" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Runs Lean 4 in a notebook where a cell's output always matches the source visible above it. Editing an early cell re-runs what depends on it instead of leaving stale results from a version that is no longer on screen. |
| lean-categories <a href="https://github.com/dzackgarza/lean-categories" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | The arithmetic theory of quadratic and bilinear lattices in Lean 4, which Mathlib does not cover: Jordan splitting over discrete valuation rings, discriminant forms and gluing, genus and spinor-genus invariants, Hasse and Witt invariants, and the mass of a genus. Nothing is admitted: no `sorry`. |

### Writing and documents

| Repository | What it does for you |
| --- | --- |
| pandoc-preview <a href="https://github.com/dzackgarza/pandoc-preview" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | A local Overleaf substitute for people who already have a real pandoc setup. Markdown, LaTeX, TikZ, BibTeX, Beamer and reveal.js in one editor; every renderer and exporter is a command you configure, not a fixed menu of app features. |
| pandoc-ssg <a href="https://github.com/dzackgarza/pandoc-ssg" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Publishes a Markdown site with real LaTeX math and `tikzcd`/TikZ blocks compiled to inline SVG, using your own pandoc templates, filters and macros rather than a generator's dialect of Markdown. |
| zotero-local-write-api <a href="https://github.com/dzackgarza/zotero-local-write-api" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Zotero's built-in local API is read-only. This add-on adds write endpoints — items, notes, attachments, collections, tags — on the same localhost server, with no API key and no cloud round trip. |

### LLM and agent infrastructure

| Repository | What it does for you |
| --- | --- |
| usage-limits <a href="https://github.com/dzackgarza/usage-limits" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Shows how much quota you have left across every provider at once: Claude Code, Codex, Copilot, Cursor, Antigravity, DeepSeek, Kiro, Ollama Cloud. |
| improved-webtools <a href="https://github.com/dzackgarza/improved-webtools" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Gives an agent web search and page fetching through your own SearxNG instance — no API key, no per-query billing. Works as an OpenCode plugin or as an MCP server for any client. |
| itree <a href="https://github.com/dzackgarza/itree" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Keeps a repository's GitHub sub-issue tree ordered and answers one question — what is the single next work unit — while flagging cycles, orphaned issues, and work hidden outside the tree. |
| agent-memory <a href="https://github.com/dzackgarza/agent-memory" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Lets an agent keep and search notes across sessions, stored as plain Markdown in a git-tracked vault you can read and edit yourself. |
| ai-review-ci <a href="https://github.com/dzackgarza/ai-review-ci" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> | Installs the same commit, push, and CI quality gates into any repository with one command, including hooks and branch protection. Profiles for Python, Bun, Rust, Sage, and docs. |

### Forks that add something

| Repository | What it adds over upstream |
| --- | --- |
| zettlr-pandoc <a href="https://github.com/dzackgarza/zettlr-pandoc" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> · Zettlr <a href="https://www.zettlr.com" title="Zettlr"><img src="https://api.iconify.design/octicon/globe-16.svg?color=%238b949e" width="16" alt="Zettlr" /></a> | Zettlr rendering math with MathJax instead of KaTeX, including mhchem, plus your own TeX macros defined once and honored both in the editor and in every pandoc export. |
| jupyter-mcp-server <a href="https://github.com/dzackgarza/jupyter-mcp-server" title="GitHub"><img src="https://api.iconify.design/octicon/mark-github-16.svg?color=%238b949e" width="16" alt="GitHub" /></a> · Docs <a href="https://jupyter-mcp-server.datalayer.tech" title="Docs"><img src="https://api.iconify.design/octicon/globe-16.svg?color=%238b949e" width="16" alt="Docs" /></a> | Drives Jupyter notebooks over ordinary HTTP with an OpenAPI schema instead of MCP. Notebooks are addressed by an ID derived from their path, so there is no session state to lose across restarts, and GPT Actions can call it directly. |

<br />

<p align="center">
  <a href="https://github.com/dzackgarza">
    <img height="170" src="./assets/github-stats.svg" alt="GitHub statistics" />
    <img height="170" src="./assets/top-languages.svg" alt="Top languages" />
  </a>
</p>

# Design System & Identidade Visual: EnviroAsset Licenciamento

Este documento define as diretrizes de interface (UI), experiência (UX) e identidade de marca (Branding) aplicadas na Landing Page B2G focada em licenciamento municipal.

## 1. Princípios de Design (UI/UX Pro Max)
*   **Soft UI Evolution:** Uso extensivo de sombras suaves, difusas e expansivas no lugar de bordas rígidas, garantindo um aspecto "flutuante" e hiper-premium.
*   **Minimalismo Bimodal:** Fundos ultra-limpos (Slate 50 / White) com foco agressivo em legibilidade e hierarquia tipográfica.
*   **Cinematic Glassmorphism:** Uso de fundos translúcidos (`backdrop-filter: blur`) integrados a orbes de luz para seções de alto impacto narrativo.
*   **Maximalismo de Conversão:** Remoção total de ruídos visuais e distrações secundárias para direcionar o usuário à ação ("Agendar Reunião").

---

## 2. Paleta de Cores (Color System)

A paleta foi desenhada para inspirar confiança institucional (GovTech) e velocidade de software em nuvem.

### Brand Colors (Primárias)
| Cor | Hexadecimal | Variável CSS | Uso Base |
| :--- | :--- | :--- | :--- |
| **Emerald Green** | `#10b981` | `--color-primary` | Botões principais (CTA), Destaques de Sucesso, Badges de Conformidade. |
| **Green Hover** | `#059669` | `--color-primary-hover` | Estado de hover dos CTAs. |
| **Royal Blue** | `#2563eb` | `--color-secondary` | Destaques textuais (Headline), Links de ação secundária. |
| **Blue Hover** | `#1d4ed8` | `--color-secondary-hover` | Estado de hover secundário. |

### Neutros & Superfícies (Slate Scale)
| Tom | Hexadecimal | Variável CSS | Aplicação |
| :--- | :--- | :--- | :--- |
| **Slate 900** | `#0f172a` | `--text-main` | Títulos (`h1`, `h2`, `h3`), Textos enfatizados e Sombra de base. |
| **Slate 500** | `#64748b` | `--text-muted` | Parágrafos de suporte, subtítulos, legendas. |
| **Slate 100** | `#f1f5f9` | `--border-color` | Bordas virtuais invísiveis e divisórias ultrafinas. |
| **Slate 50** | `#f8fafc` | `--bg-main` | Fundo base de seções alternadas (cria contraste suave com os cards brancos). |
| **Pure White** | `#ffffff` | `--bg-alt` | Fundo dos Bento Cards e cabeçalho. |

### Status Semântico (Dashboard Logic)
| Status | Hexadecimal | Fundo Pastel (Ícone) | Variável CSS | Significado |
| :--- | :--- | :--- | :--- | :--- |
| **Aprovado** | `#10B981` | `#D1FAE5` | `--status-aprovado` | Emissão de Licença, Conformidade. |
| **Em Análise** | `#3B82F6` | `#DBEAFE` ou `#F0F9FF` | `--status-em-analise` | Processamento, Infraestrutura. |
| **Aguardando** | `#F59E0B` | `#FEF3C7` ou `#FEFCE8` | `--status-aguardando` | Pendências, Alertas. |
| **Indeferido** | `#EF4444` | `#FEE2E2` ou `#FFF1F2` | `--status-indeferido` | Bloqueios, Gargalos (Ex: Balcão). |

---

## 3. Tipografia

- **Família Font Principal:** `'Inter', system-ui, -apple-system, sans-serif`
- A fonte Inter foi escolhida por sua clareza cirúrgica em interfaces de software denso, provendo alta legibilidade corporativa.

### Escalas e Pesos
- **Headlines (H1, H2):** Trabalhadas em peso `800` (Extra Bold) ou `700` (Bold) com forte compactação de tracking (letter-spacing: `-0.02em` a `-0.04em`) para passar autoridade maciça.
- **Labels Visuais (Badges):** Fonte ultrapequena (`11px` a `12px`), peso `800` (Extra Bold), transformadas em **UPPERCASE** com amplo respiro (letter-spacing: `0.15em`).
- **Body Text (Parágrafos):** Peso `400` (Regular) e `500` (Medium), com altura de linha (line-height) ampla de `1.6` a `1.7` para leitura hiper-confortável em blocos densos de informação.

---

## 4. Componentes Estilizados Base

### Grid e Layout
- O esqueleto base utiliza o padrão **Bento Grid**, focado em assimetria elegante com paddings vastos em contêineres e um grid puramente matemático (12 colunas fracionais, flex box para colapsos via `grid-3` ou `grid-2`).

### Bento Cards Premium (Soft UI)
- **Superfície:** Branco Puro.
- **Borda:** Quase imperceptível (`1px solid rgba(241, 245, 249, 1)`).
- **Arredondamento:** Alto (`border-radius: 20px` a `32px` dependiendo do viewport).
- **Sombra Padrão:** Difusa descendente (`0 4px 20px -2px rgba(0,0,0,0.03)`).
- **Interação (Hover Lift):** O card levanta (`transform: translateY(-8px) scale(1.02)`) enquanto a sombra é esmagada e espalhada para criar peso físico tridimensional.

### Glassmorphic Cards (Cinematic Approach)
- **Fundo translúcido:** `rgba(255, 255, 255, 0.6)`.
- **Motor ótico:** `backdrop-filter: blur(24px)`.
- **Reflexos físicos:** Bordas internas brancas (`inset 0 1px 0 rgba(255, 255, 255, 1)`) para simular o bisotê brilhante do vidro ao redor de todo o componente.

### Títulos Gradientes Texturizados (Cinemáticos)
- Textos primários podem incorporar gradiente com recorte via `-webkit-background-clip: text` e a frente da cor nativa como transparente (`-webkit-text-fill-color: transparent`).

## 5. Animações & Interações Globais
- **Scroll Reveal (Intersection Observer):** Nenhuma informação essencial entra na tela estática. Elementos-chave (títulos, texto, imagens) deslizam do fundo (`translateY(40px)`) para o centro recuperando visibilidade de `0%` para `100%`, guiando de forma tátil o fluxo de leitura do usuário via scrolling.
- **Staggering Transitions:** Uma "cascata orgânica". Quando um bloco tem múltiplos componentes internos (ex: 3 features cards), eles são revelados não de uma vez, mas em atrasos pontuais `0.1s`, `0.2s`, `0.3s`, criando ritmo.
- **Física de Curvas:** Easing modelado sempre em `cubic-bezier(0.16, 1, 0.3, 1)` ou similares, fugindo do amortecimento linear padrão do navegador e replicando engajamento inercial premium (estilo Apple Human Interface Guidelines).

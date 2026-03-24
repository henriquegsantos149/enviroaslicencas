# 🌿 Manual de Identidade Visual - Enviroasset

> **Gestão descomplicada de riscos ambientais**

---

## 📑 Índice

1. [Paleta de Cores](#-paleta-de-cores)
2. [Tipografia](#-tipografia)
3. [Logotipo](#-logotipo)
4. [Elementos Visuais](#-elementos-visuais)
5. [Layout e Estrutura](#-layout-e-estrutura)
6. [Componentes de Interface](#-componentes-de-interface)
7. [Aplicações Práticas](#-aplicações-práticas)
8. [CSS Variables (Código Pronto)](#-css-variables-código-pronto)

---

## 🎨 Paleta de Cores

### Cores Primárias

| Cor | HEX | RGB | Uso | Proporção |
|-----|-----|-----|-----|-----------|
| 🟩 **Verde Escuro** | `#1A5632` | `26, 86, 50` | Títulos, headings, CTA primário | 70% |
| 🟢 **Verde Médio** | `#2D9259` | `45, 146, 89` | Destaques, ícones, hover states | 20% |
| 🔵 **Azul Claro** | `#D5E8F0` | `213, 232, 240` | Backgrounds, cards, seções alternadas | 10% |

### Cores Neutras

| Cor | HEX | RGB | Uso | Contexto |
|-----|-----|-----|-----|----------|
| ⬜ **Branco** | `#FFFFFF` | `255, 255, 255` | Fundo principal, cards | Base do layout |
| ◻️ **Cinza Claro** | `#F5F5F5` | `245, 245, 245` | Seções alternadas, hover | Contraste sutil |
| ◾ **Cinza Médio** | `#666666` | `102, 102, 102` | Descrições, subtítulos | Hierarquia visual |
| ⬛ **Cinza Escuro** | `#333333` | `51, 51, 51` | Corpo de texto, parágrafos | Legibilidade máxima |
| 🔲 **Borda** | `#E5E5E5` | `229, 229, 229` | Bordas, separadores | Delimitação sutil |

---

## 🔤 Tipografia

### Família Tipográfica

**Principal:** `Inter` ou `Roboto` (Google Fonts)  
**Fallback:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif`

### Hierarquia Tipográfica

| Elemento | Família | Tamanho | Peso | Uso |
|----------|---------|---------|------|-----|
| **H1 - Hero** | Inter/Roboto | `48-64px` | `700 (Bold)` | Título principal da página |
| **H2 - Seção** | Inter/Roboto | `32-40px` | `700 (Bold)` | Títulos de seção |
| **H3 - Subseção** | Inter/Roboto | `24-28px` | `600 (Semi-bold)` | Cards, destaques |
| **Body** | Inter/Roboto | `16-18px` | `400 (Regular)` | Parágrafos, conteúdo |
| **Small** | Inter/Roboto | `14px` | `400 (Regular)` | Notas, legendas |

### Import Fonts

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
/* ou */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
```

---

## 🏷️ Logotipo

### Características

- **Formato:** SVG (vetorial escalável)
- **URL:** `https://enviroasset.com.br/wp-content/uploads/2021/11/EnviroAsset_logo-1.svg`
- **Tipografia:** Sans-serif moderna em verde escuro `#1A5632`
- **Elemento gráfico:** Ícone ambiental integrado ao texto
- **Cores:** Verde escuro predominante com acentos em verde médio

### Uso e Posicionamento

| Contexto | Alinhamento | Tamanho | Espaçamento Mínimo | Backgrounds Permitidos |
|----------|-------------|---------|-------------------|------------------------|
| Header | Esquerda | `40-50px` altura | `20px` todos os lados | Branco, Cinza Claro |
| Footer | Centro/Esquerda | Flexível (maior) | `20px` todos os lados | Verde Escuro, Branco |

---

## 🎭 Elementos Visuais

### Ícones

- **Estilo:** Line icons minimalistas (SVG)
- **Espessura:** `2px`
- **Cores:** `#1A5632` ou `#2D9259`
- **Tamanhos padrão:** `24px`, `32px`, `48px`

### Ilustrações

- **Estilo:** Flat design com elementos geométricos
- **Paleta:** Tons de verde (`#1A5632`, `#2D9259`) com acentos azuis (`#D5E8F0`)
- **Temática:** Ambiental, dados, tecnologia, sustentabilidade
- **Exemplos no site:**
  - `enviroasset_hero-graphic-1.svg`
  - `data-graphic_2.svg`
  - `cta-graphic.svg`

### Imagens

- **Formato:** WebP (fallback: JPG)
- **Tratamento:** Overlay verde suave (`20% opacity`) quando necessário
- **Temática:** Ambientes corporativos, natureza, tecnologia ambiental
- **Aspect Ratios:**
  - Hero sections: `16:9`
  - Cards: `4:3`

---

## 📐 Layout e Estrutura

### Grid System

```
Container máximo: 1200px
Colunas: 
  - Desktop: 12 colunas
  - Tablet: 4 colunas
  - Mobile: 1 coluna
Gutter: 24px
Padding lateral:
  - Mobile: 20px
  - Tablet: 40px
  - Desktop: 60px
```

### Espaçamentos (Spacing Scale)

| Token | Valor | Uso |
|-------|-------|-----|
| `xs` | `8px` | Ícones, badges, espaços mínimos |
| `sm` | `16px` | Dentro de componentes |
| `md` | `24px` | Entre elementos relacionados |
| `lg` | `40px` | Entre cards, itens de lista |
| `xl` | `60px` | Entre seções menores |
| `xxl` | `80px` | Entre grandes blocos de conteúdo |
| `3xl` | `120px` | Separações principais |

### Breakpoints

```scss
// Mobile First
$mobile: 0;
$tablet: 768px;
$desktop: 1024px;
$large-desktop: 1440px;

// Media Queries
@media (min-width: 768px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1440px) { /* Large Desktop */ }
```

---

## 🧩 Componentes de Interface

### Botões

#### Botão Primário

```css
.btn-primary {
  background-color: #2D9259;
  color: #FFFFFF;
  font-size: 16px;
  font-weight: 600;
  padding: 14px 32px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: #1A5632;
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}
```

#### Botão Secundário

```css
.btn-secondary {
  background-color: transparent;
  color: #2D9259;
  font-size: 16px;
  font-weight: 600;
  padding: 12px 30px;
  border: 2px solid #2D9259;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background-color: #2D9259;
  color: #FFFFFF;
}
```

### Cards

```css
.card {
  background-color: #FFFFFF;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}
```

### Navegação

#### Header

```css
header {
  background-color: #FFFFFF;
  height: 80px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  position: sticky;
  top: 0;
  z-index: 100;
}
```

#### Links de Navegação

```css
nav a {
  color: #333333;
  font-size: 16px;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.2s ease;
  position: relative;
  margin: 0 16px;
}

nav a:hover {
  color: #2D9259;
}

nav a:hover::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #2D9259;
}

nav a.active {
  color: #1A5632;
}
```

---

## 🎯 Aplicações Práticas

### Hero Section

```html
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <h1>Gestão descomplicada de riscos ambientais</h1>
      <p>Com quase 20 anos de experiência em projetos ambientais complexos...</p>
      <a href="#sobre" class="btn-primary">Conheça nossos serviços</a>
    </div>
    <div class="hero-image">
      <img src="enviroasset_hero-graphic-1.svg" alt="Ilustração">
    </div>
  </div>
</section>
```

**Especificações:**
- Background: Gradient `linear-gradient(135deg, #F5F5F5 0%, #FFFFFF 100%)` ou imagem com overlay
- Altura: `600-800px` (desktop), `400-500px` (mobile)
- Título: H1 em `#1A5632`, `48-64px`
- Subtítulo: `18-24px` em `#666666`
- Layout: Conteúdo à esquerda, ilustração à direita (desktop) / stack vertical (mobile)

### Seções de Conteúdo

```html
<section class="section">
  <div class="container">
    <h2>Medir. Entender. Agir.</h2>
    <div class="grid">
      <div class="card">
        <h3>Integração</h3>
        <p>Digitalização e sistematização dos dados ambientais</p>
      </div>
      <!-- Mais cards -->
    </div>
  </div>
</section>

<section class="section section-alt">
  <!-- Seção com background alternado -->
</section>
```

**Especificações:**
- Alternância de backgrounds: `#FFFFFF` e `#F5F5F5`
- Padding vertical: `80px` (desktop), `60px` (mobile)
- Grid: 2-3 colunas (desktop), 1 coluna (mobile)
- Gap entre cards: `40px`

### Footer

```html
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-column">
        <img src="logo.svg" alt="Enviroasset">
        <p>Soluções inteligentes para desafios complexos</p>
      </div>
      <div class="footer-column">
        <h4>Institucional</h4>
        <ul>
          <li><a href="#vantagens">Vantagens</a></li>
          <li><a href="#como-funciona">Como funciona</a></li>
        </ul>
      </div>
      <!-- Mais colunas -->
    </div>
  </div>
</footer>
```

**Especificações:**
- Background: `#1A5632`
- Texto: `#FFFFFF`
- Padding: `60px` vertical
- Layout: 4 colunas (desktop), 1 coluna (mobile)
- Links hover: `#D5E8F0`
- Ícones sociais: SVG em `#FFFFFF`, hover `scale(1.1)`

---

## 💻 CSS Variables (Código Pronto)

### Copie e cole no seu projeto:

```css
:root {
  /* ========== CORES ========== */
  
  /* Cores Primárias */
  --color-primary-dark: #1A5632;
  --color-primary-medium: #2D9259;
  --color-accent-light: #D5E8F0;
  
  /* Cores Neutras */
  --color-white: #FFFFFF;
  --color-gray-light: #F5F5F5;
  --color-gray-medium: #666666;
  --color-gray-dark: #333333;
  --color-border: #E5E5E5;
  --color-black: #000000;
  
  /* ========== TIPOGRAFIA ========== */
  
  /* Font Family */
  --font-family-primary: 'Inter', 'Roboto', -apple-system, BlinkMacSystemFont, 
                         'Segoe UI', Arial, sans-serif;
  
  /* Font Sizes */
  --font-size-h1: clamp(40px, 5vw, 64px);
  --font-size-h2: clamp(32px, 4vw, 40px);
  --font-size-h3: clamp(24px, 3vw, 28px);
  --font-size-body: 16px;
  --font-size-body-large: 18px;
  --font-size-small: 14px;
  
  /* Font Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-normal: 1.6;
  --line-height-relaxed: 1.8;
  
  /* ========== ESPAÇAMENTOS ========== */
  
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 40px;
  --spacing-xl: 60px;
  --spacing-xxl: 80px;
  --spacing-3xl: 120px;
  
  /* ========== LAYOUT ========== */
  
  --container-max-width: 1200px;
  --gutter: 24px;
  --header-height: 80px;
  
  /* Border Radius */
  --border-radius-sm: 6px;
  --border-radius-md: 12px;
  --border-radius-lg: 16px;
  --border-radius-full: 9999px;
  
  /* ========== SOMBRAS ========== */
  
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.12);
  --shadow-xl: 0 12px 32px rgba(0, 0, 0, 0.15);
  
  /* ========== TRANSIÇÕES ========== */
  
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.5s ease;
  
  /* ========== Z-INDEX ========== */
  
  --z-dropdown: 10;
  --z-sticky: 50;
  --z-fixed: 100;
  --z-modal-backdrop: 500;
  --z-modal: 600;
  --z-popover: 700;
  --z-tooltip: 800;
}

/* ========== RESET E BASE ========== */

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-family-primary);
  font-size: var(--font-size-body);
  line-height: var(--line-height-normal);
  color: var(--color-gray-dark);
  background-color: var(--color-white);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ========== TIPOGRAFIA ========== */

h1, h2, h3, h4, h5, h6 {
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
  color: var(--color-primary-dark);
  margin-bottom: var(--spacing-md);
}

h1 { font-size: var(--font-size-h1); }
h2 { font-size: var(--font-size-h2); }
h3 { font-size: var(--font-size-h3); }

p {
  margin-bottom: var(--spacing-sm);
}

a {
  color: inherit;
  text-decoration: none;
}

/* ========== CONTAINER ========== */

.container {
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 var(--spacing-md);
}

@media (min-width: 768px) {
  .container {
    padding: 0 var(--spacing-lg);
  }
}

@media (min-width: 1024px) {
  .container {
    padding: 0 var(--spacing-xl);
  }
}

/* ========== BOTÕES ========== */

.btn {
  display: inline-block;
  padding: 14px 32px;
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-semibold);
  text-align: center;
  text-decoration: none;
  border-radius: var(--border-radius-sm);
  transition: all var(--transition-normal);
  cursor: pointer;
  border: none;
}

.btn-primary {
  background-color: var(--color-primary-medium);
  color: var(--color-white);
}

.btn-primary:hover {
  background-color: var(--color-primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-secondary {
  background-color: transparent;
  color: var(--color-primary-medium);
  border: 2px solid var(--color-primary-medium);
  padding: 12px 30px;
}

.btn-secondary:hover {
  background-color: var(--color-primary-medium);
  color: var(--color-white);
}

/* ========== CARDS ========== */

.card {
  background-color: var(--color-white);
  border-radius: var(--border-radius-md);
  padding: 32px;
  box-shadow: var(--shadow-md);
  transition: all var(--transition-normal);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

/* ========== HEADER ========== */

header {
  background-color: var(--color-white);
  box-shadow: var(--shadow-sm);
  position: sticky;
  top: 0;
  z-index: var(--z-fixed);
  height: var(--header-height);
  display: flex;
  align-items: center;
}

/* ========== NAVEGAÇÃO ========== */

nav a {
  color: var(--color-gray-dark);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-medium);
  text-decoration: none;
  transition: color var(--transition-fast);
  position: relative;
  padding: 4px 0;
}

nav a:hover {
  color: var(--color-primary-medium);
}

nav a:hover::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--color-primary-medium);
}

nav a.active {
  color: var(--color-primary-dark);
}

/* ========== HERO SECTION ========== */

.hero {
  background: linear-gradient(135deg, var(--color-gray-light) 0%, var(--color-white) 100%);
  padding: var(--spacing-xxl) 0;
  min-height: 600px;
  display: flex;
  align-items: center;
}

@media (max-width: 767px) {
  .hero {
    min-height: 400px;
    padding: var(--spacing-xl) 0;
  }
}

/* ========== SEÇÕES ========== */

.section {
  padding: var(--spacing-xxl) 0;
}

.section-alt {
  background-color: var(--color-gray-light);
}

@media (max-width: 767px) {
  .section {
    padding: var(--spacing-xl) 0;
  }
}

/* ========== GRID ========== */

.grid {
  display: grid;
  gap: var(--spacing-lg);
}

@media (min-width: 768px) {
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
  .grid-4 { grid-template-columns: repeat(4, 1fr); }
}

/* ========== FOOTER ========== */

footer {
  background-color: var(--color-primary-dark);
  color: var(--color-white);
  padding: var(--spacing-xl) 0;
}

footer a {
  color: var(--color-white);
  text-decoration: none;
  transition: color var(--transition-fast);
}

footer a:hover {
  color: var(--color-accent-light);
}

footer h4 {
  color: var(--color-white);
  font-size: 18px;
  margin-bottom: var(--spacing-sm);
}

/* ========== UTILIDADES ========== */

.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: var(--spacing-xs); }
.mt-2 { margin-top: var(--spacing-sm); }
.mt-3 { margin-top: var(--spacing-md); }
.mt-4 { margin-top: var(--spacing-lg); }
.mt-5 { margin-top: var(--spacing-xl); }

.mb-0 { margin-bottom: 0; }
.mb-1 { margin-bottom: var(--spacing-xs); }
.mb-2 { margin-bottom: var(--spacing-sm); }
.mb-3 { margin-bottom: var(--spacing-md); }
.mb-4 { margin-bottom: var(--spacing-lg); }
.mb-5 { margin-bottom: var(--spacing-xl); }

/* ========== RESPONSIVIDADE ========== */

@media (max-width: 767px) {
  :root {
    --spacing-xxl: 60px;
    --spacing-xl: 40px;
    --header-height: 60px;
  }
}
```

---

## 📱 Componentes React (Bonus)

### Botão

```jsx
// Button.jsx
export const Button = ({ 
  children, 
  variant = 'primary', 
  onClick, 
  className = '',
  ...props 
}) => {
  const baseClass = 'btn';
  const variantClass = variant === 'secondary' ? 'btn-secondary' : 'btn-primary';
  
  return (
    <button 
      className={`${baseClass} ${variantClass} ${className}`}
      onClick={onClick}
      {...props}
    >
      {children}
    </button>
  );
};

// Uso:
<Button variant="primary">Conheça nossos serviços</Button>
<Button variant="secondary">Saiba mais</Button>
```

### Card

```jsx
// Card.jsx
export const Card = ({ children, className = '', hover = true }) => {
  return (
    <div className={`card ${hover ? 'card-hover' : ''} ${className}`}>
      {children}
    </div>
  );
};

// Uso:
<Card>
  <h3>Integração</h3>
  <p>Digitalização e sistematização dos dados ambientais</p>
</Card>
```

---

## 🎯 Checklist de Implementação

- [ ] Importar Google Fonts (Inter ou Roboto)
- [ ] Copiar CSS Variables para o projeto
- [ ] Configurar cores do tema
- [ ] Implementar sistema de espaçamento
- [ ] Criar componentes base (Button, Card, etc.)
- [ ] Configurar breakpoints responsivos
- [ ] Adicionar sombras e transições
- [ ] Implementar header sticky
- [ ] Criar footer com layout em grid
- [ ] Testar em diferentes dispositivos

---

## 📞 Contato

**Enviroasset - NewFields Brasil**

- 📧 comercial@newfields.com.br
- 📱 +55 51 99154-4051
- 🌐 https://enviroasset.com.br

---

## 📄 Licença

Este manual de identidade visual é propriedade da Enviroasset/NewFields Brasil.  
Uso restrito para desenvolvimento de páginas e materiais oficiais da marca.

---

**Última atualização:** Março 2026  
**Versão:** 1.0

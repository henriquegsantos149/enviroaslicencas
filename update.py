import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the Grid Container start with Carousel container start
target_container_start = """        <!-- Problem Cards Horizontal Track -->
        <div class="problema-scroll-track">"""
        
replacement_container_start = """        <!-- Feature Carousel Layout -->
        <div class="feature-carousel-container reveal-on-scroll">
            <div class="fc-sidebar">
                <div class="fc-fade fc-fade-top"></div>
                <div class="fc-fade fc-fade-bottom"></div>
                <div class="fc-chips-wrapper">
                    <button class="fc-chip active" data-index="0">
                        <div class="fc-chip-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-6l-2 3h-4l-2-3H2" /><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z" /></svg>
                        </div>
                        <span>Caos no Balcão</span>
                    </button>
                    <button class="fc-chip" data-index="1">
                        <div class="fc-chip-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10" /><path d="M12 2a10 10 0 0 1 10 10" /></svg>
                        </div>
                        <span>Análises Travadas</span>
                    </button>
                    <button class="fc-chip" data-index="2">
                        <div class="fc-chip-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9.88 9.88a3 3 0 1 0 4.24 4.24" /><path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68" /><path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61" /><line x1="2" y1="2" x2="22" y2="22" /></svg>
                        </div>
                        <span>Controle Cego</span>
                    </button>
                    <button class="fc-chip" data-index="3">
                        <div class="fc-chip-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 0 1 10 10" /><path d="M12 22a10 10 0 0 1-10-10" /><path d="M12 6v6l4 2" /></svg>
                        </div>
                        <span>Arrecadação Lenta</span>
                    </button>
                </div>
            </div>
            <div class="fc-content">"""

content = content.replace(target_container_start, replacement_container_start)
content = content.replace('class="prob-card prob-card-light reveal-on-scroll"', 'class="prob-card prob-card-light fc-card-wrap" data-index="0"', 1)
content = content.replace('class="prob-card prob-card-blue reveal-on-scroll"', 'class="prob-card prob-card-blue fc-card-wrap" data-index="1"', 1)
content = content.replace('class="prob-card prob-card-light reveal-on-scroll"', 'class="prob-card prob-card-light fc-card-wrap" data-index="2"', 1)
content = content.replace('class="prob-card prob-card-blue reveal-on-scroll"', 'class="prob-card prob-card-blue fc-card-wrap" data-index="3"', 1)

target_end = """            </div><!-- /.problema-scroll-track -->"""
replacement_end = """            </div>
        </div>"""
content = content.replace(target_end, replacement_end)

css_target = """            /* ===== PROBLEM SECTION HORIZONTAL SCROLL ===== */
            .problema-scroll-track {
                display: flex;
                gap: 32px;
                overflow-x: auto;
                scroll-snap-type: x mandatory;
                padding-left: clamp(24px, 5vw, calc(50vw - 550px));
                padding-right: clamp(24px, 5vw, calc(50vw - 550px));
                scroll-padding-left: clamp(24px, 5vw, calc(50vw - 550px));
                padding-top: 20px;
                padding-bottom: 80px;
                scrollbar-width: none;
                -ms-overflow-style: none;
                position: relative;
                z-index: 2;
            }

            .problema-scroll-track::-webkit-scrollbar {
                display: none;
            }"""

css_replacement = """            /* ===== FEATURE CAROUSEL (SHADCN INSPIRED) ===== */
            .feature-carousel-container {
                display: flex;
                flex-direction: column;
                min-height: 600px;
                border-radius: 40px;
                border: 1px solid rgba(15,23,42,0.1);
                overflow: hidden;
                background: #fff;
                box-shadow: 0 20px 50px -12px rgba(15, 23, 42, 0.05);
                margin-top: 20px;
                position: relative;
                z-index: 2;
            }
            @media (min-width: 1024px) {
                .feature-carousel-container {
                    flex-direction: row;
                    border-radius: 64px;
                    min-height: 600px;
                }
            }

            .fc-sidebar {
                width: 100%;
                min-height: 350px;
                background: #2563EB;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: flex-start;
                padding: 32px;
                overflow: hidden;
            }
            @media (min-width: 1024px) {
                .fc-sidebar {
                    width: 40%;
                    min-height: 100%;
                    padding-left: 64px;
                }
            }

            .fc-fade {
                position: absolute;
                left: 0; right: 0;
                height: 64px;
                z-index: 10;
                pointer-events: none;
            }
            .fc-fade-top { 
                top: 0; 
                background: linear-gradient(to bottom, #2563EB, transparent);
            }
            .fc-fade-bottom {
                bottom: 0;
                background: linear-gradient(to top, #2563EB, transparent);
            }

            .fc-chips-wrapper {
                position: relative;
                z-index: 5;
                display: flex;
                flex-direction: column;
                gap: 16px;
                width: 100%;
            }

            .fc-chip {
                display: flex;
                align-items: center;
                gap: 16px;
                padding: 16px 24px;
                border-radius: 9999px;
                border: 1px solid rgba(255,255,255,0.2);
                background: transparent;
                color: rgba(255,255,255,0.7);
                font-size: 14px;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                cursor: pointer;
                transition: all 0.5s ease;
                text-align: left;
                outline: none;
                width: fit-content;
            }
            @media (min-width: 1024px) {
                .fc-chip {
                    font-size: 15px;
                    padding: 16px 32px;
                }
            }
            .fc-chip:hover {
                border-color: rgba(255,255,255,0.4);
                color: #fff;
            }
            .fc-chip.active {
                background: #fff;
                color: #2563EB;
                border-color: #fff;
                transform: scale(1.02);
                box-shadow: 0 10px 30px -10px rgba(0,0,0,0.2);
                z-index: 10;
            }

            .fc-chip-icon {
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .fc-content {
                flex: 1;
                min-height: 500px;
                background: #F8FAFC;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 32px;
                overflow: hidden;
            }
            @media (min-width: 1024px) {
                .fc-content {
                    padding: 64px;
                    border-left: 1px solid rgba(15,23,42,0.1);
                }
            }

            .fc-card-wrap {
                position: absolute;
                width: 100%;
                transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
                opacity: 0;
                pointer-events: none;
                transform-origin: center;
                margin: 0 !important;
                max-width: 90%;
            }
            @media (min-width: 1024px) {
                .fc-card-wrap {
                    max-width: 440px;
                }
            }

            .fc-card-wrap.active {
                opacity: 1;
                transform: scale(1) translateX(0) rotate(0);
                z-index: 20;
                pointer-events: auto;
            }
            /* Shadcn spring logic emulation */
            .fc-card-wrap.prev {
                opacity: 0.4;
                transform: scale(0.85) translateX(-80px) rotate(-3deg);
                z-index: 10;
            }
            .fc-card-wrap.next {
                opacity: 0.4;
                transform: scale(0.85) translateX(80px) rotate(3deg);
                z-index: 10;
            }
            .fc-card-wrap.hidden-card {
                opacity: 0;
                transform: scale(0.7) translateX(0);
                z-index: 0;
            }"""

content = content.replace(css_target, css_replacement)

prob_card_target = """            /* Base card */
            .prob-card {
                flex: 0 0 auto;
                width: 440px;
                max-width: 82vw;
                scroll-snap-align: start;
                border-radius: 36px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                overflow: hidden;
                transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1);
                /* Scroll-reveal: starts invisible, slides up */
                opacity: 0;
                transform: translateY(48px);
            }"""

prob_card_replacement = """            /* Base card adapted for Carousel */
            .prob-card {
                border-radius: 36px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                overflow: hidden;
                transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1);
                border: 4px solid #fff;
            }
            .fc-card-wrap.prob-card:hover {
                transform: none !important;
            }"""

content = content.replace(prob_card_target, prob_card_replacement)

script_target = """        </style>
    </section>"""
script_replacement = """        </style>
        <script>
            document.addEventListener("DOMContentLoaded", () => {
                const carouselArea = document.querySelector('.feature-carousel-container');
                if(!carouselArea) return;

                const chips = carouselArea.querySelectorAll('.fc-chip');
                const cards = carouselArea.querySelectorAll('.fc-card-wrap');
                const len = cards.length;
                let currentIndex = 0;
                let isPaused = false;
                let interval;

                function updateCarousel(newIndex) {
                    currentIndex = newIndex;
                    
                    // Update Chips
                    chips.forEach((chip, idx) => {
                        if(idx === currentIndex) {
                            chip.classList.add('active');
                        } else {
                            chip.classList.remove('active');
                        }
                    });

                    // Update Cards
                    cards.forEach((card, idx) => {
                        card.classList.remove('active', 'prev', 'next', 'hidden-card');
                        let diff = idx - currentIndex;
                        
                        let normalizedDiff = diff;
                        if (diff > len / 2) normalizedDiff -= len;
                        if (diff < -len / 2) normalizedDiff += len;

                        if (normalizedDiff === 0) {
                            card.classList.add('active');
                        } else if (normalizedDiff === -1 || (diff === len - 1 && len > 2)) {
                            card.classList.add('prev');
                        } else if (normalizedDiff === 1 || (diff === -(len - 1) && len > 2)) {
                            card.classList.add('next');
                        } else {
                            card.classList.add('hidden-card');
                        }
                    });
                }

                // Interaction Mapping
                chips.forEach((chip, idx) => {
                    chip.addEventListener('click', () => {
                        updateCarousel(idx);
                    });
                    chip.addEventListener('mouseenter', () => isPaused = true);
                    chip.addEventListener('mouseleave', () => isPaused = false);
                });

                cards.forEach(card => {
                    card.addEventListener('mouseenter', () => isPaused = true);
                    card.addEventListener('mouseleave', () => isPaused = false);
                });

                // Auto Play Interval
                interval = setInterval(() => {
                    if(!isPaused) {
                        let nextIdx = (currentIndex + 1) % len;
                        updateCarousel(nextIdx);
                    }
                }, 4000); 
                
                updateCarousel(0);
            });
        </script>
    </section>"""
content = content.replace(script_target, script_replacement)

resp_target = """            /* ===== RESPONSIVE ===== */
            @media (max-width: 860px) {
                .problema-scroll-track {
                    gap: 16px;
                    padding-left: 20px;
                    padding-right: 20px;
                    scroll-padding-left: 20px;
                    padding-bottom: 60px;
                }

                .prob-card {
                    width: 320px;
                }"""
resp_replacement = """            /* ===== RESPONSIVE ===== */
            @media (max-width: 860px) {"""
content = content.replace(resp_target, resp_replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Carousel Migration Complete!")

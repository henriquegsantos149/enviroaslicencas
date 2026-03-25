import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target1 = """            /* ===== FEATURE CAROUSEL (SHADCN INSPIRED) ===== */
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
            }"""

replacement1 = """            /* ===== FEATURE CAROUSEL (SHADCN INSPIRED) ===== */
            .feature-carousel-container {
                display: flex;
                flex-direction: column;
                min-height: unset;
                border-radius: 40px;
                border: 1px solid rgba(15,23,42,0.1);
                overflow: hidden;
                background: #fff;
                box-shadow: 0 20px 50px -12px rgba(15, 23, 42, 0.05);
                margin: 20px auto 0;
                max-width: 1100px;
                position: relative;
                z-index: 2;
            }
            @media (min-width: 1024px) {
                .feature-carousel-container {
                    flex-direction: row;
                    border-radius: 48px;
                    min-height: 520px;
                }
            }

            .fc-sidebar {
                width: 100%;
                background: #2563EB;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 40px 24px;
                overflow: hidden;
            }
            @media (min-width: 1024px) {
                .fc-sidebar {
                    width: 36%;
                    min-height: 100%;
                    padding: 48px;
                    justify-content: flex-end;
                }
            }"""

target2 = """            .fc-chips-wrapper {
                position: relative;
                z-index: 5;
                display: flex;
                flex-direction: column;
                gap: 16px;
                width: 100%;
            }"""

replacement2 = """            .fc-chips-wrapper {
                position: relative;
                z-index: 5;
                display: flex;
                flex-direction: column;
                gap: 16px;
                width: fit-content;
                max-width: 100%;
            }"""

target3 = """            .fc-content {
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
            }"""

replacement3 = """            .fc-content {
                flex: 1;
                min-height: 480px;
                background: #F8FAFC;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 40px 20px;
                overflow: hidden;
            }
            @media (min-width: 1024px) {
                .fc-content {
                    padding: 48px;
                    border-left: 1px solid rgba(15,23,42,0.1);
                    min-height: auto;
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
                max-width: 88%;
            }
            @media (min-width: 1024px) {
                .fc-card-wrap {
                    max-width: 520px;
                }
            }"""

content = content.replace(target1, replacement1)
content = content.replace(target2, replacement2)
content = content.replace(target3, replacement3)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Optimization Script Run Successfully!")

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Мир легкой атлетики</title>
    <link rel="stylesheet" type="text/css" href="/static/content/style.css" />
    <link rel="stylesheet" href="/static/content/skrypnikova/css/skrypnikova.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
</head>

<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="/"><h1>Мир легкой атлетики</h1></a>
                </div>
                <nav class="nav">
                    <ul>
                        <li><a href="/" class="{{'active' if title == 'Главная' else ''}}">Главная</a></li>
                        
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle">
                                Дисциплины <span class="arrow">▼</span>
                            </a>
                            <ul class="dropdown-menu" id="discipline-menu">
                                <li><a href="/race-walking">Спортивная ходьба</a></li>
                                <li><a href="/high-jump">Прыжки в высоту</a></li>
                                <li><a href="/run">Бег</a></li>
                                <li><a href="/jump">Прыжки в длину</a></li>
                                <li><a href="/relay">Эстафеты</a></li>
                                <li><a href="/pole-vault">Прыжки с шестом</a></li>
                                <li><a href="/shot-put">Толкание ядра</a></li>
                            </ul>
                        </li>

                        <li><a href="/new-competitions" {{'class=active' if title=='Актуальные старты' else ''}}>Соревнования</a></li>
                        <li><a href="/reviews" {{'class=active' if title=='Отзывы' else ''}}>Отзывы</a></li>
                        <li><a href="/partners" {{'class=active' if title=='Партнеры' else ''}}>Партнеры</a></li>
                        <li><a href="/about" {{'class=active' if title=='О нас' else ''}}>О нас</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <main class="container body-content">
        {{!base}}
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; {{ year or 2026 }} - Мир легкой атлетики</p>
            <div class="footer-links">
                <a href="https://worldathletics.org" target="_blank">World Athletics</a> |
                <a href="http://rusathletics.info" target="_blank">RusAthletics</a> |
                <a href="https://olympics.com" target="_blank">Olympics.com</a>
            </div>
        </div>
    </footer>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const dropdown = document.querySelector('.dropdown');
        const menu = document.getElementById('discipline-menu');

        if (dropdown && menu) {
            dropdown.addEventListener('mouseenter', () => menu.style.setProperty('display', 'block', 'important'));
            dropdown.addEventListener('mouseleave', () => menu.style.setProperty('display', 'none', 'important'));
        }
    });
</script>
</body>
</html>
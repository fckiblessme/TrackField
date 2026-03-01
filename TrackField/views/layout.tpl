<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Мир легкой атлетики</title>
    <link rel="stylesheet" type="text/css" href="/static/content/style.css" />
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
                        <li><a href="/" {{'class=active' if title=='Главная' else ''}}>Главная</a></li>
                        <li><a href="/race-walking" {{'class=active' if title=='Спортивная ходьба' else ''}}>Спортивная ходьба</a></li>
                        <li><a href="/high-jump" {{'class=active' if title=='Прыжки в высоту' else ''}}>Прыжки в высоту</a></li>
                        <li><a href="/run" {{'class=active' if title=='Бег' else ''}}>Бег</a></li>
                        <li><a href="/jump" {{'class=active' if title=='Прыжки в длину' else ''}}>Прыжки в длину</a></li>
                        <li><a href="/pole-vault" {{'class=active' if title=='Прыжки с шестом' else ''}}>Прыжки с шестом</a></li>
                        <li><a href="/shot-put" {{'class=active' if title=='Толкание ядра' else ''}}>Толкание ядра</a></li>
                        <li><a href="/about" {{'class=active' if title=='О нас' else ''}}>О нас</a></li>
                        <li><a href="/contact" {{'class=active' if title=='Контакты' else ''}}>Контакты</a></li>
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
</body>
</html>
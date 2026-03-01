% rebase('layout.tpl', title='Разработчики', year=year)

<div class="discipline-hero">
    <h1>Разработчики</h1>
</div>




<div class="section">
    <h2>Над сайтом работали</h2>
    <div class="legends-grid">

       
        <div class="legend-card">
            <div class="legend-image">
                <div class="initials-circle" style="background-color: #00A896;">СД</div>
            </div>
            <div class="legend-info">
                <h3>Скрыпникова Дарья</h3>
                <p class="legend-country">ФСПО ГУАП</p>
                <p class="legend-desc">Разработка страниц: толкание ядра, прыжки с шестом, страница о разработчиках. Отвечала за наполнение технически сложных дисциплин, собирала информацию о снарядах и правилах соревнований.</p>
                <a href="https://vk.com/d_skry" target="_blank" class="legend-link">Страница ВКонтакте →</a>
            </div>
        </div>

        
        <div class="legend-card">
            <div class="legend-image">
                <div class="initials-circle" style="background-color: #008c7a;">СВ</div>
            </div>
            <div class="legend-info">
                <h3>Стрельцова Виктория</h3>
                <p class="legend-country">ФСПО ГУАП</p>
                <p class="legend-desc">Разработка страниц: прыжки в высоту, спортивная ходьба, главная страница. Работала над структурой главной страницы и навигацией по сайту, собирала исторические справки и информацию о легендах спорта.</p>
                <a href="https://vk.com/fckiblessme" target="_blank" class="legend-link">Страница ВКонтакте →</a>
            </div>
        </div>

   
        <div class="legend-card">
            <div class="legend-image">
                <div class="initials-circle" style="background-color: #006b5c;">ЧП</div>
            </div>
            <div class="legend-info">
                <h3>Чемякина Полина</h3>
                <p class="legend-country">ФСПО ГУАП</p>
                <p class="legend-desc">Разработка страниц: прыжки в длину, бег на короткие дистанции, эстафета. Занималась подбором фотографий, описанием правил беговых дисциплин и таблицами рекордов.</p>
                <a href="https://vk.com/pllood" target="_blank" class="legend-link">Страница ВКонтакте →</a>
            </div>
        </div>
    </div>
</div>

    <div class="section">
        <h2>Оформление сайта</h2>
        <p>При разработке дизайна мы стремились к чистому и современному виду, который не отвлекает от содержания.</p>
        
        <h3>Цветовая палитра:</h3>
        
        <div class="color-palette">

            <div class="color-card">
                <div class="color-sample color-dark"></div>
                <div class="color-info">
                    <h4>#333333</h4>
                    <p>Основной цвет текста — глубокий тёмно-серый, комфортный для чтения</p>
                </div>
            </div>
            

            <div class="color-card">
                <div class="color-sample color-light"></div>
                <div class="color-info">
                    <h4>#E5E5E5</h4>
                    <p>Фоновый цвет страниц и карточек — светлый нейтральный серый</p>
                </div>
            </div>
            
   
            <div class="color-card">
                <div class="color-sample color-accent"></div>
                <div class="color-info">
                    <h4>#00A896</h4>
                    <p>Акцентный цвет — используется для второстепенных кнопок, рамок, иконок</p>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.hero-image-section {
    margin: 30px 0 50px 0;
}


.hero-image-container {
    max-width: 1200px;
    margin: 0 auto;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
.initials-circle {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    font-weight: bold;
    color: white;
    border: 4px solid white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    margin: 0 auto;
}
.hero-image-container img {
    width: 100%;
    height: auto;
    max-height: 500px;
    object-fit: cover;
    border-radius: 12px;
    display: block;
}

.legends-grid {
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin: 30px 0;
}

.legend-card {
    display: flex;
    gap: 30px;
    background: #E5E5E5;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.2s;
}

.legend-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}

.legend-image {
    flex: 0 0 150px;
}

.legend-image img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

.legend-info h3 {
    margin: 0 0 10px 0;
    font-size: 1.6rem;
    color: #00A896;
}

.legend-country {
    font-size: 1.2rem;
    margin: 5px 0;
    color: #333333;
}

.legend-desc {
    font-size: 1.1rem;
    line-height: 1.6;
    margin: 15px 0;
    color: #333333;
}

.legend-link {
    display: inline-block;
    padding: 8px 20px;
    background: #00A896;
    color: white;
    text-decoration: none;
    border-radius: 25px;
    font-weight: 500;
    transition: background 0.2s;
}

.legend-link:hover {
    background: #008c7a;
    text-decoration: none;
}

/* Стили для цветовой палитры */
.color-palette {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin: 25px 0;
}

.color-card {
    display: flex;
    align-items: center;
    gap: 25px;
    background: #E5E5E5;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.color-sample {
    width: 100px;
    height: 100px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    border: 2px solid white;
}

.color-sample.color-dark {
    background-color: #333333;
}

.color-sample.color-light {
    background-color: #E5E5E5;
    border: 2px solid #ccc;
}

.color-sample.color-accent {
    background-color: #00A896;
}

.color-info h4 {
    color: #00A896;
    font-size: 1.4rem;
    margin: 0 0 8px 0;
    font-family: monospace;
    letter-spacing: 1px;
}

.color-info p {
    color: #333333;
    margin: 0;
    font-size: 1.05rem;
    line-height: 1.5;
}

@media (max-width: 768px) {
    .legend-card {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .legend-image {
        flex: 0 0 auto;
    }
    
    .color-card {
        flex-direction: column;
        text-align: center;
    }
    
    .color-sample {
        width: 80px;
        height: 80px;
    }
}
</style>
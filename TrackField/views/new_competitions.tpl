% rebase('layout.tpl', title='Соревнования', year=year)

<div class="discipline-hero">
    <h1>Актуальные соревнования</h1>
</div>

<div class="discipline-content">

    <div class="section">
        <h2>Добавить соревнование</h2>

        <div class="info-block comp-info-block">
            <p class="info-text">Заполните форму, чтобы добавить информацию о предстоящем старте. Соревнование появится в общем списке ниже.</p>
        </div>

        % if error:
            <div class="comp-error">
                <span class="comp-error-icon">⚠️</span>
                <span>{{ error }}</span>
            </div>
        % end

        <form action="/new-competitions" method="post" class="comp-form">
            
            <div class="comp-form-group">
                <label>Автор</label>
                <input type="text" name="author" =>
            </div>

            <div class="comp-form-group">
                <label>Название</label>
                <input type="text" name="comp_name" =>
            </div>

            <div class="comp-form-group">
                <label>Дисциплина</label>
                <select name="discipline">
                    <option value="">Выберите из списка</option>
                    <option value="Спортивная ходьба">Спортивная ходьба</option>
                    <option value="Прыжки в высоту">Прыжки в высоту</option>
                    <option value="Бег">Бег</option>
                    <option value="Прыжки в длину">Прыжки в длину</option>
                    <option value="Эстафеты">Эстафеты</option>
                    <option value="Прыжки с шестом">Прыжки с шестом</option>
                    <option value="Толкание ядра">Толкание ядра</option>
                </select>
            </div>

            <div class="comp-form-group">
                <label>Дата проведения</label>
                <input type="date" name="event_date">
            </div>

            <div class="comp-form-group">
                <label>Описание</label>
                <textarea name="description" rows="3"=></textarea>
            </div>

            <div class="comp-form-group">
                <label>Телефон</label>
                <input type="text" name="phone" placeholder="+7 (ххх) ххх-хх-хх">
            </div>

            <div class="comp-form-submit">
                <button type="submit" class="btn">Добавить соревнование</button>
            </div>

        </form>
    </div>


    <div class="section">
        <h2>Предстоящие старты</h2>

        <div class="comp-feed">

            % for comp in competitions:
            <div class="comp-card">
                <div class="comp-card-badge">{{ comp['discipline'] }}</div>
                <h3 class="comp-card-title">{{ comp['comp_name'] }}</h3>
                <p class="comp-card-desc">{{ comp['description'] }}</p>
                <div class="comp-card-meta">
                    <span>📅 {{ comp['event_date'] }}</span>
                    <span>Автор: {{ comp['author'] }}</span>
                    % if comp['phone']:
                    <span>📞 {{ comp['phone'] }}</span>
                    % end
                </div>
            </div>
            % end

            % if len(competitions) == 0:
            <p class="comp-empty">Пока нет добавленных соревнований...</p>
            % end

        </div>
    </div>

</div>


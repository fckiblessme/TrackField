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
                <input type="text" name="author" placeholder="Только русские буквы, пробелы и дефисы, 3-50 символов" value="{{ c_author }}">
            </div>

            <div class="comp-form-group">
                <label>Название</label>
                <input type="text" name="comp_name" placeholder="Только буквы, цифры, пробелы, дефисы, точки, 3-100 символов" value="{{ c_comp_name }}">
            </div>

            <div class="comp-form-group">
                <label>Дисциплина</label>
                <select name="discipline">
                    <option value="">Выберите дисциплину</option>
                    <option value="Спортивная ходьба" {{ 'selected' if c_discipline == 'Спортивная ходьба' else '' }}>Спортивная ходьба</option>
                    <option value="Прыжки в высоту" {{ 'selected' if c_discipline == 'Прыжки в высоту' else '' }}>Прыжки в высоту</option>
                    <option value="Бег" {{ 'selected' if c_discipline == 'Бег' else '' }}>Бег</option>
                    <option value="Прыжки в длину" {{ 'selected' if c_discipline == 'Прыжки в длину' else '' }}>Прыжки в длину</option>
                    <option value="Эстафеты" {{ 'selected' if c_discipline == 'Эстафеты' else '' }}>Эстафеты</option>
                    <option value="Прыжки с шестом" {{ 'selected' if c_discipline == 'Прыжки с шестом' else '' }}>Прыжки с шестом</option>
                    <option value="Толкание ядра" {{ 'selected' if c_discipline == 'Толкание ядра' else '' }}>Толкание ядра</option>
                </select>
            </div>

            <div class="comp-form-group">
                <label>Дата проведения</label>
                <input type="date" name="event_date" value="{{ c_event_date }}">
            </div>

            <div class="comp-form-group">
                <label>Описание</label>
                <textarea name="description" rows="7" placeholder="От 20 до 1000 символов, не только цифры и спецсимволы" style="resize: none;">{{ c_description }}</textarea>
            </div>

            <div class="comp-form-group">
                <label>Телефон</label>
                <input type="text" name="phone" placeholder="+7 ххх ххх-хх-хх" value="{{ c_phone }}">
            </div>

            <div class="comp-form-submit">
                <button type="submit" class="btn">Добавить соревнование</button>
            </div>

        </form>
    </div>


    <div class="section">
        <h2>Предстоящие старты </h2>

        <div class="comp-feed">

            % for comp in competitions:
            <div class="comp-card {{ 'comp-card-past' if comp['event_date'] < today else '' }}">                
                <h3 class="comp-card-title">{{ comp['comp_name'] }}</h3>
                <div class="comp-card-badge">{{ comp['discipline'] }}</div>
                <p class="comp-card-desc">{{ comp['description'] }}</p>
                <div class="comp-card-meta">
                    <span>{{ comp['event_date'][8:10] }}.{{ comp['event_date'][5:7] }}.{{ comp['event_date'][0:4] }}</span>
                    <span>{{ comp['author'] }}</span>
                    % if comp['phone']:
                    <span>{{ comp['phone'] }}</span>
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
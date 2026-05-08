% rebase('layout.tpl', title='Партнеры', year=year)

<div class="discipline-hero">
    <h1>Наши партнеры</h1>
</div>

<div class="discipline-content">

    <div class="section">
        <h2>Стать партнером</h2>

        <div class="info-block comp-info-block">
            <p class="info-text">Заполните форму, чтобы добавить информацию о партнёрстве. Компания появится в общем списке ниже.</p>
        </div>

        % if error:
            <div class="comp-error">
                <span class="comp-error-icon">⚠️</span>
                <span>{{ error }}</span>
            </div>
        % end

        <form action="/add-partner" method="post" class="comp-form">
            
            <div class="comp-form-group">
                <label>Наименование компании</label>
                <input type="text" name="name" value="{{ p_name }}">
            </div>

            <div class="comp-form-group">
                <label>Описание деятельности</label>
                <textarea name="description" rows="3" style="resize: none;" >{{ p_desc }}</textarea>
            </div>

            <div class="comp-form-group">
                <label>Дата начала сотрудничества</label>
                <input type="date" name="join_date" value="{{ p_date }}">
            </div>

            <div class="comp-form-group">
                <label>Контактный телефон</label>
                <input type="text" name="phone" placeholder="+7 (XXX) XXX-XX-XX" value="{{ p_phone }}">
            </div>

            <div class="comp-form-submit">
                <button type="submit" class="btn">Зарегистрировать</button>
            </div>

        </form>
    </div>

    <div class="section">
        <h2>Список партнерских компаний</h2>

        <div class="comp-feed">

            % for p in partners:
            <div class="comp-card">
                <div class="comp-card-badge">Партнёр</div>
                <h3 class="comp-card-title">{{ p['name'] }}</h3>
                <p class="comp-card-desc">{{ p['description'] }}</p>
                <div class="comp-card-meta">
                    <span>📅 С нами с: {{ p['join_date'] }}</span>
                    % if p.get('phone'):
                    <span>📞 {{ p['phone'] }}</span>
                    % end
                </div>
            </div>
            % end

            % if len(partners) == 0:
            <p class="comp-empty">Пока нет добавленных партнёров...</p>
            % end

        </div>
    </div>

</div>
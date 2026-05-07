% rebase('layout.tpl', title='Партнерские компании', year=year)

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="/static/style.css">
    <title>Наши партнеры</title>
</head>
<body>
    <nav>
        <a href="/">Главная</a> | <a href="/partners">Партнеры</a>
    </nav>

    <h1>Наши партнёрские компании</h1>

    <form action="/partners" method="post">
        <div>
            <label>Наименование:</label>
            <input type="text" name="name" value="{{values.get('name', '')}}">
            % if 'name' in errors:
                <span class="error">{{errors['name']}}</span>
            % end
        </div>
        <div>
            <label>Описание:</label>
            <textarea name="description">{{values.get('description', '')}}</textarea>
            % if 'description' in errors:
                <span class="error">{{errors['description']}}</span>
            % end
        </div>
        <div>
            <label>Телефон (+7XXXXXXXXXX):</label>
            <input type="text" name="phone" value="{{values.get('phone', '')}}">
            % if 'phone' in errors:
                <span class="error">{{errors['phone']}}</span>
            % end
        </div>
        <button type="submit">Добавить партнера</button>
    </form>

    <hr>

    <div class="partner-list">
        % for item in partners:
            <div class="partner-card">
                <h3>{{item['name']}}</h3>
                <p>{{item['description']}}</p>
                <small>Тел: {{item['phone']}} | Дата: {{item['date']}}</small>
            </div>
        % end
    </div>
</body>
</html>

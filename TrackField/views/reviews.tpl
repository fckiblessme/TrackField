% rebase('layout.tpl', title='Отзывы', year=year)
<meta charset="utf-8" />
<div class="discipline-hero">
    <h1>Отзывы пользователей</h1>
    <p class="discipline-subtitle">Делитесь впечатлениями о тренировках и соревнованиях</p>
 </div>

    <div class="review-form-section">
        <h2>Оставить отзыв</h2>
        <form method="POST" action="/reviews/add" class="review-form">
            <div class="form-group">
                <label for="author">Ваше имя <span class="required">*</span></label>
                <input type="text" 
                       id="author" 
                       name="author" 
                       value="{{form_data.get('author', '')}}" 
                       class="{{'error-input' if errors.get('author') else ''}}">
                % if errors.get('author'):
                    <div class="error-message">{{errors['author']}}</div>
                % end
            </div>
            
            <div class="form-group">
                <label for="text">Ваше мнение <span class="required">*</span></label>
                <textarea id="text" 
                          name="text" 
                          rows="5" 
                          placeholder="Поделитесь своим опытом тренировок или соревнований..."
                          class="{{'error-input' if errors.get('text') else ''}}">{{form_data.get('text', '')}}</textarea>
                % if errors.get('text'):
                    <div class="error-message">{{errors['text']}}</div>
                % end
                <div class="character-counter">Минимум 10 символов</div>
            </div>
            
            <div class="form-row">
                <div class="form-group half">
                    <label for="date">Дата тренировки или соревнований <span class="required">*</span></label>
                    <input type="date" 
                           id="date" 
                           name="date" 
                           value="{{form_data.get('date', '')}}"
                           class="{{'error-input' if errors.get('date') else ''}}">
                    % if errors.get('date'):
                        <div class="error-message">{{errors['date']}}</div>
                    % end
                </div>
                
                <div class="form-group half">
                    <label for="phone">Контактный телефон <span class="required">*</span></label>
                    <input type="tel" 
                           id="phone" 
                           name="phone" 
                           value="{{form_data.get('phone', '')}}" 
                           placeholder="+7 (XXX) XXX-XX-XX"
                           class="{{'error-input' if errors.get('phone') else ''}}">
                    % if errors.get('phone'):
                        <div class="error-message">{{errors['phone']}}</div>
                    % end
                </div>
            </div>
            
            <div class="form-actions">
                <button type="submit" class="btn-submit"> Оставить отзыв</button>
                <button type="reset" class="btn-reset"> Очистить форму</button>
            </div>
        </form>
    </div>
    

    <div class="reviews-list-section">
        <h2>Все отзывы <span class="reviews-count">({{len(reviews)}})</span></h2>
        
        % if not reviews:
            <div class="empty-state">
                <p>Пока нет ни одного отзыва.</p>
            </div>
        % else:
            <div class="reviews-grid">
                % for review in reviews:
                    <div class="review-card">
                        <div class="review-header">
                            <div class="review-author">
                                <span class="author-icon"></span>
                                <strong>{{review['author']}}</strong>
                            </div>
                            <div class="review-date">
                                {{review['date']}}
                            </div>
                        </div>
                        <div class="review-content">
                            <p>{{review['text']}}</p>
                        </div>
                        <div class="review-footer">
                            <span class="review-phone">{{review['phone']}}</span>
                        </div>
                    </div>
                % end
            </div>
        % end
    </div>

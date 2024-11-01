import streamlit as st
import random

# Установка основной цветовой схемы и стилей
st.set_page_config(page_title="Event Planning Simulation", page_icon="🎉")

# Основные стили
st.markdown("""
    <style>
    .title {
        font-size: 2em;
        color: #1E90FF;
        font-weight: bold;
    }
    .subheader {
        font-size: 1.5em;
        color: #333333;
    }
    .task {
        font-size: 1.2em;
        color: #555555;
    }
    .result {
        font-size: 1.3em;
        font-weight: bold;
        color: #228B22;
    }
    .section-divider {
        border-top: 1px solid #D3D3D3;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Заголовок приложения
st.markdown('<p class="title">Event Planning: Traditional vs. rentArest</p>', unsafe_allow_html=True)

st.write("### Сравните традиционный способ планирования мероприятий и автоматизацию с помощью rentArest.")
st.write("**Цель**: Увидеть, насколько rentArest экономит ваше время и усилия при планировании мероприятий.")

# Симуляция традиционного способа
def traditional_method():
    st.markdown('<p class="subheader">Традиционный способ</p>', unsafe_allow_html=True)
    total_time = 0
    tasks = [
        ("Поиск подходящего места", random.randint(10, 15)),
        ("Согласование даты с площадкой", random.randint(5, 10)),
        ("Поиск кейтеринга", random.randint(8, 12)),
        ("Заказ услуг развлечения", random.randint(6, 10)),
        ("Обеспечение транспортировки", random.randint(4, 8))
    ]

    for task, duration in tasks:
        st.markdown(f'<p class="task">• {task}... ({duration} минут)</p>', unsafe_allow_html=True)
        total_time += duration

    st.markdown(f'<p class="result">Всего времени потрачено на традиционное планирование: {total_time} минут</p>', unsafe_allow_html=True)
    return total_time

# Симуляция с rentArest
def rentArest_method():
    st.markdown('<p class="subheader">Планирование с помощью rentArest</p>', unsafe_allow_html=True)
    total_time = 0
    tasks = [
        ("Выбор типа мероприятия и бюджета", 2),
        ("Получение рекомендаций площадок", 1),
        ("Выбор кейтеринга и развлечений", 1),
        ("Подтверждение заказа", 1)
    ]

    for task, duration in tasks:
        st.markdown(f'<p class="task">• {task}... ({duration} минуты)</p>', unsafe_allow_html=True)
        total_time += duration

    st.markdown(f'<p class="result">Всего времени потрачено на планирование с rentArest: {total_time} минуты</p>', unsafe_allow_html=True)
    return total_time

# Основной блок приложения
if st.button("Начать симуляцию"):
    traditional_time = traditional_method()
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    rentArest_time = rentArest_method()

    # Сравнение результатов
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Результаты:</p>', unsafe_allow_html=True)
    st.write(f"Традиционное планирование заняло: **{traditional_time} минут**.")
    st.write(f"Планирование с rentArest заняло: **{rentArest_time} минуты**.")

    if rentArest_time < traditional_time:
        st.markdown(f'<p class="result">Вы сэкономили {traditional_time - rentArest_time} минут благодаря rentArest!</p>', unsafe_allow_html=True)
        st.success("rentArest упрощает процесс и экономит ваше время.")
    else:
        st.info("С rentArest вы получаете удобство и меньше стресса!")

st.write("Нажмите на кнопку выше, чтобы начать!")

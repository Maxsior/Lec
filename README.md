# О Lec

**Lec** - это язык для быстрого и гибкого описания графики.

# Философия языка

**Lec** ориентирован на ручное описание графики, отсюда вытекают основные принципы, воплощённые в языке:
- легко читается
- просто пишется
- быстро изучается (1 лекция = ~90мин)
- декларативный
- лаконичный
- простая грамматика
- встраиваемый
- расширяемый

# Пример сцены
```lec
e:
    ellipse
        stroke 1

r:
    rectangle
        text "some text"
        fill "blue"

arrow
    direction r e
    text "arrow"
```

<img src="https://raw.githubusercontent.com/Maxsior/Lec/main/examples/imgs/scene.png" alt="Изображение сцены" width="300px">

# TIkTakToe
## Gomoku-Beginner
Реализация игры "обратные" крестики-нолики 
Логика данной версии проста. 
Компьютер, если не "видит" шанса на поражение или победу, просто "дурачится"
### О программе 
Игрок ходит первым. Под игровым полем присутвует кнопка новой игры. При нажатии на нее игровое поле обновляется, очищая игровое поле,
после чего игра начинается заново. Игрок ходит крестиками, а компьютер - ноликами. Побеждает тот, у кого получится ряд
из пяти фигур. Если все поле будет заполнено фигурами и рядов из 5 фигур не будет, то игра заканчивается ничьей.
### Логика игры
Компьютер ходит используя несколько паттернов предпобедной серии:
-XXXX
X-XXX
XX-XX
XXX-X
XXXX-
-XXX-
Последний паттерн обЪяснен необходимостью предугадать победный паттерн -XXXX- где в независимости от хода компьютера игрока ждет победа.


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку

import re
from collections import Counter


def top_ten_words(input_string):
    no_punctuation = re.sub(r'[^\w\s]', '', input_string) #удаляем в строке все, что не пробел и не слово
    words = no_punctuation.lower().split() #создаем список слов, разбивая строку по пробелам
    counter = Counter(words) #создаем словарь counter, где ключи - это слова, а значения - количество их повторений
    top_ten = counter.most_common(10)
    return top_ten


text = '''Битва за Мидуэй
Материал из Википедии — свободной энциклопедии
Текущая версия страницы пока не проверялась опытными участниками и может значительно отличаться от версии, проверенной 9 июня 2022 года; проверки требуют 19 правок.
Мидуэйское сражение
Основной конфликт: Вторая мировая война, Война на Тихом океане
Сражение у атолла Мидуэй. Диорама сражения
Сражение у атолла Мидуэй. Диорама сражения
Дата	4—7 июня 1942 года
Место	Окрестности атолла Мидуэй
Итог	Тактическая и стратегическая победа США
Противники
 США

 Японская империя

Командующие
Соединённые Штаты Америки Честер Нимиц
Соединённые Штаты Америки Фрэнк Флетчер
Соединённые Штаты Америки Рэймонд Спрюэнс

Флаг ВМС Японии Исороку Ямамото
Флаг ВМС Японии Тюити Нагумо
Флаг ВМС Японии Нобутакэ Кондо
Флаг ВМС Японии Тамон Ямагути

Силы сторон
3 авианосца,
7 тяжёлых крейсеров,
1 лёгкий крейсер,
15 эсминцев,
233 палубных самолёта,
127 самолётов наземного базирования,
16 подводных лодок[1]

4 авианосца,
2 линейных крейсера,
2 тяжёлых крейсера,
1 лёгкий крейсер,
12 эсминцев,
248 палубных самолётов[2],
16 гидросамолётов

не принимали участия в сражении:
2 лёгких авианосца,
5 линкоров,
4 тяжёлых крейсера,
2 лёгких крейсера,
около 35 кораблей поддержки

Потери
1 авианосец,
1 эсминец,
ок. 362 человек,
144 самолёта[3]

4 авианосца,
1 тяжёлый крейсер потоплен,
1 тяжёлый крейсер серьёзно повреждён,
3057 человек[4],
248 самолётов[5]

Логотип Викисклада Медиафайлы на Викискладе
[скрыть]Перейти к шаблону «Тихоокеанский театр военных действий Второй мировой войны» 
Тихоокеанский театр военных действий Второй мировой войны
Перл-ХарборТаиландБирмаМалайяГонконгФилиппины (1941–1942)Гилберта и Маршалловы острова (1942)ГуамУэйкГолландская Ост-ИндияПортугальский ТиморАвстралияНовая ГвинеяСингапурИндийский океанРейд на ТокиоСоломоновы островаКоралловое мореМидуэйАлеутские островаАндаманские островаГилберта и Маршалловы острова (1943—1944)ИндияФилиппины (1944–1945)Бомбардировка Токио 10 марта 1945 годаМарианские островаБорнеоРюкюХиросима и НагасакиМаньчжурия-Сахалин
Сражение у атолла Мидуэй, Мидуэйское сражение[6][7] (англ. Battle of Midway, 4-7 июня 1942 года), (яп. ミッドウェー海戦 миддоуэ кайсэн) — крупное морское сражение Второй мировой войны на Тихом океане. Решительная победа флота США над силами японского ВМФ. Стало поворотной точкой в войне на Тихом океане. Японская авианосная группа потеряла 4 тяжёлых авианосца, 256 самолётов (с учётом авиации крейсеров)[8], что лишило японский флот возможности эффективно действовать вне зон прикрытия береговой авиации.


Содержание
1	Планы сторон
1.1	Императорская Япония
1.2	Соединённые Штаты Америки
2	Ход сражения
2.1	Первые столкновения
2.2	Битва авианосцев
2.3	Атака американской подводной лодки «Наутилус»
2.4	Ответная атака японцев
2.5	Атака «Хирю» пикирующими бомбардировщиками
3	Итоги
3.1	Потери Императорского военно-морского флота Японии
3.2	Потери Тихоокеанского военно-морского флота США
3.3	Прекращение операции и приказ об отходе
4	Стратегические последствия
5	Память
5.1	Императорская Япония
5.2	Соединённые Штаты Америки
6	В культуре
7	Примечания
8	Литература
9	Ссылки
Планы сторон
Императорская Япония
Не существует единого мнения о причинах, побудивших японцев атаковать атолл Мидуэй. Принято считать, что со стороны японского флота целью операции, включавшей отвлекающую атаку на Алеутские острова, являлось уничтожение американских авианосцев и окончательная нейтрализация Тихоокеанского флота США. Японцы намеревались занять Мидуэй с целью расширения «защитного периметра» своих островов. Операция служила подготовкой к дальнейшему наступлению на острова Фиджи и Самоа, а также к возможному вторжению на Гавайи.

Не рискуя совершать повторное нападение на основную базу американского флота в Пёрл-Харборе, японское командование решило атаковать базу на атолле Мидуэй, а затем уничтожить авианосцы противника в случае, если последние придут на выручку гарнизону[9]. Как и в случае с атакой на Пёрл-Харбор, была сделана ставка на внезапность нападения.

Силы японского флота были разделены на две части:

ударная группа авианосцев (командующий — адмирал Нагумо)
группа линкоров с сопровождением (командующий — адмирал Ямамото)
Соединённые Штаты Америки
Расчёт японцев на внезапность не оправдался. В мае 1942 группа криптографов Тихоокеанского флота (HYPO) сумела взломать японский военно-морской код JN-25 и получить сведения, что следующей целью атаки японского флота будет некая цель «AF» в Тихом океане. Проблема была в том, что американское командование не могло идентифицировать цель «АF». Возможно, это был атолл Мидуэй или база Пёрл-Харбор на Гавайях. Для проверки было отправлено сообщение о нехватке воды на атолле Мидуэй. Вскоре была перехвачена японская шифровка: «Неполадки с водоснабжением на „АF“»[10][11].

На основе этой информации командующий американским тихоокеанским флотом адмирал Честер Нимиц спланировал ответные действия. Американские авианосцы «Энтерпрайз», «Хорнет» и «Йорктаун» были скрытно выдвинуты к северо-востоку от атолла Мидуэй и полностью подготовлены к бою. Контр-адмирал Рэймонд А. Спрюэнс возглавил 16-е оперативное авианосное соединение, ядро которого составляли авианосцы «Хорнет» и «Энтерпрайз». Контр-адмирал Фрэнк Дж. Флетчер командовал 17-м оперативным авианосным соединением, главным кораблём которого был авианосец «Йорктаун». Таким образом, хотя японские силы имели значительное численное превосходство, внезапность оказалась на стороне США.

Ход сражения
Первые столкновения

Martin B-26-MA Marauder «Susie-Q», 18th Reconnaissance Squadron, 22nd Bombardment Group USAAF
В 9:25 3 июня пилот взлетевшего с Мидуэя американского разведывательного гидросамолёта «Каталина» младший лейтенант Джек Ред, обнаружив японскую группировку, идущую к Мидуэю, передал сообщение из двух слов: «Главные силы».

Первый удар нанесли американцы: девять тяжёлых бомбардировщиков B-17 Flying Fortress («Летающая крепость»), поднявшись с базы Мидуэй, в 16:23 нанесли удар по транспортным судам японской группировки. Как выяснилось позднее, ни одна бомба в цель не попала.

В 4:30 утра 4 июня стартовала первая волна японских бомбардировщиков и истребителей прикрытия. В 4:45 самолёты построились и легли на заданный курс — 36 торпедоносцев Nakajima B5N «Кейт» с авианосцев «Хирю» и «Сорю», 36 пикирующих бомбардировщиков «Вэл» с авианосцев «Кага» и «Акаги» и 36 истребителей «Зеро», по 9 с каждого авианосца. Истребителями прикрытия командовал лейтенант Суганами Минору. В 6:20 атакующая группа из 108 самолётов достигла атолла и нанесла удар по базе, причинив ей значительные разрушения.

Американские истребители F4F-3 и F2A-3 (под командованием майора Паркса и капитана Армстейда), находившиеся на базе, вступили в бой и, несмотря на тяжёлые потери, сбили несколько бомбардировщиков и, по меньшей мере, три «Зеро». Большинство американских машин было сбито истребителями лейтенанта Суганами. Вернулись 10 самолётов из 25, причём 4 разбились при посадке. 221-я авиагруппа была уничтожена.

Бо́льших успехов добилась зенитная артиллерия: было сбито около трети атаковавших бомбардировщиков[12].

Руководивший атакой лейтенант Томонага доложил, что американские бомбардировщики успели покинуть базу до налёта и наземная оборона не подавлена, поэтому перед высадкой десанта потребуется ещё один удар с воздуха[13].

В 5:34 пилот взлетевшей с Мидуэя «Каталины» Говард Эди сообщил об обнаружении японских авианосцев. Американские бомбардировщики с Мидуэя действительно успели подняться до японского налёта и нанесли удар по японским авианосцам. Атакующая группа состояла из шести торпедоносцев Grumman TBF Avenger (лейт. Файберлинг, они поднялись с Мидуэя в 6:10) и четырёх бомбардировщиков Martin B-26 Marauder (кап. Коллинз), также вооружённых торпедами. Из-за отсутствия истребителей прикрытия с американской стороны, атака была отбита японскими истребителями без заметного ущерба для кораблей, при этом были сбиты все атакующие самолёты, кроме одного Avenger’а и двух B-26[14].

В соответствии с японской доктриной того времени, командующий авианосной группой адмирал Нагумо держал половину своих самолётов в резерве на случай отражения атаки авианосцев противника. Всего было 36 пикирующих бомбардировщиков с «Хирю» и «Сорю», 36 торпедоносцев с «Кага» и «Акаги» и 36 истребителей, снова по 9 с каждого авианосца. Соответственно цели, резервные самолёты были вооружены торпедами. После отражения первого налёта американцев Нагумо решил, что опасность атаки миновала, и приказал перевооружить резерв бомбами для повторной атаки Мидуэя.

Приказ был отдан в 7:15, и работы по перевооружению были в разгаре, когда в 7:40 поступило сообщение от самолёта-разведчика об обнаружении значительных американских сил. Нагумо немедленно отменил предыдущий приказ, и на резервные самолёты вновь стали подвешивать торпеды. Ещё через полчаса от разведчика поступило сообщение, что обнаружен всего один авианосец противника (остальные не были обнаружены). При этом из-за нехватки персонала на ангарных палубах оставались и авиабомбы, и торпеды, которые не успевали спустить в надёжно защищённые погреба. Этот фактор создавал опасную ситуацию — авиабомбе было достаточно пробить верхнюю палубу, чтобы сдетонировали все находившиеся на ангарной палубе боеприпасы (вдвое больше, чем при обычном положении).

Битва авианосцев
Проанализировав поступившие к 7:00 радиосообщения о ходе воздушной атаки на Мидуэй, американские моряки подсчитали, что японские самолёты вернутся на свои авианосцы около 9:00. Чтобы атаковать японские авианосцы, когда те будут принимать и заправлять самолёты, Спрюэнс отдал приказ о немедленном взлёте с авианосцев всех имеющихся самолётов. С «Хорнет» и «Энтерпрайз» взлетели 117 самолётов: 68 пикирующих бомбардировщиков, 29 торпедоносцев, 20 истребителей. Но, завершив приём самолётов первой волны, японский флот изменил курс и направился на северо-восток. В результате, когда 35 пикирующих бомбардировщиков и 10 истребителей с авианосца «Хорнет» прилетели в район, где, по расчётам американцев, должен был находиться японский флот, его там не оказалось, и эти самолёты легли на обратный курс.

В 7:50 к японскому флоту подошла эскадрилья из 16 пикирующих бомбардировщиков «Донтлес» под командованием майора Хендерсона (отдельно шла группа из 11 пикировщиков «Виндикейтор»). Самолёт Хендерсона был сбит ещё на подходе, и командование принял капитан Эльмер Глайден. Часть пикировщиков атаковала авианосец «Хирю» с пологого пикирования.

В 8:08 авианосец увернулся от четырёх бомб. В 8:12 ещё две бомбы легли справа. Корабль тряхнуло и засыпало осколками. Четыре матроса были убиты, шесть ранено[15].

Три бомбардировщика атаковали авианосец «Кага», не добившись попаданий. Практически все американские пикировщики были сбиты.

В 8:14 тяжёлый крейсер «Тонэ» открыл огонь орудиями левого борта, сигнализируя о появлении тяжёлых бомбардировщиков Boeing B-17 Flying Fortress (под командованием полковника Суини) на высоте 6500 метров. Японские истребители прикрытия осторожно атаковали их в течение 10 минут, не нанеся существенных повреждений. «Летающие крепости» сбросили бомбы и в 8:20 ушли. «Сорю» и «Хирю» не получили никаких повреждений.

Именно в этот момент (8:20) пришло новое сообщение с японского гидросамолёта № 4, который следил за американскими кораблями:

Колонну противника замыкает корабль, похожий на авианосец.

В 8:17 появилась группа «Виндикейторов» (под командованием майора Бенджамина Норриса), которая взлетела с аэродрома на Мидуэе вместе с эскадрильей Хендерсона, но отстала от неё. С высоты 150 метров они атаковали линейный крейсер «Харуна».

Капитан 1-го ранга Такама блестяще управлял линейным кораблём «Харуна». Американцы сбрасывали одну бомбу за другой, но старый линкор ухитрился увернуться от всех. Два близких разрыва были отмечены в 8:29, но командир дивизиона живучести капитан 3-го ранга Иосино доложил, что они не причинили никаких повреждений.

Эта эскадрилья тоже не смогла повредить японский флот[15].


Последний торпедоносец «Девастейтор» из 8-й эскадрильи поднимается с палубы авианосца Хорнет 4 июня 1942.
В 8:55 японский флот получил предупреждение от разведывательного самолёта:

Десять торпедоносцев противника идут прямо на вас.

Это была 8-я торпедоносная эскадрилья, ведомая капитаном 3-го ранга Джоном Уолдроном. Они поднялись примерно в 7:00 с авианосца «Хорнет». В 9:18 15 торпедоносцев «Девастейтор» атаковали соединение Нагумо. Не считая Уолдрона, вся эскадрилья состояла из резервистов, призванных всего несколько месяцев назад. В приказе Уолдрона, написанном накануне сражения, говорилось:

Если останется лишь один самолёт для последнего захода, то я хочу, чтобы этот пилот прорвался и попал. Пусть Бог будет с нами. Удачи, счастливого приземления и покажите им[16].

Несмотря на то, что все пилоты 8-й эскадрильи были новичками, они, не колеблясь, шли на авианосец прямым курсом, хотя до цели было ещё целых 10 миль. Японские истребители прикрытия сбили все торпедоносцы, кроме самолёта Джорджа Гэя, который успел сбросить торпеду и несколько позже, повреждённый, посадил машину на воду. 8-я торпедоносная эскадрилья была полностью уничтожена. Это была шестая американская атака за утро.

Огонь по эскадрилье Уолдрона был прекращён в 9:36, а уже в 9:38 японцев атаковала 6-я эскадрилья торпедоносцев под командованием капитана 3-го ранга Линдси (14 самолётов «Девастейтор»). В 9:40 Линдси приказал эскадрилье разделиться на два отряда и атаковать японский авианосец («Кага») с двух сторон. В 15 милях от авианосца их атаковали 25 истребителей «Зеро». Только 4 торпедоносца вышли на линию атаки (9:58), сбросили торпеды и повернули обратно. Линдси погиб в этой атаке. Повредить авианосец не удалось.

В 8:45 с авианосца «Йорктаун» начали взлёт 12 торпедоносцев «Девастейтор» капитана 3-го ранга Месси. Его эскадрилья была перехвачена в 15 км от японских авианосцев. Торпедоносцы смогли прорваться к японскому флоту, идя на высоте 50 метров, и разделились на 2 группы для атаки с двух сторон. В этот момент капитан Месси был сбит. Командование принял старшина Эдерс. 4 самолёта смогли сбросить торпеды, из них два были сразу сбиты, а 2 вернулись на авианосец. Это была 8-я американская атака за утро, и в 10:15 атакующие самолёты были уничтожены[15].

В этот момент было завершено перевооружение японских бомбардировщиков, и 93 машины, ожидая сигнала, стояли на полётных палубах. Удар по американскому флоту было решено нанести в 10:30. В 10:20 Нагумо приказал поднять самолёты, и авианосцы начали разворот на ветер.


Кларенс Маккласки (фото 1943—1944)
Примерно в 7:45 капитан 3-го ранга Кларенс Уэйд Маккласки (англ. Clarence Wade McClusky) с авианосца «Энтерпрайз» повёл свои самолёты в сторону японского флота. С ним шла 6-я разведывательная эскадрилья лейтенанта Эрла Галлахера и 6-я бомбардировочная эскадрилья лейтенанта Ричарда Беста, всего 30 пикировщиков «Донтлес».

Капитан 3-го ранга Макс Лесли поднял свои 17 пикировщиков «Донтлес» (3-ю бомбардировочную эскадрилью) с авианосца «Йорктаун» около 8:55, вместе с эскадрильей Месси. Сразу после взлёта его самолёты потеряли 4 бомбы.

Маккласки вышел в точку перехвата в 9:20, но не обнаружил там японский флот. Ему потребовалось около часа, чтобы его найти. Он заметил корабли в 10:05 на расстоянии 35 миль. Они атаковали авианосцы: по недоразумению, Маккласки и 25 самолётов атаковали один авианосец, а Бест и 5 самолётов — другой.

Капитан 3-го ранга Маккласки, пикировавший первым, видел совершенно не повреждённую полётную палубу с самолётами, стоявшими в полной готовности к вылету на корме. Эрл Галлахер, пикирующий четвёртым, заметил столбы воды от двух близких разрывов и взрыв своей собственной бомбы, разорвавшейся среди стоявших на палубе самолётов. Младший лейтенант Клайс, пикирующий седьмым, видел уже море огня, бушевавшего на корме авианосца, но совершенно не повреждённый центр полётной палубы с нарисованным на ней красным кругом. Именно в этот круг и угодила его бомба. Так всё и продолжалось до младшего лейтенанта Голдсмита, пикировавшего последним. Голдсмит ясно видел, как авианосец, который теперь представлял собой пылающий остов, пытался маневрировать в отчаянной попытке избежать дальнейших попаданий[15].

В этот самый момент (10:25) Макс Лесли (он должен был атаковать вместе с эскадрильей Месси, но потерял её и искал около 15 минут) пошёл в атаку на другой авианосец. 14 самолётов атаковали авианосец, а последние 4 сбросили бомбы на эсминец и линкор.

Таким образом, две группы бомбардировщиков совершено независимо нанесли одновременный удар по трём различным авианосцам — «Акаги», «Кага» и «Сорю». До сих пор точно не установлено, кто какой авианосец атаковал, предположительно, первым был атакован «Кага». Японские истребители были заняты уничтожением эскадрильи Месси, зенитного огня тоже не было.

«Сорю» и «Кага» затонули вечером 4 июня.

Атака американской подводной лодки «Наутилус»
Через два часа после атаки бомбардировщиков американская подводная лодка «Наутилус» выпустила 3 торпеды по японскому авианосцу. В боевом рапорте «Наутилуса» говорится, что лодка выпустила торпеды между 13:59 и 14:05 с дистанции 2500 метров при угле встречи 125 градусов, после чего погрузилась на 92 метра.

Командир «Наутилуса» капитан 3-го ранга Билл Брокман был уверен, что атаковал и потопил авианосец «Сорю». Однако, по японским данным, тремя торпедами был атакован авианосец «Кага», причём две торпеды прошли мимо, а третья не разорвалась.

Билл Брокман до самой смерти полагал, что потопил «Сорю», подводная лодка «Наутилус» именно так и вошла в американскую историю[17].

Ответная атака японцев
Для нанесения ответного удара по американскому флоту на «Хирю» удалось собрать 18 пикирующих бомбардировщиков «99» под командованием лейтенанта Митио Кобаяси и всего шесть истребителей «Зеро» для сопровождения (под командованием лейтенанта Сигемацу). Бомбардировщики несли 250-кг бомбы. В 10:54 первые «Зеро» поднялись с полётной палубы, а в 10:58 поднялись пикировщики. В 11:45 раздался сигнал воздушной тревоги на «Йорктауне», авианосец увеличил скорость, его прикрывали крейсеры «Астория» и «Портленд». На перехват было поднято 12 истребителей под командованием капитана 3-го ранга Педерсона. Во время атаки были сбиты 5 японских пикировщиков, но 7 прорвались к авианосцу и добились трёх попаданий. Обратно на «Хирю» вернулись 5 пикировщиков и 1 истребитель.


Американские пикировщики SBD Dauntless заходят в атаку на горящий крейсер «Микума»

Авианосец «Йорктаун» был серьёзно повреждён
Сразу же было принято решение о второй атаке. Было поднято в воздух 10 торпедоносцев Nakajima B5N (Т-97) под командованием лейтенанта Томонага и 6 истребителей лейтенанта Мори. Об их приближении на «Йорктауне» узнали в 14:20. Торпедоносцы атаковали двумя группами по 5 самолётов, живыми из боя вышла только одна группа (лейтенанта Хасимото) из пяти торпедоносцев и три истребителя. Бой окончился в 14:52. Торпедоносцы добились двух точных попаданий.

Авианосец «Йорктаун» (капитан 1-го ранга Букмастер) был тяжёло повреждён, с него сняли экипаж и взяли на буксир к Пёрл-Харбору. 7 июня 1942 года японская подводная лодка потопила авианосец и находившийся у его борта эсминец.

Атака «Хирю» пикирующими бомбардировщиками
Уже в момент японской атаки на «Йорктаун» пришло сообщение об обнаружении последнего японского авианосца («Хирю»). У американцев уже не осталось ни одного торпедоносца, поэтому на «Энтерпрайзе» была создана смешанная группа из пикировщиков, всего 25 самолётов. Возглавил авиагруппу лейтенант Эрл Галлахер. Сразу за ними (16:03) с «Хорнета» поднялось ещё 16 пикировщиков.

В 16:58 Галлахер повёл пикировщики в атаку. «Хирю» прикрывало только 6 истребителей. В 17:03 японский сигнальщик сообщил об атаке американских самолётов, но времени отреагировать на атаку у японцев уже не оказалось: пикировщики добились четырёх попаданий 1000-фунтовыми бомбами, которые вызвали взрывы и многочисленные пожары в трюмах, справиться с которыми команде не удалось. Несколько позже на японский флот сбросили бомбы несколько B-17, но не добились ни одного попадания. Из эскадрильи Галлахера не вернулось 3 самолёта.


B-17 атакуют «Хирю».
Ночью японский отряд из 4 тяжёлых крейсеров, направленных для обстрела Мидуэя, сделал резкий поворот из-за обнаруженной американской подводной лодки. При этом замыкающий крейсер «Могами» врезался в идущий перед ним крейсер «Микума». На «Могами» была разрушена носовая часть, на «Микуме» началась утечка топлива. Оба повреждённые крейсера в сопровождении двух эсминцев стали отходить к ближайшей базе — острову Трук.

По приказу адмирала Ямагути безнадёжно повреждённые «Акаги» и «Хирю» были затоплены японцами утром 5 июня в 05.10. В этот день самолёты с Мидуэя атаковали японские повреждённые крейсеры. Добиться попаданий им не удалось. В исторической литературе встречается информация, что один загоревшийся пикировщик врезался в «Микуму» и нанёс ему тяжёлые повреждения, однако документально этот факт не подтверждён[Комм. 1]. 58 пикирующих бомбардировщиков с «Хорнета» и «Энтерпрайза» безуспешно искали главные силы японцев, уходивших на запад и находившихся в зоне плохой погоды.

6 июня американские самолёты с авианосцев вновь атаковали японские тяжёлые крейсеры «Микума» и «Могами». «Микума» был потоплен, «Могами» получил новые повреждения, но добрался до порта.

Итоги
Потери Императорского военно-морского флота Японии

Горящий «Хирю»

Спасённый лётчик
Около 2 500 человек личного состава.
256 самолётов морского базирования (с учётом авиации крейсеров).
4 тяжёлых авианосца: «Акаги», «Кага», «Сорю», «Хирю».
тяжёлый крейсер «Микума».
Среди погибших в сражении — 110 опытных пилотов и членов экипажей японской палубной авиации.[источник не указан 307 дней]

Командир 2-й дивизии авианосцев контр-адмирал Ямагути и командир авианосца «Хирю» капитан 1-го ранга Каку отказались покинуть тонущий «Хирю» и погибли вместе с кораблём. Командующий ударной группировкой вице-адмирал Тюити Нагумо и раненый Кусака пытались покончить жизнь самоубийством, но офицерам удалось уговорить их не делать этого.

Потери Тихоокеанского военно-морского флота США
Около 362 человек личного состава.
144 самолёта наземного и морского базирования.
1 эсминец.
1 тяжёлый авианосец «Йорктаун»[3].
Прекращение операции и приказ об отходе
Потеряв 4 тяжёлых авианосца и тяжёлый крейсер, а также более двухсот боевых самолётов палубной авиации, главнокомандующий Объединённым императорским флотом адмирал Ямамото в 23:55 4-го июня был вынужден отдать приказ о прекращении наступательных действий и возвращению остатков ударной группировки к берегам Японии. К этому времени в распоряжении Ямамото всё ещё оставалось около 100 кораблей, в том числе 11 линкоров.

Стратегические последствия
После сражения у атолла Мидуэй Императорская Япония потеряла инициативу в войне и была вынуждена перейти к оборонительным действиям. В результате операции уже через месяц японская императорская ставка отдала приказ об отсрочке боевых действий против Новой Каледонии, Фиджи и Самоа[19].

В стратегии и тактике войны на море произошли необратимые изменения.

«Битва авианосцев» — морское сражение, в котором корабли противника даже не сблизились для визуального контакта и артиллерийской дуэли, показала, что авианосец как тип нового боевого корабля стал главенствовать на Тихом океане, а затем и во всей акватории Мирового океана.

Соединённые Штаты Америки сделали далеко идущие выводы из результатов сражения 1942 года у атолла Мидуэй. Наряду со строительством тяжёлых атомных подводных лодок, на вооружении ВМС США всегда находятся боеготовые авианосные соединения, способные выполнять как оборонительные, так и наступательные задачи.

Память
Императорская Япония
Командиру 2-й дивизии авианосцев контр-адмиралу Тамону Ямагути, который отказался покинуть борт авианосца «Хирю» и погиб вместе с флагманом, согласно традициям японского Императорского флота присвоено звание вице-адмирала посмертно.

Соединённые Штаты Америки
В память о победе название «Мидуэй» носили несколько кораблей ВМС США. В американской традиции все они имеют стандартное название USS Midway.

USS Midway (AG-41) — транспорт. На службе с 1942 по 1946 год. 3 апреля 1943 года переименован в USS Panay (AG-41).
USS Midway (CVE-63) — эскортный авианосец, тип «Касабланка». Спущен на воду в 1943 году. Год спустя переименован в USS St. Lo. Потоплен самолётом камикадзе 25 октября 1944 года.
В американской кораблестроительной промышленности согласно традиции вся серия однотипных тяжёлых авианосцев ВМС США носит кодовое название по имени первого спущенного на воду боевого корабля. Отсюда серия тяжёлых эскортных авианосцев тип «Мидуэй». Начало строительства кораблей серии — 1943 год.

USS Midway (CV-41) — первый тяжёлый американский авианосец, головной корабль серии, тип «Мидуэй». Принимал участие в бомбардировках Северного Вьетнама, а также принимал участие в операции «Буря в пустыне» в 1991 году. Находился в составе американских ВМС 47 лет. Выведен из состава флота 11 апреля 1992 года. С 1998 года — корабль-музей в городе Сан-Диего.
В 1949 году имя «Мидуэй» было присвоено Чикагскому международному аэропорту.

В культуре
Этим событиям шведская пауэр-метал-группа Sabaton посвятила свою песню «Midway»[20].
Художественный фильм «Мидуэй[en]» (1976, США, реж. Джек Смайт).
Художественный фильм «Мидуэй» («Midway», США, Китай, 2019).'''

print(top_ten_words(text))

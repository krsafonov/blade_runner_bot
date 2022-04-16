from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.calback_data import get_callback



start = InlineKeyboardMarkup(row_width=2)#made the first keyboard for buttons with the begging buttons

start_viza = InlineKeyboardButton(text="Консульский отдел", callback_data=get_callback.new(item_name="basic info"))
start.insert(start_viza)

subscribe = InlineKeyboardButton(text="Рассылка новостей", callback_data=get_callback.new(item_name="to subscribe"))
start.insert(subscribe)

viza2_info = InlineKeyboardButton(text="Визовая информация", callback_data=get_callback.new(item_name="main viza info"))
start.insert(viza2_info)

covid_measures = InlineKeyboardButton(text="Covid-19", callback_data=get_callback.new(item_name="covid"))
start.insert(covid_measures)

another = InlineKeyboardButton(text="То что не относится к консульскому отделу", callback_data=get_callback.new(item_name="another"))
start.insert(another)





back_to_start = InlineKeyboardMarkup(row_width=2)#made button for getting back to start from any option
startback = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="back_to_start"))
back_to_start.insert(startback)




another2 = InlineKeyboardMarkup(row_width=2)#made keyboards for buttons for another data and add return button

news_events = InlineKeyboardButton(text="События", callback_data=get_callback.new(item_name="events"))
another2.insert(news_events)

politics = InlineKeyboardButton(text="Политика", callback_data=get_callback.new(item_name="polit"))
another2.insert(politics)

trade = InlineKeyboardButton(text="Экономика", callback_data=get_callback.new(item_name="trade"))
another2.insert(trade)

culture = InlineKeyboardButton(text="Культура", callback_data=get_callback.new(item_name="cul"))
another2.insert(culture)

war = InlineKeyboardButton(text="Чехи в войне", callback_data=get_callback.new(item_name="war"))
another2.insert(war)

about = InlineKeyboardButton(text="О посольстве ", callback_data=get_callback.new(item_name="about"))
another2.insert(about)

another = InlineKeyboardButton(text="Вернуться в начало", callback_data=get_callback.new(item_name="startback"))
another2.insert(another)


back_to_another = InlineKeyboardMarkup(row_width=2)#made button which getting back to another from any button

aback = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="aback"))
back_to_another.insert(aback)


viza_info = InlineKeyboardMarkup(row_width=2)#made keyboard from bu


long_term = InlineKeyboardButton(text="Долгосрочная виза", callback_data=get_callback.new(item_name="long term viza"))
viza_info.insert(long_term)


shengen = InlineKeyboardButton(text="Шенгенская виза", callback_data=get_callback.new(item_name="shengen"))
viza_info.insert(shengen)


permission = InlineKeyboardButton(text="Постоянное проживание", callback_data=get_callback.new(item_name="constant"))
viza_info.insert(permission)


permission_long = InlineKeyboardButton(text="Долгосрочное проживание", callback_data=get_callback.new(item_name="long_live"))
viza_info.insert(permission_long)


basic = InlineKeyboardButton(text="Основная информация", callback_data=get_callback.new(item_name="basic"))
viza_info.insert(basic)


fee = InlineKeyboardButton(text="Консульские сборы", callback_data=get_callback.new(item_name="fee"))
viza_info.insert(fee)


blanks = InlineKeyboardButton(text="Бланки", callback_data=get_callback.new(item_name="blanks"))
viza_info.insert(blanks)


cl = InlineKeyboardButton(text="Не нуждаются в визе", callback_data=get_callback.new(item_name="country_list"))
viza_info.insert(cl)


branch = InlineKeyboardButton(text="Визовые центры", callback_data=get_callback.new(item_name="viza_center"))
viza_info.insert(branch)


ter = InlineKeyboardButton(text="Сфера деятельности", callback_data=get_callback.new(item_name="ter"))
viza_info.insert(ter)


backtostart = InlineKeyboardButton(text="Вернуться в начало", callback_data=get_callback.new(item_name="back_to_start"))
viza_info.insert(backtostart)



backtostart1 = InlineKeyboardMarkup(row_width=2)

backtostart = InlineKeyboardButton(text="Вернуться в начало", callback_data=get_callback.new(item_name="backrt"))

backtostart1.insert(backtostart)



backtovizainfo1 = InlineKeyboardMarkup(row_width=2)

aback12 = InlineKeyboardButton(text="Вернуться в визовую информацию", callback_data=get_callback.new(item_name="aback1"))
backtovizainfo1.insert(aback12)


get_notified = InlineKeyboardMarkup(row_width=2)#made keyabord for buttons which make you notified and gives option to cancel or get list of news

unsubscribe = InlineKeyboardButton(text="Отменить", callback_data=get_callback.new(item_name="get_back_to_start"))
get_notified.insert(unsubscribe)

news_list = InlineKeyboardButton(text="Список новостей", callback_data=get_callback.new(item_name="news_list"))
get_notified.insert(news_list)

backtostart = InlineKeyboardButton(text="Вернуться в начало", callback_data=get_callback.new(item_name="bacs"))
get_notified.insert(backtostart)


long_term = InlineKeyboardMarkup(row_width=2)#made keyboard for buttons for viza info

educ = InlineKeyboardButton(text="С целью обучения", callback_data=get_callback.new(item_name="education_cz"))
long_term.insert(educ)

family = InlineKeyboardButton(text="Соединения семьи", callback_data=get_callback.new(item_name="family1"))
long_term.insert(family)


sport = InlineKeyboardButton(text="С целью спорта", callback_data=get_callback.new(item_name="sport1"))
long_term.insert(sport)


difference = InlineKeyboardButton(text="Долгосрочная и Краткосрочная", callback_data=get_callback.new(item_name="how differ1"))
long_term.insert(difference)


bis = InlineKeyboardButton(text="Предпринимательства", callback_data=get_callback.new(item_name="bis"))
long_term.insert(bis)


long_list = InlineKeyboardButton(text="Список статей", callback_data=get_callback.new(item_name="long_list"))
long_term.insert(long_list)


backtoviza = InlineKeyboardButton(text="Вернуться в визовую информацию", callback_data=get_callback.new(item_name="vb"))
long_term.insert(backtoviza)


back_to_long_term = InlineKeyboardMarkup(row_width=2)

get_back_to_start_from_covid = InlineKeyboardMarkup(row_width=2)
back = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="getbacklong"))
get_back_to_start_from_covid.insert(back)


get_back_from_education = InlineKeyboardMarkup(row_width=2)
back = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="get back to long viza"))
get_back_from_education.insert(back)


get_back_to_mailing = InlineKeyboardMarkup(row_width=2)#made button which gwts back to subcribe prosses
back1 = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="subagain"))
get_back_to_mailing.insert(back1)


back_to_long_term = InlineKeyboardMarkup(row_width=2)

get_back = InlineKeyboardButton(text="Вернуться в долгосрочную визу", callback_data=get_callback.new(item_name="56"))
back_to_long_term.insert(get_back)
from telepot.namedtuple import InlineKeyboardButton, ReplyKeyboardMarkup

k1 = ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="Settings", callback_data='setting'),
                                    InlineKeyboardButton(text="Start", callback_data='start')]], one_time_keyboard=True,
                         resize_keyboard=True)

k2 = ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="Year", callback_data='year')]], one_time_keyboard=True,
                         resize_keyboard=True)

k4 = ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="Back", callback_data='back')]], one_time_keyboard=True,
                         resize_keyboard=True)

k5 = ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="1900", callback_data='1900'),
                                    InlineKeyboardButton(text="1920", callback_data='1920'),
                                    InlineKeyboardButton(text="1950", callback_data='1950'),
                                    InlineKeyboardButton(text="1980", callback_data='1980'),
                                    InlineKeyboardButton(text="1990", callback_data='1990'),
                                    InlineKeyboardButton(text="2000", callback_data='2000'),
                                    InlineKeyboardButton(text="Back", callback_data='back')]], one_time_keyboard=True,
                         resize_keyboard=True)

k6 = ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="Settings", callback_data='setting'),
                                    InlineKeyboardButton(text="Continue", callback_data='back')]],
                         one_time_keyboard=True, resize_keyboard=True)

k7 = ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="Give me other results", callback_data='another_one'),
                                    InlineKeyboardButton(text="Settings", callback_data='setting')]],
                         one_time_keyboard=True, resize_keyboard=True)

k8 = ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="Settings", callback_data='setting')]],
                         one_time_keyboard=True, resize_keyboard=True)
from pathlib import Path
from whaaaaat import style_from_dict, Token

whatsapp_selectors_dict = {
    'login_area':'#app > div > div > div.landing-header',
    'new_chat_button': '#side > header div[role="button"] span[data-icon="chat"]',
    'search_contact_input': '#app > div > div span > div > span > div div > label > input',
    'contact_list_elements_filtered': '#app > div > div span > div > span > div div > div div > div div > span > span[title][dir]',
    'group_list_elements_filtered': '#app > div > div span > div > span > div div > div div > div div > span[title][dir]',
    'target_focused_title': '#main > header div > div > span[title]',
    'message_area': '#main > footer div.selectable-text[contenteditable]',
    'status':'#main > header > div > div > span[title]'
}


websites = {'whatsapp': 'https://web.whatsapp.com/'}


data_folder_path = Path.home()/'wplay'
user_data_folder_path = Path.home()/'wplay'/'.userData'

menu_style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})
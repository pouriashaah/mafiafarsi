import random

help_text = [
    "```List of commands```",
    "Type `commands` below to receive details about it.",
    "**1. !roles**: `a detailed guide on roles`",
    "**2. !game_start_guide**: `a step by step guide on how to start a game`",
    "**3. !mafia_story**: `mafia story detail`"
]


roles_text = [
    "**Roles:**",
     "Type `commands` below with `!roles` at the start of it to receive details about it.`(example:!roles citizen)`",
    "`citizen`: city-aligned role. No special powers.",
    "`mafia`: Mafia-aligned role. Capable of killing a citizen during nighttime with fellow mafia."
]

start_guide_text = [
    "**Game_Start_Guide:**",
     " some start guide",
]

mafia_story_text = [
    "**Mafia_Story:**",
     "some mafia story",
]


roles = {
    'citizen':'city-aligned role. No special powers.',
    'mafia':'Mafia-aligned role. Capable of killing a citizen during nighttime with fellow mafia.'
}

def handle_response(message) -> str:
    query = message.split()
    p_message = message.lower()



    if len(query) == 1:

        if p_message=='hello':
            return 'Hey There!'

        if p_message=='roll':
            return str(random.randint(1,6))


        if p_message=='!help':
            return  '\n'.join(help_text)


        if p_message=='!roles':
            return  '\n'.join(roles_text)

        if p_message=='!game_start_guide':
                return  '\n'.join(start_guide_text)

        if p_message=='!mafia_story':
                return  '\n'.join(mafia_story_text)


    elif len(query) == 2 and query[1] in roles and query[0] == '!roles':
            return roles[query[1]]


    # return "نمیفهمم چی زر میزنی !"
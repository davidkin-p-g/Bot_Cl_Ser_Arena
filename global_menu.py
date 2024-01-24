# -*- coding: utf-8 -*-
from interactions import Extension, slash_command, SlashContext
# Импрот Embed
from interactions import Embed, EmbedFooter, EmbedField
# Импорт Components
from interactions import ActionRow, Button, ButtonStyle, StringSelectMenu, ComponentContext, component_callback
# Импорт Paginator (Нумирация страниц)
from interactions.ext.paginators import Paginator


class GlobalMenu(Extension):
    def __init__(self, bot) -> None:
        # Форма сообщеня для главного меню
        self.embeds_global_menu = Embed(
            color=0x4F638C,
            title=f"Меню ",
            description=f"Главное меню для работы с ботом ThunderArena.",
            footer= EmbedFooter(text="По всем вопросам обращаться к администрации\nБот написан @Suglinca#6900"),
            fields=[
                EmbedField(
                name="Личный профиль",
                value=f'''В личном профиле вы можете просматривать и редактировать всю необходимую личную информацию для использования нашей платформы.\n
                **Доступные возможности**
                • Регистрация
                • Изменение Рейтинга, Роли, Имени
                • Просмотр Вашего профиля и достижений''',
                inline=True,
                ),
                EmbedField(
                name="Командный профиль",
                value=f'''Командный профиль создан для взаимодействия с вашей командой зарегистрированной на нашей платформе.\n
                **Доступные возможности**
                • Создание команды
                • Изменение параметров команды
                •...''',
                inline=True,
                )
            ]
        )
            
        # Форма компонентов для главного меню
        self.components_global_menu: list[ActionRow] = [ ActionRow(
                 Button(
                    style=ButtonStyle.SECONDARY,
                    label="Личный Профиль",
                    custom_id="user_profile",
                ),
                 Button(
                    style=ButtonStyle.SECONDARY,
                    label="Командный профиль",
                    custom_id="comand_profile",
                )
            )
        ]

        print('Load extension global menu')
        pass


    @slash_command()
    async def seng_global_menu(self, ctx : SlashContext):
        try:
            # Вызов главного меню по средставам slash команды
            await ctx.send(embed=self.embeds_global_menu, components=self.components_global_menu, ephemeral=True)
        except Exception as e:
            await ctx.send('Во время вывода главного меню произошла непредвиденная ошибка. Прозьба сообщить администрации о проблеме.')

    

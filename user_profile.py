# -*- coding: utf-8 -*-
from interactions import Extension, slash_command, SlashContext
# Импрот Embed
from interactions import Embed, EmbedFooter, EmbedField
# Импорт Components
from interactions import ActionRow, Button, ButtonStyle, StringSelectMenu, ComponentContext, component_callback
# Импорт Paginator (Нумирация страниц)
from interactions.ext.paginators import Paginator


class UserProfile(Extension):
    def __init__(self, bot) -> None:
        # ...
        
        print('Load extension user profile')
        pass

    

    # Просушивания конпки вызова личного профиля
    @component_callback('user_profile')
    async def user_profile(self, ctx : ComponentContext):
        # Запрос модели профиля пользователя
        # Формирование Embed личного профиля
        embed_user_profile = self.embed_user_profile_function(ctx.author_id)
        # Формирование Components личного профиля

        # Редактирование меню в личный профиль
        await ctx.edit_origin(embed=self.embeds_user_profile, components=self.components_user_profile)
    
    def embed_user_profile_function(self, user_id : int):

        pass
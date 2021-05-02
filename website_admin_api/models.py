from django.db import models

from wagtail.core.models import Page,Orderable
from wagtail.core.fields import RichTextField,Creator,StreamField
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

#api
from wagtail.api import APIField


from phonenumber_field.modelfields import PhoneNumberField
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from django.utils import timezone
#Теги
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from modelcluster.models import ClusterableModel



class HomePage(Page):
    contact_data_email = models.EmailField(blank=False,verbose_name='Email для связи',default='example@mail.com')
    contact_data_phone = PhoneNumberField(blank=False, region='UA', verbose_name='Контактный номер',default='+380999999999')

    company_position = RichTextField(blank=True,verbose_name='Позиция/философия компании')
    content_panels = Page.content_panels + [
        FieldPanel('company_position', classname="full"),
        FieldPanel('contact_data_email', ),
        FieldPanel('contact_data_phone', ),
        InlinePanel('gallery_images', label="Галлерея изображений"),
    ]

    api_fields = [
        APIField('title_ru'),
        APIField('title_uk'),
        APIField('company_position_ru'),
        APIField('company_position_uk'),
        APIField('contact_data_email'),
        APIField('contact_data_phone'),
        APIField('contact_data_phone'),
        APIField('gallery_images'),
        APIField('about_company_page'),

          # This will nest the relevant BlogPageAuthor objects in the API response
    ]
    class Meta:
        verbose_name='Главная страница'



class HomeHeaderGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250,verbose_name='Подпись к изображению')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
    api_fields = [
        APIField('image'),
        APIField('caption'),
    ]

class AboutCompanyPage(Page):
    # page=ParentalKey(HomePage, on_delete=models.CASCADE, related_name='about_company_page',verbose_name='Домашння страница для страницы "О компании"')
    page=models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='about_company_page',verbose_name='Домашння страница для страницы "О компании"')
    # home_page=models.ForeignKey(HomePage,on_delete=models.CASCADE, related_name='home_page_about_company',verbose_name='О компании 2')
    about_company_text = RichTextField(blank=False,verbose_name='Текст о компании')
    content_panels = Page.content_panels + [
        FieldPanel('page',),
        FieldPanel('about_company_text', classname="full"),
        # InlinePanel('activities', label="Виды деятельности"),
    ]
    # parent_page_types=['home.HomePage']

    api_fields = [
        APIField('about_company_text_ru'),
        APIField('about_company_text_uk'),
        # APIField('activities_page'),
        # APIField('activities'),
    ]
    parent_page_types = ['website_admin_api.HomePage']
    class Meta:
        verbose_name='О компании'

class ActivitiesPage(Page):
    home_page=models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='activities_page',verbose_name='Домашння страница для страницы Направления деятельности')

    content_panels = Page.content_panels + [
        FieldPanel('home_page', ),
        InlinePanel('activities', label="Виды деятельности"),
    ]
    api_fields = [

        APIField('home_page'),
        APIField('activities'),
    ]
    parent_page_types = ['website_admin_api.HomePage']
    class Meta:
        verbose_name='Страница "услуги / направления деятельности"'

class Activities(Orderable):
    page=ParentalKey(ActivitiesPage, on_delete=models.CASCADE, related_name='activities',verbose_name='Вид деятельности')
    kind_of_activity=models.TextField(max_length=1000,verbose_name='Вид деятельности')
    activity_image=models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='activity_image',
        verbose_name='Изображение для вида деятельности',blank=False)
    activity_image_caption = models.CharField(blank=True, max_length=250, verbose_name='Подпись к изображению')
    panels = [
        FieldPanel('kind_of_activity'),
        ImageChooserPanel('activity_image'),
        FieldPanel('activity_image_caption'),
    ]
    def __str__(self):
        return self.kind_of_activity

    api_fields = [
        APIField('kind_of_activity_ru'),
        APIField('kind_of_activity_uk'),
        APIField('activity_image'),
        APIField('activity_image_caption_ru'),
        APIField('activity_image_caption_uk'),
    ]



class HeadingNewsPublicationsTypes(Orderable,ClusterableModel):
# class HeadingNewsPublicationsTypes(Orderable):
    name_heading_ru=models.CharField(max_length=255,verbose_name='Название рубрики')
    name_heading_uk=models.CharField(max_length=255,verbose_name='Назва рубрики',)

    def __str__(self):
        return self.name_heading_ru + '/' + self.name_heading_uk

    class Meta:
        verbose_name_plural='Рубрики для новостей/публикаций'
        verbose_name='Рубрики для новостей/публикаций'


    content_panels = Page.content_panels + [
        FieldPanel('name_heading_ru'),
        FieldPanel('name_heading_uk'),
    ]


    api_fields = [
            APIField('name_heading_ru'),
            APIField('name_heading_uk'),
        ]

class NewsPublicationPage(Page):
    home_page=models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='news_publication_page',verbose_name='Домашння страница для страницы "Новости"')
    content_panels = Page.content_panels + [
        FieldPanel('home_page',),
    ]
    parent_page_types=['website_admin_api.HomePage']

    api_fields = [
        APIField('news_publications'),
    ]
class NewsPublicationTag(TaggedItemBase):

    content_object = ParentalKey(
        'NewsPublication',
        related_name='tagged_items',
        on_delete=models.CASCADE,
        verbose_name = 'Теги',
    )


    api_fields = [
        APIField('content_object'),
    ]
    class Meta:
        verbose_name='Новости/Публикации'

# class NewsPublicationPage(Page,models.Model):
class NewsPublication(Page,Orderable):
    page = ParentalKey(NewsPublicationPage, on_delete=models.CASCADE, related_name='news_publications',
                       verbose_name='Новости/Публикации')
    publication_heading=ParentalKey(HeadingNewsPublicationsTypes,related_name='publication',on_delete=models.CASCADE,verbose_name='Название рубрики')
    publication_title=models.CharField(max_length=255,verbose_name='Название публикации/новости')
    publication_text =models.TextField(max_length=10000,verbose_name='Текст публикации/новости')
    tags = ClusterTaggableManager(through=NewsPublicationTag,blank=True,related_name='news_tags')

    publication_image = models.ForeignKey('wagtailimages.Image', blank=False,
                                                                 on_delete=models.CASCADE,
                                                                 related_name='+',)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации/новости')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания публикации/новости',
                                   editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения публикации/новости')
    caption = models.CharField(blank=True, max_length=255, verbose_name='Подпись к изображению')

    content_panels = Page.content_panels + [
        FieldPanel('page', ),
        MultiFieldPanel([
            FieldPanel('tags'),
        ], heading="Теги"),
        MultiFieldPanel([
            FieldPanel('publication_heading'),
            FieldPanel('publication_title'),
            FieldPanel('publication_text'),
        ], heading="Текстовая информация публикации"),
        MultiFieldPanel([
            ImageChooserPanel('publication_image'),
            FieldPanel('caption'),
        ], heading="Изображение для публикации/новости"),
    ]
    api_fields = [
        APIField('publication_heading'),
        APIField('publication_title_ru'),
        APIField('publication_title_uk'),
        APIField('publication_text_ru'),
        APIField('publication_text_uk'),
        APIField('tags'),
        APIField('publication_image'),
        APIField('caption_ru'),
        APIField('caption_uk'),
    ]
    parent_page_types = ['website_admin_api.NewsPublicationPage']
    class Meta:
        verbose_name='Отдельная Новость/Публикация'

# class HeadingNewsPublications(Orderable,models.Model):
#     page = ParentalKey(NewsPublicationPage, on_delete=models.CASCADE,related_name='news_page_headings', verbose_name='Страница новости',)
#     heading_name=models.ForeignKey(HeadingNewsPublicationsTypes,on_delete=models.CASCADE,verbose_name='Рубрика',related_name='heading_name')
#     panels = [
#         SnippetChooserPanel('heading_name'),
#     ]

class TeamPage(Page):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='team_page',
                             verbose_name='Домашняя страница для страницы команды')
    key_phrase_title=models.CharField(max_length=255,verbose_name='Ключевая фраза/Заголовок (о кадровой политике компании)')
    key_phrase_text = RichTextField(verbose_name='Текст-расшифровка ключевой фразы/заголовка')
    content_panels = [
        FieldPanel('page',),
        FieldPanel('title',),
        FieldPanel('key_phrase_title'),
        FieldPanel('key_phrase_text'),
        # InlinePanel('team_members', label="Участники команды"),
    ]

    api_fields = [
        APIField('title_ru'),
        APIField('title_uk'),
        APIField('key_phrase_title_ru'),
        APIField('key_phrase_title_uk'),
        APIField('key_phrase_text_ru'),
        APIField('key_phrase_text_uk'),
        APIField('team_members'),
    ]
    parent_page_types = ['website_admin_api.HomePage']
    class Meta:
        verbose_name='Команда'


class TeamMember(Page,Orderable):
    page=ParentalKey(TeamPage, on_delete=models.CASCADE, related_name='team_members',verbose_name='Учасник команды')
    full_name=models.CharField(max_length=255,verbose_name='ФИО',blank=False)
    competence=models.TextField(max_length=510,verbose_name='сфера компетенции',blank=False)
    professional_credo=models.TextField(max_length=510,verbose_name='Профессиональное кредо',blank=False)
    additional_information=models.TextField(max_length=1000,verbose_name='Дополнительная информация')
    photo=models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='photo',
        verbose_name='Фото учасника команды', blank=False)
    photo_caption = models.CharField(blank=True, max_length=250, verbose_name='Подпись к изображению')

    def __str__(self):
        return self.full_name

    content_panels = [
        FieldPanel('title'),
        FieldPanel('page'),
        FieldPanel('full_name'),
        FieldPanel('competence'),
        FieldPanel('professional_credo'),
        FieldPanel('additional_information'),
        ImageChooserPanel('photo'),
        FieldPanel('photo_caption'),
    ]

    api_fields = [

        APIField('title_ru'),
        APIField('title_uk'),
        APIField('full_name_ru'),
        APIField('full_name_uk'),
        APIField('competence_ru'),
        APIField('competence_uk'),
        APIField('professional_credo_ru'),
        APIField('professional_credo_uk'),
        APIField('additional_information_ru'),
        APIField('additional_information_uk'),
        APIField('photo'),
        APIField('photo_caption_ru'),
        APIField('photo_caption_uk'),
    ]
    class Meta:
        verbose_name='Участник команды'

    parent_page_types = ['website_admin_api.TeamPage']


class ContactsPage(Page):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='contact_page',
                             verbose_name='Домашняя страница для страницы "Контакты"')

    content_panels = [
        FieldPanel('page',),
        FieldPanel('title',),
    ]

    api_fields = [
        APIField('title_ru'),
        APIField('title_uk'),
        APIField('contacts'),
    ]
    parent_page_types = ['website_admin_api.HomePage']
    class Meta:
        verbose_name='Контакты'

class Contacts(Page,Orderable):
    page = ParentalKey(ContactsPage, on_delete=models.CASCADE, related_name='contacts', verbose_name='Елементы списка контактов')
    subject_of_request=models.CharField(max_length=255,verbose_name='Компетенция представителя')
    full_name=models.CharField(max_length=255,verbose_name='Полное имя представителя компании')
    email = models.EmailField(blank=True, verbose_name='Email для связи', default='example@mail.com')
    phone = PhoneNumberField(blank=True, region='UA', verbose_name='Контактный номер',
                                          default='+380999999999')

    content_panels = [
        FieldPanel('page',),
        FieldPanel('title',),
        FieldPanel('subject_of_request',),
        FieldPanel('full_name',),
        FieldPanel('email',),
        FieldPanel('phone',),
    ]

    api_fields = [
        APIField('title_ru'),
        APIField('title_uk'),
        APIField('subject_of_request_ru'),
        APIField('subject_of_request_uk'),
        APIField('full_name_ru'),
        APIField('full_name_uk'),
        APIField('email'),
        APIField('phone'),
    ]
    parent_page_types = ['website_admin_api.ContactsPage']
    class Meta:
        verbose_name='Елемент списка контактов'

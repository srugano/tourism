from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField


class HomePage(Page):
    lead_text = models.CharField(
        max_length=140, blank=True, help_text="Subheading text under the banner title"
    )
    button = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="Select an optional text to link to",
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50, default="Read More", blank=False, help_text="Read more "
    )
    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
    ]


class LongTextPage(Page):
    text_field = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("text_field", classname="full")]


class CardsPage(Page):
    """
    This will be used for example for showing multiple tours or Blog items
    """

    text_field = RichTextField(blank=True)
    cards = ParentalManyToManyField(
        "wagtailcore.Page",
        blank=True,
        # null=True,
        related_name="page_cards",
        help_text="Select a page to create card",
        # on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                PageChooserPanel("cards")
                # DocumentChooserPanel('book_file'),
                # PageChooserPanel('publisher'),
            ],
            heading="Collection of Book Fields",
            classname="collapsible collapsed",
        )
    ]


class TourPage(Page):
    # Add other things after
    text_field = RichTextField(blank=True)
    main_picture = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The main picture for the tour",
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("text_field", classname="full"),
        ImageChooserPanel("main_picture"),
    ]

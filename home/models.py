from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    MultiFieldPanel,
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import RichTextBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from streams import blocks

NEW_TABLE_OPTIONS = {
    "minSpareRows": 0,
    "startRows": 4,
    "startCols": 4,
    "colHeaders": False,
    "rowHeaders": True,
    "contextMenu": [
        "row_above",
        "row_below",
        "---------",
        "col_left",
        "col_right",
        "---------",
        "remove_row",
        "remove_col",
        "---------",
        "undo",
        "redo",
    ],
    "editor": "text",
    "stretchH": "all",
    "renderer": "text",
    "autoColumnSize": False,
}


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = [
        "flex.FlexPage",
        "services.ServiceListingPage",
        "contact.ContactPage",
    ]
    max_count = 1
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
    body = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("cards", blocks.CardBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("cta", blocks.CallToActionBlock()),
            (
                "testimonial",
                SnippetChooserBlock(
                    target_model="testimonials.Testimonial",
                    template="streams/testimonial_block.html",
                ),
            ),
            (
                "pricing_table",
                blocks.PricingTableBlock(table_options=NEW_TABLE_OPTIONS),
            ),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel("body"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["tours"] = TourPage.objects.live().public()
        return context


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
    short_description = RichTextField(blank=True)
    main_picture = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The main picture for the tour",
        on_delete=models.SET_NULL,
    )
    body = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("rich_text", RichTextBlock()),
            ("cards", blocks.CardBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("cta", blocks.CallToActionBlock()),
            (
                "testimonial",
                SnippetChooserBlock(
                    target_model="testimonials.Testimonial",
                    template="streams/testimonial_block.html",
                ),
            ),
            (
                "pricing_table",
                blocks.PricingTableBlock(table_options=NEW_TABLE_OPTIONS),
            ),
        ],
        null=True,
        blank=True,
    )
    duration = models.CharField(
        max_length=140, blank=True, help_text="The duration. eg: 2 days"
    )

    content_panels = Page.content_panels + [
        FieldPanel("short_description", classname="full"),
        ImageChooserPanel("main_picture"),
        FieldPanel("duration"),
        StreamFieldPanel("body"),
    ]

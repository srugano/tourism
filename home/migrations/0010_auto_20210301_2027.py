# Generated by Django 3.0.11 on 2021-03-01 20:27

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_tourpage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourpage',
            name='text_field',
        ),
        migrations.AlterField(
            model_name='tourpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max lenght 100 characters', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional help text for this card. Max lenght is 500 characters.', max_length=500, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image automatically croped to 570px by 370px')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_page', wagtail.core.blocks.URLBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image to be automatically cropped to 786px by 552px')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on the left with text on the Right. Or image in the right with text on the left')), ('title', wagtail.core.blocks.CharBlock(help_text='Max lenght of 60 character.', max_length=60)), ('text', wagtail.core.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_page', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Max length of 200 characters', max_length=200)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_page', wagtail.core.blocks.URLBlock(required=False))]))])), ('testimonial', wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonial', template='streams/testimonial_block.html')), ('pricing_table', streams.blocks.PricingTableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo'], 'editor': 'text', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 4, 'stretchH': 'all'}))], blank=True, null=True),
        ),
    ]
